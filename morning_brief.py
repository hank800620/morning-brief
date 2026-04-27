#!/usr/bin/env python3
"""Morning Brief delivery via GitHub Issue.

Reads the brief body from stdin (or --body-file), takes title from --subject,
and POSTs to https://api.github.com/repos/<repo>/issues to create an issue.

Why GitHub Issue instead of email: the Anthropic routine sandbox blocks all
SMTP ports AND all third-party email APIs at its egress firewall (responds
with HTTP 403 "Host not in allowlist"). GitHub's API is on the sandbox
allowlist, so this works. GitHub auto-emails the watcher when the issue is
created, so the user still receives an email at their normal inbox — the
difference is GitHub sends it, not us.

Usage:
    python3 morning_brief.py --subject "[morning-brief-bot] 2026-04-25 ..." < body.md
    python3 morning_brief.py --subject "..." --body-file body.md
    python3 morning_brief.py --subject "..." --body-file body.md --dry-run

Env vars required:
    GITHUB_TOKEN  — PAT or OAuth token with `issues: write` on the target repo

Env vars optional:
    GITHUB_REPO   — `owner/repo`. Default: "hank800620/morning-brief"
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request


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
    parts: list[str] = []
    for issue in issues:
        parts.append(f"=== {issue['title']} ===")
        parts.append(f"URL: {issue.get('html_url', '')}")
        parts.append(f"Created: {issue.get('created_at', '')}")
        body = issue.get("body") or "(empty)"
        # Cap each body at 2500 chars — enough to capture title + Today's Insight +
        # top items + Talking Points, but not bloat downstream LLM context.
        parts.append(body[:2500])
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
    parser = argparse.ArgumentParser(description="Post the morning brief as a GitHub issue.")
    parser.add_argument("--subject", help="Issue title (required unless --fetch-recent)")
    parser.add_argument("--body-file", help="Path to markdown body (defaults to stdin)")
    parser.add_argument("--label", action="append", default=[],
                        help="Label to attach (repeatable). Or filter for --fetch-recent.")
    parser.add_argument("--dry-run", action="store_true", help="Print instead of posting")
    parser.add_argument("--fetch-recent", action="store_true",
                        help="Print recent issues for the given --label (for routine memory).")
    parser.add_argument("--limit", type=int, default=7,
                        help="Number of recent issues to fetch (used with --fetch-recent).")
    args = parser.parse_args()

    if args.fetch_recent:
        if not args.label:
            print("ERROR: --fetch-recent requires --label", file=sys.stderr)
            return 1
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
