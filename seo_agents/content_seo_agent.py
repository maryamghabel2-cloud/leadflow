#!/usr/bin/env python3
"""
Content SEO Agent
Generates UAE-focused content outlines/pages for LeadFlow acquisition.
"""

from __future__ import annotations

from pathlib import Path
from typing import List


def dubai_content_briefs() -> List[dict]:
    return [
        {
            "slug": "dentist-website-dubai",
            "title": "Dentist Website Design in Dubai: What Actually Books Patients",
            "primary_keyword": "dentist website Dubai",
            "secondary": ["dental website Dubai", "clinic website UAE", "online appointment dental Dubai"],
            "intent": "commercial investigation",
            "outline": [
                "Why Dubai dental clinics lose patients with weak websites",
                "Must-have pages: services, team, before/after, insurance, booking",
                "English + Arabic bilingual expectations",
                "How a free live preview reduces buying risk",
                "Pricing packages and what you get",
                "CTA: request free preview",
            ],
        },
        {
            "slug": "medspa-website-dubai",
            "title": "Medspa Website Design in Dubai for High-Ticket Bookings",
            "primary_keyword": "medspa website Dubai",
            "secondary": ["aesthetic clinic website UAE", "botox clinic website Dubai"],
            "intent": "commercial",
            "outline": [
                "Luxury trust signals for aesthetic clinics",
                "Treatment pages that convert consults",
                "Gallery / results without medical claims issues",
                "Bilingual EN/AR positioning",
                "CTA",
            ],
        },
        {
            "slug": "clinic-website-cost-uae",
            "title": "How Much Should a Clinic Website Cost in the UAE?",
            "primary_keyword": "clinic website cost UAE",
            "secondary": ["dental website price Dubai", "website design cost Dubai clinic"],
            "intent": "commercial",
            "outline": [
                "Typical agency ranges vs productized packages",
                "Why USDT one-time packages fit international operators",
                "Launch vs Growth vs Authority",
                "CTA to /hire and /onboard",
            ],
        },
    ]


def write_markdown_articles(out_dir: Path) -> List[Path]:
    out_dir.mkdir(parents=True, exist_ok=True)
    written: List[Path] = []
    for brief in dubai_content_briefs():
        path = out_dir / f"{brief['slug']}.md"
        lines = [
            f"# {brief['title']}",
            "",
            f"**Primary keyword:** {brief['primary_keyword']}",
            f"**Secondary:** {', '.join(brief['secondary'])}",
            f"**Intent:** {brief['intent']}",
            "",
            "## Outline",
            "",
        ]
        for i, item in enumerate(brief["outline"], 1):
            lines.append(f"{i}. {item}")
        lines += [
            "",
            "## Draft intro",
            "",
            f"If you run a clinic in Dubai or the wider UAE, your website is often the first trust check before a WhatsApp message or call. "
            f"A strong {brief['primary_keyword']} setup should make services obvious, show real team proof, and let patients request an appointment in under a minute.",
            "",
            "## CTA",
            "",
            "- Free preview: [/hire](/hire)",
            "- Checkout: [/onboard](/onboard)",
            "- Sample: [/live_demos/marina_pearl_dental_live.html](/live_demos/marina_pearl_dental_live.html)",
            "",
        ]
        path.write_text("\n".join(lines), encoding="utf-8")
        written.append(path)
    return written
