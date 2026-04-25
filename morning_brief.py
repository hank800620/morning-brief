#!/usr/bin/env python3
"""Morning Brief email sender via Resend HTTPS API.

Reads the brief body from stdin (or --body-file), takes subject from --subject,
renders markdown to HTML, and POSTs to https://api.resend.com/emails.

Why Resend instead of Gmail SMTP: the Anthropic routine sandbox firewalls
all SMTP ports (25/465/587), so App Password auth can't establish a connection.
Resend uses HTTPS (port 443) which the sandbox allows.

Usage:
    python3 morning_brief.py --subject "[morning-brief-bot] 2026-04-25 ..." < body.md
    python3 morning_brief.py --subject "..." --body-file body.md
    python3 morning_brief.py --subject "..." --body-file body.md --dry-run

Env vars required:
    RESEND_API_KEY  — Resend API key (re_...)
    TO_EMAIL        — Recipient email

Env vars optional:
    RESEND_FROM     — Sender. Default: "Morning Brief <onboarding@resend.dev>"
                      (the resend.dev sandbox sender works without domain verification.)
"""
from __future__ import annotations

import argparse
import html
import json
import os
import re
import sys
import urllib.error
import urllib.request


# Minimal markdown -> HTML for the subset we use:
# headings, bold, inline code, links, hr, unordered list, paragraphs.
def md_to_html(text: str) -> str:
    lines = text.split("\n")
    out: list[str] = []
    in_list = False

    def close_list():
        nonlocal in_list
        if in_list:
            out.append("</ul>")
            in_list = False

    def inline(s: str) -> str:
        s = html.escape(s)
        s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
        s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
        s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)",
                   lambda m: f'<a href="{m.group(2)}">{m.group(1)}</a>', s)
        return s

    for raw in lines:
        line = raw.rstrip()
        if not line.strip():
            close_list()
            out.append("")
            continue
        if line.strip() == "---":
            close_list()
            out.append("<hr>")
            continue
        m = re.match(r"^(#{1,6})\s+(.+)$", line)
        if m:
            close_list()
            level = len(m.group(1))
            out.append(f"<h{level}>{inline(m.group(2))}</h{level}>")
            continue
        m = re.match(r"^[-*]\s+(.+)$", line)
        if m:
            if not in_list:
                out.append("<ul>")
                in_list = True
            out.append(f"<li>{inline(m.group(1))}</li>")
            continue
        close_list()
        out.append(f"<p>{inline(line)}</p>")
    close_list()
    return "\n".join(out)


EMAIL_CSS = """
body { font-family: -apple-system, "Segoe UI", "Microsoft JhengHei", sans-serif;
       max-width: 760px; margin: 0 auto; padding: 16px; line-height: 1.55; color: #222; }
h1 { border-bottom: 2px solid #333; padding-bottom: 8px; }
h2 { margin-top: 28px; border-left: 4px solid #4a90e2; padding-left: 10px; }
h3 { margin-top: 20px; color: #1a1a1a; }
a { color: #1f6feb; text-decoration: none; }
a:hover { text-decoration: underline; }
hr { border: none; border-top: 1px solid #ddd; margin: 24px 0; }
ul { padding-left: 22px; }
strong { color: #111; }
code { background: #f4f4f4; padding: 2px 5px; border-radius: 3px; font-family: ui-monospace, monospace; }
"""


def render_html(body_md: str) -> str:
    return (
        "<!doctype html><html><head><meta charset='utf-8'>"
        f"<style>{EMAIL_CSS}</style></head><body>{md_to_html(body_md)}</body></html>"
    )


def send_via_resend(subject: str, body_md: str) -> str:
    api_key = os.environ["RESEND_API_KEY"]
    to_email = os.environ["TO_EMAIL"]
    from_addr = os.environ.get("RESEND_FROM", "Morning Brief <onboarding@resend.dev>")

    payload = {
        "from": from_addr,
        "to": [to_email],
        "subject": subject,
        "text": body_md,
        "html": render_html(body_md),
    }

    req = urllib.request.Request(
        "https://api.resend.com/emails",
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            result = json.loads(resp.read().decode("utf-8"))
            return result.get("id", "<no-id>")
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"Resend API {e.code}: {body}") from e


def main() -> int:
    parser = argparse.ArgumentParser(description="Send the morning brief via Resend.")
    parser.add_argument("--subject", required=True, help="Full email subject line")
    parser.add_argument("--body-file", help="Path to markdown body (defaults to stdin)")
    parser.add_argument("--dry-run", action="store_true", help="Print instead of sending")
    args = parser.parse_args()

    if args.body_file:
        with open(args.body_file, "r", encoding="utf-8") as f:
            body_md = f.read()
    else:
        body_md = sys.stdin.read()

    if not body_md.strip():
        print("ERROR: empty body", file=sys.stderr)
        return 1

    if args.dry_run:
        print(f"Subject: {args.subject}\n")
        print(body_md)
        return 0

    msg_id = send_via_resend(args.subject, body_md)
    print(f"Sent: {args.subject} (resend id: {msg_id})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
