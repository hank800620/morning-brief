"""MorningBrief class for parsing and handling morning brief content."""
from __future__ import annotations

from typing import Optional
from .parser import parse_brief
from . import __init__ as mb_types


class MorningBrief:
    def __init__(self, title: str, body: str):
        self.title = title
        self.body = body
        self._data: Optional[mb_types.MorningBriefData] = None

    @property
    def data(self) -> mb_types.MorningBriefData:
        """Lazily parse and return structured data."""
        if self._data is None:
            self._data = parse_brief(self.body)
        return self._data

    @property
    def meta_capex(self) -> Optional[str]:
        """Extract Meta Capex statement from TLDR."""
        tldr = self.data.get("tldr")
        return tldr["meta_capex"] if tldr and "meta_capex" in tldr else None

    @property
    def gpt_version(self) -> Optional[str]:
        """Extract GPT model version from AI section."""
        ai = self.data.get("ai_insight")
        return ai["gpt_version"] if ai and "gpt_version" in ai else None

    @property
    def automation_rate(self) -> Optional[int]:
        """Extract desktop automation rate from AI section."""
        ai = self.data.get("ai_insight")
        return ai["automation_rate"] if ai and "automation_rate" in ai else None