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
from typing import Optional


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
            "Accept": "application/vnd.github.v3+json",
            "User-Agent": "morning-brief-bot",
        },
    )
    try:
        with urllib.request.urlopen(req) as response:
            issues = json.load(response)
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"GitHub API error: {e.code} {e.reason}") from e
    except urllib.error.URLError as e:
        raise RuntimeError(f"Network error: {e.reason}") from e

    output_lines = []
    for issue in issues:
        output_lines.append(f"=== {issue['title']} ===")
        output_lines.append(issue["body"])
    return "\n".join(output_lines)


def post_issue(title: str, body: str, labels: Optional[list[str]] = None) -> dict:
    """Create a GitHub issue. Returns the created issue JSON."""
    token = os.environ["GITHUB_TOKEN"]
    repo = os.environ.get("GITHUB_REPO", "hank800620/morning-brief")
    url = f"https://api.github.com/repos/{repo}/issues"
    payload = {"title": title, "body": body}
    if labels:
        payload["labels"] = labels

    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github.v3+json",
            "Content-Type": "application/json",
            "User-Agent": "morning-brief-bot",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req) as response:
            return json.load(response)
    except urllib.error.HTTPError as e:
        error_body = e.read().decode("utf-8") if e.fp else "No response body"
        raise RuntimeError(f"GitHub API error: {e.code} {e.reason} — {error_body}") from e
    except urllib.error.URLError as e:
        raise RuntimeError(f"Network error: {e.reason}") from e


def read_body(body_file: Optional[str]) -> str:
    """Read body from file or stdin."""
    if body_file:
        with open(body_file, "r", encoding="utf-8") as f:
            return f.read()
    return sys.stdin.read()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--subject", required=True, help="Issue title")
    parser.add_argument("--body-file", help="Path to file containing body")
    parser.add_argument("--dry-run", action="store_true", help="Print issue instead of posting")
    parser.add_argument("--label", action="append", help="Labels to attach to the issue")
    args = parser.parse_args()

    body = read_body(args.body_file)

    if args.dry_run:
        print(f"Title: {args.subject}")
        print(f"Body:\n{body}")
        if args.label:
            print(f"Labels: {args.label}")
        return

    if not os.environ.get("GITHUB_TOKEN"):
        raise RuntimeError("GITHUB_TOKEN environment variable is required")

    response = post_issue(args.subject, body, args.label)
    print(json.dumps(response, indent=2))


if __name__ == "__main__":
    main()