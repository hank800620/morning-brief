from typing import TypedDict


class TLDRPoint(TypedDict):
    meta_capex: str
    arm_earnings: str
    us_china_summit: str


class AIDetail(TypedDict):
    gpt_version: str
    automation_rate: int
    revenue: str
    cloud_partners: list[str]


class MorningBriefData(TypedDict, total=False):
    date: str
    window_start: str
    window_end: str
    tldr: TLDRPoint
    ai_insight: AIDetail