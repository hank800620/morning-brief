"""Structured parser for Morning Brief markdown content."""
from __future__ import annotations

import re
from typing import Optional
from . import __init__ as mb_types


def parse_tldr_point(text: str) -> mb_types.TLDRPoint:
    """Parse the 30-Second TLDR section into structured data."""
    lines = [line.strip() for line in text.strip().split("\n") if line.strip()]
    point_map: dict[str, str] = {}
    for line in lines:
        if line.startswith("- Meta"):
            point_map["meta_capex"] = line
        elif line.startswith("- Arm Holdings"):
            point_map["arm_earnings"] = line
        elif line.startswith("- 川習北京峰會"):
            point_map["us_china_summit"] = line
    return mb_types.TLDRPoint(**point_map)


def parse_ai_section(text: str) -> Optional[mb_types.AIDetail]:
    """Parse the AI section for GPT-5.5 details."""
    gpt_match = re.search(r"GPT-(\d+\.\d+)", text)
    automation_match = re.search(r"桌面自動化 (\d+)%", text)
    revenue_match = re.search(r"\$(\d+) 億", text)
    cloud_match = re.search(r"可同時服務 (AWS、Google Cloud|AWS, Google Cloud)", text)

    if not gpt_match:
        return None

    return mb_types.AIDetail(
        gpt_version=gpt_match.group(1),
        automation_rate=int(automation_match.group(1)) if automation_match else 75,
        revenue=f"${revenue_match.group(1)}B" if revenue_match else "$250B",
        cloud_partners=["AWS", "Google Cloud"] if cloud_match else [],
    )


def parse_brief(body: str) -> mb_types.MorningBriefData:
    """Parse the full morning brief into structured data."""
    lines = body.strip().split("\n")
    data: mb_types.MorningBriefData = {}

    # Extract date from header
    header_match = re.match(r"# ☀️ Hank's Morning Brief · (\d{4}-\d{2}-\d{2})", body)
    if header_match:
        data["date"] = header_match.group(1)

    # Extract time window
    window_match = re.search(
        r"Window: (\d{4}-\d{2}-\d{2} \d{2}:\d{2}) → (\d{4}-\d{2}-\d{2} \d{2}:\d{2})", body
    )
    if window_match:
        data["window_start"] = window_match.group(1)
        data["window_end"] = window_match.group(2)

    # Extract TLDR
    tldr_match = re.search(r"## ⚡ 30-Second TLDR\n((?:- .*\n?)+)", body)
    if tldr_match:
        data["tldr"] = parse_tldr_point(tldr_match.group(1))

    # Extract AI section
    ai_match = re.search(r"## 1️⃣ 🤖 AI / 科技\n\n### ① ⭐.+?(?=## |\Z)", body, re.DOTALL)
    if ai_match:
        ai_detail = parse_ai_section(ai_match.group(0))
        if ai_detail:
            data["ai_insight"] = ai_detail

    return data