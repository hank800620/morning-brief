#!/usr/bin/env python3
"""Morning Brief email sender. Plain-text + HTML (lightweight) via Gmail SMTP.

Reads the brief body from stdin (or --body-file), takes subject from --subject,
and sends. No external deps — uses stdlib only so no pip install is required
inside the routine sandbox.

Usage:
    python3 morning_brief.py --subject "[morning-brief-bot] 2026-04-25 ..." < body.md
    python3 morning_brief.py --subject "..." --body-file body.md
    python3 morning_brief.py --subject "..." --body-file body.md --dry-run

Env vars required (set by the routine before invoking):
    GMAIL_USER           — Gmail address sending the mail
    GMAIL_APP_PASSWORD   — 16-char App Password (NOT the real Google password)
    TO_EMAIL             — Recipient (defaults to GMAIL_USER if unset)
"""
from __future__ import annotations

import argparse
import html
import os
import re
import smtplib
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# Minimal markdown → HTML converter covering the subset we use:
# headings (#..######), bold (**), inline code (`), links ([t](u)),
# horizontal rule (---), unordered list (-), paragraphs.
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


def send_email(subject: str, body_md: str) -> None:
    gmail_user = os.environ["GMAIL_USER"]
    gmail_pw = os.environ["GMAIL_APP_PASSWORD"]
    to_email = os.environ.get("TO_EMAIL", gmail_user)

    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = gmail_user
    msg["To"] = to_email
    msg.attach(MIMEText(body_md, "plain", "utf-8"))
    msg.attach(MIMEText(render_html(body_md), "html", "utf-8"))

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, timeout=30) as s:
        s.login(gmail_user, gmail_pw)
        s.send_message(msg)


def main() -> int:
    parser = argparse.ArgumentParser(description="Send the morning brief via Gmail SMTP.")
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

    send_email(args.subject, body_md)
    print(f"Sent: {args.subject}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
