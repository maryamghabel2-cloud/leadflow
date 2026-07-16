#!/usr/bin/env python3
"""
Local UAE SEO Agent
Checks Dubai/UAE clinic keyword coverage and local intent signals.
"""

from __future__ import annotations

from dataclasses import dataclass, asdict, field
from typing import Any, Dict, List


DEFAULT_UAE_KEYWORDS = [
    "Dubai",
    "UAE",
    "clinic website",
    "dental",
    "medspa",
    "Arabic",
    "English",
    "Abu Dhabi",
    "Sharjah",
    "book",
    "appointment",
    "USDT",
]


@dataclass
class LocalSEOResult:
    target: str
    score: int
    found: List[str] = field(default_factory=list)
    missing: List[str] = field(default_factory=list)
    recommendations: List[str] = field(default_factory=list)


def analyze_local_text(target: str, text: str, keywords: List[str] | None = None) -> LocalSEOResult:
    keywords = keywords or DEFAULT_UAE_KEYWORDS
    blob = (text or "").lower()
    found = [k for k in keywords if k.lower() in blob]
    missing = [k for k in keywords if k not in found]
    score = int(round(100 * len(found) / max(1, len(keywords))))
    recs: List[str] = []
    if "Dubai" not in found and "UAE" not in found:
        recs.append("Add explicit Dubai/UAE location terms in H1/title and first paragraph.")
    if "Arabic" not in found:
        recs.append("Mention bilingual EN/AR support for UAE trust and relevance.")
    if "appointment" not in found and "book" not in found:
        recs.append("Add booking/appointment language for patient conversion intent.")
    if "dental" not in found and "medspa" not in found and "clinic" not in found:
        recs.append("Clarify niche: dental clinic / medspa / clinic website design.")
    if score < 70:
        recs.append("Create dedicated content pages for: dentist website Dubai, medspa website Dubai, clinic website UAE.")
    return LocalSEOResult(target=target, score=score, found=found, missing=missing, recommendations=recs)


def to_dict(result: LocalSEOResult) -> Dict[str, Any]:
    return asdict(result)
