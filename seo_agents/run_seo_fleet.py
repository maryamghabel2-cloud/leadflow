#!/usr/bin/env python3
"""
LeadFlow SEO Fleet Orchestrator
Runs technical + local UAE SEO agents, writes reports, applies safe on-page fixes.
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Any

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))

from technical_seo_agent import audit_local_file, audit_url, to_dict as page_to_dict  # noqa: E402
from local_uae_seo_agent import analyze_local_text, to_dict as local_to_dict  # noqa: E402
from content_seo_agent import write_markdown_articles  # noqa: E402


PUBLIC_PAGES = [
    # path relative to root, public URL path, keywords
    ("index.html", "/", ["Dubai", "UAE", "clinic website", "dental", "medspa"]),
    ("hire.html", "/hire", ["Dubai", "UAE", "clinic website", "dental", "medspa", "Arabic", "English", "USDT", "Abu Dhabi"]),
    ("onboard.html", "/onboard", ["USDT", "Dubai", "clinic"]),
    ("generated_sites/live_demos/marina_pearl_dental_live.html", "/live_demos/marina_pearl_dental_live.html", ["Dubai", "dental", "appointment", "book"]),
]


def apply_safe_fixes(root: Path) -> List[str]:
    """Best-effort automatic fixes for common issues on public pages."""
    actions: List[str] = []

    # index.html: ensure twitter card + stronger canonical already maybe present
    index = root / "index.html"
    if index.exists():
        html = index.read_text(encoding="utf-8", errors="ignore")
        original = html
        if 'name="twitter:card"' not in html and "twitter:card" not in html:
            html = html.replace(
                "</title>",
                '</title>\n    <meta name="twitter:card" content="summary_large_image">',
                1,
            )
            actions.append("index.html: added twitter:card")
        if "application/ld+json" not in html:
            schema = '''
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "ProfessionalService",
      "name": "LeadFlow.AI",
      "url": "https://leadflow-ai-1vip.onrender.com/",
      "description": "Clinic and medspa website design for Dubai and the UAE. English + Arabic ready. USDT packages.",
      "areaServed": ["Dubai", "UAE", "Abu Dhabi", "Sharjah"],
      "serviceType": ["Dental website design", "Medspa website design", "Clinic website design"]
    }
    </script>'''
            html = html.replace("</head>", schema + "\n</head>", 1)
            actions.append("index.html: added ProfessionalService JSON-LD")
        if 'rel="canonical"' not in html and "rel='canonical'" not in html:
            html = html.replace(
                "</title>",
                '</title>\n    <link rel="canonical" href="https://leadflow-ai-1vip.onrender.com/">',
                1,
            )
            actions.append("index.html: added canonical")
        # ensure H1 exists - hard to inject safely; skip if present
        if html != original:
            index.write_text(html, encoding="utf-8")

    hire = root / "hire.html"
    if hire.exists():
        html = hire.read_text(encoding="utf-8", errors="ignore")
        original = html
        if 'name="twitter:card"' not in html:
            html = html.replace(
                '<meta name="robots" content="index,follow">',
                '<meta name="robots" content="index,follow">\n  <meta name="twitter:card" content="summary_large_image">\n  <meta name="twitter:title" content="Clinic Website Design in Dubai | LeadFlow.AI">\n  <meta name="twitter:description" content="EN+AR clinic websites for Dubai & UAE. Free live preview. USDT checkout.">',
                1,
            )
            actions.append("hire.html: added twitter tags")
        if html != original:
            hire.write_text(html, encoding="utf-8")

    # onboard basic SEO if thin
    onboard = root / "onboard.html"
    if onboard.exists():
        html = onboard.read_text(encoding="utf-8", errors="ignore")
        original = html
        if "<title>" in html and "Dubai" not in html[html.find("<title>"):html.find("</title>") + 8]:
            html = html.replace(
                html[html.find("<title>"): html.find("</title>") + 8],
                "<title>LeadFlow Checkout | Dubai Clinic Website Packages (USDT)</title>",
                1,
            )
            actions.append("onboard.html: retitled for Dubai packages")
        if 'name="description"' not in html:
            html = html.replace(
                "</title>",
                '</title>\n    <meta name="description" content="Checkout LeadFlow clinic website packages for Dubai & UAE. Launch $799, Growth $1499, Authority $2999 USDT.">\n    <meta name="robots" content="index,follow">\n    <link rel="canonical" href="https://leadflow-ai-1vip.onrender.com/onboard">',
                1,
            )
            actions.append("onboard.html: added meta description + canonical")
        if 'lang="' not in html[:300]:
            html = html.replace("<html", '<html lang="en"', 1)
            actions.append("onboard.html: set html lang")
        if html != original:
            onboard.write_text(html, encoding="utf-8")

    # marina demo: ensure canonical-ish and unique alts already; add robots index if missing
    marina = root / "generated_sites/live_demos/marina_pearl_dental_live.html"
    if marina.exists():
        html = marina.read_text(encoding="utf-8", errors="ignore")
        original = html
        if 'rel="canonical"' not in html:
            html = html.replace(
                "</title>",
                '</title>\n<link rel="canonical" href="https://leadflow-ai-1vip.onrender.com/live_demos/marina_pearl_dental_live.html">',
                1,
            )
            actions.append("marina demo: added canonical")
        if 'name="robots"' not in html:
            html = html.replace(
                "</title>",
                '</title>\n<meta name="robots" content="index,follow">',
                1,
            )
            actions.append("marina demo: added robots index,follow")
        if html != original:
            marina.write_text(html, encoding="utf-8")

    return actions


def run(base_url: str = "", local_only: bool = True) -> Dict[str, Any]:
    root = ROOT
    report_dir = root / "seo_reports"
    report_dir.mkdir(parents=True, exist_ok=True)

    # Apply safe fixes first so re-audit benefits
    fixes = apply_safe_fixes(root)

    page_results: List[Dict[str, Any]] = []
    local_results: List[Dict[str, Any]] = []

    for file_rel, public_path, kws in PUBLIC_PAGES:
        path = root / file_rel
        if not path.exists():
            continue
        if local_only or not base_url:
            audit = audit_local_file(path, public_path=public_path, keywords=kws)
        else:
            audit = audit_url(base_url.rstrip("/") + public_path, keywords=kws)
            # also keep local fallback if fetch fails hard
            if audit.score == 0 and any(i.code == "fetch_error" for i in audit.issues):
                audit = audit_local_file(path, public_path=public_path, keywords=kws)
        page_results.append(page_to_dict(audit))

        text = path.read_text(encoding="utf-8", errors="ignore")
        local_results.append(local_to_dict(analyze_local_text(public_path, text, kws)))

    articles = write_markdown_articles(root / "content" / "seo")

    # Expand sitemap with content pages (as markdown paths not public; skip)
    # Write agent playbooks if missing
    agents_dir = root / "agents"
    agents_dir.mkdir(exist_ok=True)
    seo_agent_md = agents_dir / "07_seo_fleet_agent.md"
    if not seo_agent_md.exists() or True:
        seo_agent_md.write_text(
            """# Agent 07 — SEO Fleet Agent

