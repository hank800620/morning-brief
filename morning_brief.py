#!/usr/bin/env python3
"""Morning Brief delivery.

Two delivery paths, because the Anthropic routine sandbox egress firewall has
flipped over time:

1. (current) `--emit`: write the brief to `briefs/<label>/<date>.md` with YAML
   front matter (title/label). The routine then commits + pushes; a GitHub
   Action (`.github/workflows/brief-to-issue.yml`) creates the Issue from the
   pushed file. Works because `git push` is allowed from the sandbox while
   `api.github.com` is blocked (since ~2026-06-24 — the reverse of April).
2. (legacy) `--subject` + POST to api.github.com — kept for local/manual use.

Cross-issue memory likewise has two modes: `--fetch-recent --local` reads the
`briefs/` folder in the checkout (no network); plain `--fetch-recent` hits the
GitHub API (works locally, blocked in the sandbox).

Usage:
    python3 morning_brief.py --emit --subject "[morning-brief][daily] ..." --body-file body.md --label daily
    python3 morning_brief.py --fetch-recent --local --label daily --limit 5
    python3 morning_brief.py --subject "..." --body-file body.md   # legacy API post

Env vars (legacy API paths only):
    GITHUB_TOKEN  — PAT or OAuth token with `issues: write` on the target repo
    GITHUB_REPO   — `owner/repo`. Default: "hank800620/morning-brief"
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.request

BRIEFS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "briefs")

# Per-label body cap. Higher cadence reports cover more sections
# (weekly has 對賬 + 下週重點; monthly has MTK 季度目標 + 校準) that live
# in later sections of the body — those need a higher cap so cross-issue
# memory in the next cadence can still see them.
# Caps sized so a TYPICAL issue fits fully, with headroom for anomalies.
BODY_CAP = {
    "daily": 5000,    # typical 3500-4500 chars, full body fits
    "weekly": 7000,   # typical ~5000 chars, full body fits
    "monthly": 12000, # typical ~7000+ chars, full body fits
}


def parse_front_matter(text: str) -> tuple[dict[str, str], str]:
    """Split a briefs file into (front_matter_dict, body). Files without front
    matter return ({}, whole_text)."""
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, text
    meta: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if ":" in line:
            key, _, val = line.partition(":")
            meta[key.strip()] = val.strip()
    return meta, text[end + 5:].lstrip("\n")


def fetch_recent_local(label: str, limit: int) -> str:
    """Read the N most-recent briefs for a label from briefs/<label>/ in the
    checkout. Same output format as the API path, zero network."""
    label_dir = os.path.join(BRIEFS_DIR, label)
    if not os.path.isdir(label_dir):
        return f"(no recent issues with label `{label}`)"
    files = sorted(
        (f for f in os.listdir(label_dir) if f.endswith(".md")),
        reverse=True,
    )[:limit]
    if not files:
        return f"(no recent issues with label `{label}`)"
    body_cap = BODY_CAP.get(label, 5000)
    parts: list[str] = []
    for name in files:
        with open(os.path.join(label_dir, name), "r", encoding="utf-8") as f:
            meta, body = parse_front_matter(f.read())
        parts.append(f"=== {meta.get('title', name)} ===")
        parts.append(f"Date: {meta.get('date', name[:-3])}")
        parts.append(body[:body_cap])
        parts.append("")
    return "\n".join(parts)


def emit_brief(title: str, body_md: str, label: str) -> str:
    """Write the brief to briefs/<label>/<date>.md with front matter, for the
    brief-to-issue GitHub Action to pick up on push. Returns the path."""
    m = re.search(r"\d{4}-\d{2}-\d{2}", title)
    if not m:
        raise ValueError(f"no YYYY-MM-DD date found in title: {title!r}")
    date = m.group(0)
    label_dir = os.path.join(BRIEFS_DIR, label)
    os.makedirs(label_dir, exist_ok=True)
    path = os.path.join(label_dir, f"{date}.md")
    with open(path, "w", encoding="utf-8") as f:
        f.write(f"---\ntitle: {title}\nlabel: {label}\ndate: {date}\n---\n\n")
        f.write(body_md)
    return path


def fetch_recent(label: str, limit: int) -> str:
    """Fetch the N most-recent issues with the given label, formatted as plain text
    for downstream LLM consumption. Returns one big string with === title === markers."""
    token = os.environ["GITHUB_TOKEN"]
    repo = os.environ.get("GITHUB_REPO", "hank800620/morning-brief")
    url = (
        f"https://api.github.com/repos/{repo}/issues"
        f"?state=all&labels={label}&per_page={limit}"
        f"&sort=created&direction=desc"
    )
    req = urllib.request.Request(
        url,
        headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "morning-brief-bot",
        },
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        issues = json.loads(resp.read().decode("utf-8"))
    if not issues:
        return f"(no recent issues with label `{label}`)"
    body_cap = BODY_CAP.get(label, 5000)
    parts: list[str] = []
    for issue in issues:
        parts.append(f"=== {issue['title']} ===")
        parts.append(f"URL: {issue.get('html_url', '')}")
        parts.append(f"Created: {issue.get('created_at', '')}")
        body = issue.get("body") or "(empty)"
        parts.append(body[:body_cap])
        parts.append("")
    return "\n".join(parts)


def create_issue(title: str, body_md: str, labels: list[str] | None = None) -> str:
    token = os.environ["GITHUB_TOKEN"]
    repo = os.environ.get("GITHUB_REPO", "hank800620/morning-brief")

    payload: dict = {"title": title, "body": body_md}
    if labels:
        payload["labels"] = labels

    req = urllib.request.Request(
        f"https://api.github.com/repos/{repo}/issues",
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "Content-Type": "application/json",
            "User-Agent": "morning-brief-bot",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return data.get("html_url", "<no-url>")
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"GitHub API {e.code}: {body}") from e


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):  # Windows console defaults to cp950
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser(description="Post the morning brief as a GitHub issue.")
    parser.add_argument("--subject", help="Issue title (required unless --fetch-recent)")
    parser.add_argument("--body-file", help="Path to markdown body (defaults to stdin)")
    parser.add_argument("--label", action="append", default=[],
                        help="Label to attach (repeatable). Or filter for --fetch-recent.")
    parser.add_argument("--dry-run", action="store_true", help="Print instead of posting")
    parser.add_argument("--fetch-recent", action="store_true",
                        help="Print recent issues for the given --label (for routine memory).")
    parser.add_argument("--local", action="store_true",
                        help="With --fetch-recent: read briefs/ folder instead of the GitHub API.")
    parser.add_argument("--emit", action="store_true",
                        help="Write brief to briefs/<label>/<date>.md instead of posting to the API.")
    parser.add_argument("--limit", type=int, default=7,
                        help="Number of recent issues to fetch (used with --fetch-recent).")
    args = parser.parse_args()

    if args.fetch_recent:
        if not args.label:
            print("ERROR: --fetch-recent requires --label", file=sys.stderr)
            return 1
        if args.local:
            print(fetch_recent_local(args.label[0], args.limit))
        else:
            print(fetch_recent(args.label[0], args.limit))
        return 0

    if not args.subject:
        print("ERROR: --subject is required (unless --fetch-recent)", file=sys.stderr)
        return 1

    if args.body_file:
        with open(args.body_file, "r", encoding="utf-8") as f:
            body_md = f.read()
    else:
        body_md = sys.stdin.read()

    if not body_md.strip():
        print("ERROR: empty body", file=sys.stderr)
        return 1

    if args.emit:
        if not args.label:
            print("ERROR: --emit requires --label", file=sys.stderr)
            return 1
        path = emit_brief(args.subject, body_md, args.label[0])
        print(f"Emitted: {path}")
        return 0

    if args.dry_run:
        print(f"Title: {args.subject}")
        if args.label:
            print(f"Labels: {', '.join(args.label)}")
        print()
        print(body_md)
        return 0

    url = create_issue(args.subject, body_md, labels=args.label or None)
    print(f"Posted: {url}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
