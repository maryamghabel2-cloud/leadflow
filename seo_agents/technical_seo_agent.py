#!/usr/bin/env python3
"""
Technical SEO Agent for LeadFlow
Inspired by open-source SEO audit agents (seo-audit-skill / AISeoAgent patterns).
Audits HTML for title, meta, H1, canonical, OG, Twitter, JSON-LD, images, lang.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, asdict, field
from html.parser import HTMLParser
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
from urllib.parse import urljoin, urlparse


@dataclass
class Issue:
    severity: str  # critical | high | medium | low
    code: str
    message: str
    fix_hint: str = ""


@dataclass
class PageAudit:
    url_or_path: str
    score: int = 0
    issues: List[Issue] = field(default_factory=list)
    data: Dict[str, Any] = field(default_factory=dict)


class _SEOHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title = ""
        self.in_title = False
        self.metas: List[Dict[str, str]] = []
        self.links: List[Dict[str, str]] = []
        self.headings: Dict[str, List[str]] = {f"h{i}": [] for i in range(1, 7)}
        self.current_h: Optional[str] = None
        self.h_buf = ""
        self.images: List[Dict[str, str]] = []
        self.scripts_ld: List[str] = []
        self.in_ld = False
        self.ld_buf = ""
        self.lang = ""
        self.text_bits: List[str] = []
        self.capture_text = True

    def handle_starttag(self, tag, attrs):
        a = {k.lower(): (v or "") for k, v in attrs}
        if tag == "html":
            self.lang = a.get("lang", "")
        if tag == "title":
            self.in_title = True
            self.title = ""
        if tag == "meta":
            self.metas.append(a)
        if tag == "link":
            self.links.append(a)
        if tag in self.headings:
            self.current_h = tag
            self.h_buf = ""
        if tag == "img":
            self.images.append(
                {
                    "src": a.get("src", ""),
                    "alt": a.get("alt", None) if "alt" in a else "",
                    "has_alt_attr": "alt" in a,
                    "loading": a.get("loading", ""),
                    "width": a.get("width", ""),
                    "height": a.get("height", ""),
                }
            )
        if tag == "script" and "ld+json" in a.get("type", "").lower():
            self.in_ld = True
            self.ld_buf = ""

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False
        if tag in self.headings and self.current_h == tag:
            self.headings[tag].append(re.sub(r"\s+", " ", self.h_buf).strip())
            self.current_h = None
            self.h_buf = ""
        if tag == "script" and self.in_ld:
            self.scripts_ld.append(self.ld_buf.strip())
            self.in_ld = False
            self.ld_buf = ""

    def handle_data(self, data):
        if self.in_title:
            self.title += data
        if self.current_h:
            self.h_buf += data
        if self.in_ld:
            self.ld_buf += data
        if self.capture_text and data and data.strip():
            self.text_bits.append(data.strip())


def _meta_content(metas: List[Dict[str, str]], *, name: str = "", prop: str = "") -> str:
    for m in metas:
        if name and m.get("name", "").lower() == name.lower():
            return m.get("content", "").strip()
        if prop and m.get("property", "").lower() == prop.lower():
            return m.get("content", "").strip()
    return ""


def _link_href(links: List[Dict[str, str]], rel: str) -> str:
    for l in links:
        rels = {x.strip().lower() for x in l.get("rel", "").split()}
        if rel.lower() in rels:
            return l.get("href", "").strip()
    return ""


def audit_html(html: str, url_or_path: str, target_keywords: Optional[List[str]] = None) -> PageAudit:
    p = _SEOHTMLParser()
    try:
        p.feed(html)
    except Exception as e:
        return PageAudit(url_or_path=url_or_path, score=0, issues=[Issue("critical", "parse_error", str(e))])

    title = re.sub(r"\s+", " ", p.title).strip()
    desc = _meta_content(p.metas, name="description")
    robots = _meta_content(p.metas, name="robots")
    viewport = _meta_content(p.metas, name="viewport")
    canonical = _link_href(p.links, "canonical")
    og_title = _meta_content(p.metas, prop="og:title")
    og_desc = _meta_content(p.metas, prop="og:description")
    og_image = _meta_content(p.metas, prop="og:image")
    og_url = _meta_content(p.metas, prop="og:url")
    tw_card = _meta_content(p.metas, name="twitter:card")
    h1s = p.headings["h1"]
    text = " ".join(p.text_bits)
    words = re.findall(r"[A-Za-z\u0600-\u06FF]{2,}", text)
    word_count = len(words)

    issues: List[Issue] = []
    score = 100

    def add(sev: str, code: str, msg: str, hint: str = "", penalty: int = 5):
        nonlocal score
        issues.append(Issue(sev, code, msg, hint))
        score -= penalty

    if not title:
        add("critical", "title_missing", "Missing <title>", "Add a unique title 50-60 chars with primary keyword.", 20)
    else:
        if len(title) < 30:
            add("medium", "title_short", f"Title short ({len(title)} chars)", "Aim 50-60 characters.", 5)
        if len(title) > 65:
            add("medium", "title_long", f"Title long ({len(title)} chars)", "Keep under ~60 characters.", 4)
    if not desc:
        add("critical", "meta_desc_missing", "Missing meta description", "Add 120-160 char description with CTA.", 15)
    else:
        if len(desc) < 70:
            add("medium", "meta_desc_short", f"Meta description short ({len(desc)})", "Expand to 120-160 chars.", 4)
        if len(desc) > 170:
            add("low", "meta_desc_long", f"Meta description long ({len(desc)})", "Trim to ~155 chars.", 2)
    if not viewport:
        add("high", "viewport_missing", "Missing viewport meta", "Add mobile viewport meta.", 10)
    if not p.lang:
        add("high", "lang_missing", "Missing html lang", "Set lang='en' or appropriate code.", 8)
    if len(h1s) == 0:
        add("critical", "h1_missing", "No H1 found", "Add exactly one clear H1.", 15)
    elif len(h1s) > 1:
        add("medium", "h1_multiple", f"Multiple H1s ({len(h1s)})", "Use a single H1.", 6)
    if not canonical and not url_or_path.endswith((".md",)):
        add("medium", "canonical_missing", "No canonical link", "Add <link rel=canonical>.", 5)
    if not og_title or not og_desc or not og_image:
        add("medium", "og_incomplete", "Open Graph incomplete", "Set og:title, og:description, og:image.", 6)
    if not tw_card:
        add("low", "twitter_card_missing", "No twitter:card", "Add twitter:card=summary_large_image.", 2)
    if not p.scripts_ld:
        add("medium", "schema_missing", "No JSON-LD schema", "Add ProfessionalService/LocalBusiness/FAQPage as relevant.", 8)

    missing_alt = [img for img in p.images if not img.get("has_alt_attr")]
    empty_alt = [img for img in p.images if img.get("has_alt_attr") and not (img.get("alt") or "").strip()]
    if missing_alt:
        add("high", "img_alt_missing", f"{len(missing_alt)} images missing alt attribute", "Add descriptive alt text.", min(12, 3 * len(missing_alt)))
    if empty_alt:
        add("medium", "img_alt_empty", f"{len(empty_alt)} images have empty alt", "Use meaningful alt (or empty only if decorative).", 4)

    if word_count < 150 and "/onboard" not in url_or_path and "miner" not in url_or_path:
        add("medium", "thin_content", f"Thin visible text (~{word_count} words)", "Add useful copy for search intent.", 6)

    if target_keywords:
        blob = f"{title} {desc} {' '.join(h1s)} {text}".lower()
        missing_kw = [k for k in target_keywords if k.lower() not in blob]
        if missing_kw:
            add(
                "medium",
                "keywords_missing",
                f"Missing target keywords: {', '.join(missing_kw[:6])}",
                "Naturally include UAE/clinic keywords in title, H1, and body.",
                min(12, 2 * len(missing_kw)),
            )

    # internal noindex warning for public pages
    if robots and "noindex" in robots.lower() and any(x in url_or_path for x in ["hire", "index.html", "/"]):
        add("high", "noindex_public", "Public page has noindex", "Remove noindex from public acquisition pages.", 12)

    score = max(0, min(100, score))
    data = {
        "title": title,
        "title_len": len(title),
        "description": desc,
        "description_len": len(desc),
        "robots": robots,
        "lang": p.lang,
        "canonical": canonical,
        "h1": h1s,
        "h2_count": len(p.headings["h2"]),
        "og": {"title": og_title, "description": og_desc, "image": og_image, "url": og_url},
        "twitter_card": tw_card,
        "json_ld_blocks": len(p.scripts_ld),
        "images": len(p.images),
        "images_missing_alt": len(missing_alt),
        "word_count": word_count,
    }
    return PageAudit(url_or_path=url_or_path, score=score, issues=issues, data=data)


def audit_local_file(path: Path, public_path: str = "", keywords: Optional[List[str]] = None) -> PageAudit:
    html = path.read_text(encoding="utf-8", errors="ignore")
    return audit_html(html, public_path or str(path), keywords)


def audit_url(url: str, keywords: Optional[List[str]] = None, timeout: int = 25) -> PageAudit:
    import urllib.request

    req = urllib.request.Request(url, headers={"User-Agent": "LeadFlow-SEO-Agent/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            html = resp.read().decode("utf-8", errors="ignore")
            return audit_html(html, url, keywords)
    except Exception as e:
        return PageAudit(url_or_path=url, score=0, issues=[Issue("critical", "fetch_error", str(e))])


def to_dict(audit: PageAudit) -> Dict[str, Any]:
    d = asdict(audit)
    return d