## Mission
Improve LeadFlow organic discovery in Dubai/UAE for clinic website demand.

## Tools in repo
- `seo_agents/run_seo_fleet.py`
- `seo_agents/technical_seo_agent.py`
- `seo_agents/local_uae_seo_agent.py`
- `seo_agents/content_seo_agent.py`

## Weekly loop
1. Run fleet: `python3 seo_agents/run_seo_fleet.py --local`
2. Read `seo_reports/latest_seo_report.md`
3. Ship fixes for critical/high issues
4. Publish/refresh one content brief from `content/seo/`
5. Submit/refresh sitemap in Google Search Console
6. Outreach still required until rankings compound

## Public pages to protect
- `/` and `/hire` (acquisition)
- `/onboard` (conversion)
- flagship demos

## Do not index
- `/first-customer`, `/go`, `/agency`, `/docs`
""",
            encoding="utf-8",
        )

    avg = int(round(sum(p["score"] for p in page_results) / max(1, len(page_results))))
    critical = sum(1 for p in page_results for i in p["issues"] if i["severity"] == "critical")
    high = sum(1 for p in page_results for i in p["issues"] if i["severity"] == "high")

    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "average_score": avg,
        "critical_issues": critical,
        "high_issues": high,
        "fixes_applied": fixes,
        "pages": page_results,
        "local_uae": local_results,
        "content_briefs": [str(a.relative_to(root)) for a in articles],
        "sources_inspired_by": [
            "https://github.com/JeffLi1993/seo-audit-skill",
            "https://github.com/zurd46/AISeoAgent",
            "https://github.com/Bhanunamikaze/Agentic-SEO-Skill",
            "https://github.com/AgriciDaniel/claude-seo",
        ],
    }

    ts = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    json_path = report_dir / f"seo_report_{ts}.json"
    latest_json = report_dir / "latest_seo_report.json"
    md_path = report_dir / f"seo_report_{ts}.md"
    latest_md = report_dir / "latest_seo_report.md"

    json_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    latest_json.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")

    md = [
        f"# LeadFlow SEO Fleet Report",
        f"",
        f"Generated: {payload['generated_at']}",
        f"",
        f"## Summary",
        f"- Average score: **{avg}/100**",
        f"- Critical issues: **{critical}**",
        f"- High issues: **{high}**",
        f"",
        f"## Fixes applied this run",
    ]
    if fixes:
        md += [f"- {f}" for f in fixes]
    else:
        md.append("- None needed / already present")

    md += ["", "## Page audits"]
    for p in page_results:
        md.append(f"### `{p['url_or_path']}` — score {p['score']}/100")
        if not p["issues"]:
            md.append("- No issues 🎉")
        else:
            for i in p["issues"]:
                md.append(f"- **{i['severity'].upper()}** `{i['code']}`: {i['message']}")
                if i.get("fix_hint"):
                    md.append(f"  - Fix: {i['fix_hint']}")
        md.append("")

    md += ["## Local UAE keyword coverage"]
    for loc in local_results:
        md.append(f"### `{loc['target']}` — {loc['score']}/100")
        md.append(f"- Found: {', '.join(loc['found']) or '—'}")
        md.append(f"- Missing: {', '.join(loc['missing']) or '—'}")
        for r in loc["recommendations"]:
            md.append(f"- Rec: {r}")
        md.append("")

    md += [
        "## Content briefs generated",
        *[f"- `{c}`" for c in payload["content_briefs"]],
        "",
        "## Inspired by open-source SEO agents",
        *[f"- {s}" for s in payload["sources_inspired_by"]],
        "",
        "## Next actions",
        "1. Push changes and confirm `/hire`, `/robots.txt`, `/sitemap.xml` live",
        "2. Submit sitemap in Google Search Console",
        "3. Expand one markdown brief into a public HTML article when ready",
        "4. Keep outbound outreach while SEO compounds",
        "",
    ]
    md_text = "\n".join(md)
    md_path.write_text(md_text, encoding="utf-8")
    latest_md.write_text(md_text, encoding="utf-8")

    print(md_text)
    print(f"\nWrote {latest_md}")
    return payload


def main():
    parser = argparse.ArgumentParser(description="Run LeadFlow SEO agent fleet")
    parser.add_argument("--base-url", default="", help="Live base URL to fetch pages")
    parser.add_argument("--local", action="store_true", help="Audit local files only")
    args = parser.parse_args()
    local_only = args.local or not args.base_url
    run(base_url=args.base_url, local_only=local_only)


if __name__ == "__main__":
    main()
