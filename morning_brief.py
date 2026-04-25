#!/usr/bin/env python3
"""Morning Brief email sender.

Reads the brief body from stdin (or --body-file), takes subject from --subject,
renders markdown to HTML, sends via Gmail SMTP.

Designed to be invoked from a Claude routine: Claude gathers news and writes
the brief, then calls this script to send the email.

Usage:
    python morning_brief.py --subject "[morning-brief-bot] 2026-04-25 ..." < body.md
    python morning_brief.py --subject "..." --body-file body.md
    python morning_brief.py --subject "..." --body-file body.md --dry-run

Env vars required (set by the routine before invoking):
    GMAIL_USER           — Gmail address sending the mail
    GMAIL_APP_PASSWORD   — 16-char App Password (NOT the real Google password)
    TO_EMAIL             — Recipient (defaults to GMAIL_USER if unset)
"""
from __future__ import annotations

import argparse
import os
import smtplib
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import markdown


EMAIL_CSS = """
body { font-family: -apple-system, "Segoe UI", "Microsoft JhengHei", sans-serif;
       max-width: 760px; margin: 0 auto; padding: 16px; line-height: 1.55; color: #222; }
h1 { border-bottom: 2px solid #333; padding-bottom: 8px; }
h2 { margin-top: 28px; border-left: 4px solid #4a90e2; padding-left: 10px; }
h3 { margin-top: 20px; color: #1a1a1a; }
blockquote { border-left: 3px solid #ccc; margin: 0; padding: 6px 14px; color: #444;
             background: #fafafa; }
a { color: #1f6feb; text-decoration: none; }
a:hover { text-decoration: underline; }
hr { border: none; border-top: 1px solid #ddd; margin: 24px 0; }
ul { padding-left: 22px; }
strong { color: #111; }
"""


def render_html(body_md: str) -> str:
    body_html = markdown.markdown(
        body_md,
        extensions=["tables", "fenced_code", "nl2br", "sane_lists"],
    )
    return (
        "<!doctype html><html><head><meta charset='utf-8'>"
        f"<style>{EMAIL_CSS}</style></head><body>{body_html}</body></html>"
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

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as s:
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
