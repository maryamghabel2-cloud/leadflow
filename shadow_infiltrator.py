"""
LeadFlow.AI - Shadow Infiltrator (Editorial Monochrome Generator)
Generates premium local-business websites in the same Swiss/editorial design language
as the LeadFlow flagship portal — zero neon cyan / cyber glow.
"""

from __future__ import annotations

import os
from typing import Dict, Any
from cloud_deployer import CloudDeploymentEngine


class ShadowInfiltrator:
    def __init__(self, output_dir: str = None):
        if output_dir is None:
            output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "generated_sites")
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)
        self.deployer = CloudDeploymentEngine(base_output_dir=self.output_dir)

    def generate_luxury_site(
        self,
        business_name: str,
        category: str,
        city: str,
        phone: str = "+1 (555) 019-2831",
        custom_domain: str = None,
    ) -> Dict[str, Any]:
        slug = "".join(c if c.isalnum() else "_" for c in business_name.lower()).strip("_")
        filename = f"{slug}_luxury.html"
        filepath = os.path.join(self.output_dir, filename)
        if custom_domain is None:
            custom_domain = f"{slug}.com"

        cat_lower = (category or "").lower()
        if any(w in cat_lower for w in ["dental", "clinic", "doctor", "health", "medical", "vet", "veterinary"]):
            html_content = self._generate_medical_site(business_name, category, city, phone)
            paradigm = "Medical & Wellness (Editorial Clinical)"
        elif any(w in cat_lower for w in ["restaurant", "dining", "food", "lounge", "bistro", "cafe"]):
            html_content = self._generate_dining_site(business_name, category, city, phone)
            paradigm = "Fine Dining (Editorial Hospitality)"
        elif any(w in cat_lower for w in ["law", "legal", "attorney", "lawyer", "justice"]):
            html_content = self._generate_legal_site(business_name, category, city, phone)
            paradigm = "Law Firm (Editorial Counsel)"
        elif any(w in cat_lower for w in ["estate", "realty", "property", "architecture", "builder"]):
            html_content = self._generate_realty_site(business_name, category, city, phone)
            paradigm = "Real Estate (Editorial Property)"
        else:
            html_content = self._generate_universal_dynamic_site(business_name, category, city, phone)
            paradigm = f"Universal Editorial ({(category or 'Services').title()})"

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html_content.strip())

        demo_res = self.deployer.provision_live_demo(business_name, html_content, paradigm)
        pkg_res = self.deployer.create_client_handover_package(business_name, html_content, custom_domain)

        return {
            "status": "success",
            "business_name": business_name,
            "category": category,
            "city": city,
            "phone": phone,
            "industry_paradigm_applied": paradigm,
            "generated_filename": filename,
            "generated_filepath": filepath,
            "live_cloud_demo_url": demo_res["live_cloud_url"],
            "client_handover_zip": pkg_res["handover_zip_path"],
            "custom_domain_configured": custom_domain,
            "upsell_pitch": (
                f"Hi {business_name} team,\n\n"
                f"We noticed your establishment in {city} has a strong local reputation but currently lacks a polished official website.\n\n"
                f"Our team prepared a free live preview tailored for your profession ({paradigm}):\n"
                f"LIVE DEMO: {demo_res['live_cloud_url']}\n\n"
                f"If you love it, you can take ownership and receive the full deployment ZIP for your domain `{custom_domain}`.\n"
                f"Happy to adjust services, photos, or colors on request."
            ),
        }

    def _shell(
        self,
        name: str,
        city: str,
        phone: str,
        title: str,
        kicker: str,
        headline: str,
        lead: str,
        cta: str,
        cards: list,
        tool_title: str,
        tool_body: str,
        tool_js: str,
        tool_html: str,
        modal_title: str,
    ) -> str:
        cards_html = ""
        for i, (t, d) in enumerate(cards, 1):
            cards_html += f"""
            <div class="card">
                <div class="card-kicker">0{i}</div>
                <h3>{t}</h3>
                <p>{d}</p>
            </div>"""

        return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@500;700;800&family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap');
        :root {{
            --bg: #FBFBF9; --stone: #F2EFE9; --card: #FFFFFF; --charcoal: #18181B;
            --slate: #475569; --muted: #78716C; --champagne: #B8860B; --border: #E5E0D8;
            --font-serif: 'Cinzel', serif; --font-sans: 'Plus Jakarta Sans', sans-serif; --font-mono: 'JetBrains Mono', monospace;
        }}
        * {{ margin: 0; padding: 0; box-sizing: border-box; font-family: var(--font-sans); }}
        body {{ background: var(--bg); color: var(--charcoal); line-height: 1.75; border-top: 4px solid var(--charcoal); }}
        header {{
            display: flex; justify-content: space-between; align-items: center; gap: 16px;
            padding: 22px 48px; border-bottom: 1px solid var(--border); background: rgba(251,251,249,0.96);
            position: sticky; top: 0; z-index: 50;
        }}
        @media (max-width: 720px) {{ header {{ padding: 16px 18px; flex-direction: column; }} }}
        .brand {{ display: flex; align-items: center; gap: 12px; text-decoration: none; color: inherit; }}
        .mark {{ width: 34px; height: 34px; background: var(--charcoal); color: #fff; display: flex; align-items: center; justify-content: center; font-family: var(--font-serif); font-weight: 700; }}
        .brand-text {{ font-family: var(--font-serif); letter-spacing: 3px; font-weight: 800; font-size: 16px; }}
        .btn {{
            border: 1px solid var(--charcoal); background: var(--charcoal); color: #fff;
            padding: 12px 20px; font-size: 12px; font-weight: 700; letter-spacing: 1.5px;
            text-transform: uppercase; cursor: pointer; text-decoration: none; display: inline-flex;
        }}
        .btn:hover {{ background: var(--champagne); color: #000; }}
        .btn-ghost {{ background: transparent; color: var(--charcoal); }}
        .btn-ghost:hover {{ background: var(--stone); color: var(--charcoal); }}
        .hero {{
            max-width: 1180px; margin: 0 auto; padding: 72px 24px 64px;
            display: grid; grid-template-columns: 1.2fr 1fr; gap: 40px; align-items: center;
            border-bottom: 1px solid var(--border);
        }}
        @media (max-width: 900px) {{ .hero {{ grid-template-columns: 1fr; padding: 40px 20px; }} }}
        .kicker {{
            font-family: var(--font-mono); font-size: 11px; letter-spacing: 2.5px; color: var(--champagne);
            text-transform: uppercase; font-weight: 700; margin-bottom: 14px;
        }}
        h1 {{ font-size: 44px; line-height: 1.15; font-weight: 800; letter-spacing: -0.5px; margin-bottom: 16px; }}
        @media (max-width: 640px) {{ h1 {{ font-size: 32px; }} }}
        h1 em {{ font-family: var(--font-serif); font-style: italic; font-weight: 700; color: #0F172A; }}
        .lead {{ color: var(--slate); font-size: 16px; max-width: 560px; margin-bottom: 28px; }}
        .actions {{ display: flex; gap: 12px; flex-wrap: wrap; }}
        .panel {{
            background: var(--stone); border: 1px solid var(--border); padding: 28px;
        }}
        .panel h3 {{ font-family: var(--font-serif); font-size: 20px; margin-bottom: 8px; }}
        .panel p {{ color: var(--slate); font-size: 14px; margin-bottom: 18px; }}
        .section {{ max-width: 1180px; margin: 0 auto; padding: 64px 24px; }}
        .section h2 {{ font-size: 30px; font-weight: 800; margin-bottom: 8px; }}
        .section .sub {{ color: var(--slate); margin-bottom: 28px; }}
        .grid {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 18px; }}
        @media (max-width: 900px) {{ .grid {{ grid-template-columns: 1fr; }} }}
        .card {{ background: #fff; border: 1px solid var(--border); padding: 24px; }}
        .card-kicker {{ font-family: var(--font-mono); font-size: 11px; color: var(--muted); letter-spacing: 1px; margin-bottom: 10px; }}
        .card h3 {{ font-size: 18px; margin-bottom: 8px; }}
        .card p {{ color: var(--slate); font-size: 14px; }}
        .tool {{
            max-width: 900px; margin: 0 auto; background: #fff; border: 1px solid var(--border);
            padding: 36px; text-align: center;
        }}
        .tool .kicker {{ margin-bottom: 10px; }}
        .tool h2 {{ font-size: 28px; margin-bottom: 10px; }}
        .tool p {{ color: var(--slate); margin-bottom: 18px; }}
        .tool input[type=range] {{ width: min(100%, 520px); accent-color: var(--charcoal); margin: 14px 0 20px; }}
        .tool-val {{ font-family: var(--font-serif); font-size: 36px; font-weight: 700; margin: 8px 0 6px; }}
        footer {{
            border-top: 1px solid var(--border); padding: 40px 24px; text-align: center; color: var(--muted); font-size: 13px;
            background: #fff;
        }}
        footer strong {{ color: var(--charcoal); }}
        .modal-bg {{
            display: none; position: fixed; inset: 0; background: rgba(24,24,27,0.45);
            align-items: center; justify-content: center; padding: 18px; z-index: 100;
        }}
        .modal-bg.open {{ display: flex; }}
        .modal {{ width: min(480px, 100%); background: #fff; border: 1px solid var(--border); padding: 28px; position: relative; }}
        .modal h3 {{ font-family: var(--font-serif); font-size: 22px; margin-bottom: 8px; }}
        .modal p {{ color: var(--slate); font-size: 14px; margin-bottom: 16px; }}
        .modal input, .modal select {{
            width: 100%; border: 1px solid var(--border); background: var(--bg); padding: 12px 14px;
            margin-bottom: 12px; font-size: 14px; outline: none;
        }}
        .modal input:focus, .modal select:focus {{ border-color: var(--charcoal); background: #fff; }}
        .close {{ position: absolute; top: 12px; right: 14px; border: 0; background: transparent; font-size: 22px; cursor: pointer; color: var(--muted); }}
    </style>
</head>
<body>
    <header>
        <a class="brand" href="#">
            <div class="mark">L</div>
            <div class="brand-text">{name[:18].upper()}</div>
        </a>
        <button class="btn" onclick="openModal()">{cta}</button>
    </header>

    <section class="hero">
        <div>
            <div class="kicker">{kicker} · {city}</div>
            <h1>{headline}</h1>
            <p class="lead">{lead}</p>
            <div class="actions">
                <button class="btn" onclick="openModal()">{cta}</button>
                <a class="btn btn-ghost" href="#services">View services</a>
            </div>
        </div>
        <div class="panel">
            <div class="kicker">At a glance</div>
            <h3>{name}</h3>
            <p>Premium local presence for clients in {city}. Built as a clean editorial website — easy to read, easy to book, easy to trust.</p>
            <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;">
                <div style="background:#fff;border:1px solid var(--border);padding:14px;">
                    <div style="font-family:var(--font-serif);font-size:24px;font-weight:700;">4.9</div>
                    <div style="font-size:12px;color:var(--muted);text-transform:uppercase;letter-spacing:1px;">Client rating</div>
                </div>
                <div style="background:#fff;border:1px solid var(--border);padding:14px;">
                    <div style="font-family:var(--font-serif);font-size:24px;font-weight:700;">24h</div>
                    <div style="font-size:12px;color:var(--muted);text-transform:uppercase;letter-spacing:1px;">Response goal</div>
                </div>
            </div>
        </div>
    </section>

    <section class="section" id="services">
        <h2>What we offer</h2>
        <p class="sub">Clear services presented with editorial restraint — no neon chrome, no visual noise.</p>
        <div class="grid">{cards_html}
        </div>
    </section>

    <section class="section">
        <div class="tool">
            <div class="kicker">Interactive preview</div>
            <h2>{tool_title}</h2>
            <p>{tool_body}</p>
            {tool_html}
            <div style="margin-top:18px;">
                <button class="btn" onclick="openModal()">Continue with {name}</button>
            </div>
        </div>
    </section>

    <footer>
        <div style="font-family:var(--font-serif);font-size:20px;color:var(--charcoal);margin-bottom:8px;">{name}</div>
        <div>{city} · Direct line: <strong>{phone}</strong></div>
        <div style="margin-top:10px;">Preview site prepared with LeadFlow editorial engine</div>
    </footer>

    <div class="modal-bg" id="modal">
        <div class="modal">
            <button class="close" onclick="closeModal()">×</button>
            <h3>{modal_title}</h3>
            <p>Share your details and the {name} team will follow up.</p>
            <form onsubmit="handleBooking(event)">
                <input type="text" placeholder="Full name *" required>
                <input type="tel" placeholder="Phone / WhatsApp *" required>
                <input type="email" placeholder="Email (optional)">
                <button class="btn" style="width:100%;justify-content:center;" type="submit">Submit request</button>
            </form>
        </div>
    </div>

    <script>
        function openModal() {{ document.getElementById('modal').classList.add('open'); }}
        function closeModal() {{ document.getElementById('modal').classList.remove('open'); }}
        function handleBooking(e) {{
            e.preventDefault(); closeModal();
            alert('Thank you. Your request for {name} has been recorded.');
        }}
        {tool_js}
    </script>
</body>
</html>"""

    def _generate_medical_site(self, name: str, cat: str, city: str, phone: str) -> str:
        return self._shell(
            name=name,
            city=city,
            phone=phone,
            title=f"{name} · Medical & Dental · {city}",
            kicker="Clinical practice",
            headline="Calm, precise care<br>for modern patients",
            lead=f"{name} brings clinic-grade expertise and a composed patient experience to {city} — from first consult to follow-up.",
            cta="Book consultation",
            cards=[
                ("Diagnostics", "Clear assessments and treatment planning without rushed appointments."),
                ("Restorative care", "Durable, natural-looking results designed around your comfort."),
                ("Prevention", "Maintenance programs that keep outcomes stable over time."),
            ],
            tool_title="Treatment brightness preview",
            tool_body="Slide to preview the kind of whitening outcome patients often aim for in a single visit package.",
            tool_html='<div class="tool-val" id="tool-val">70% brighter</div><input type="range" min="10" max="100" value="70" oninput="updateTool(this.value)">',
            tool_js="function updateTool(v){ document.getElementById('tool-val').innerText = v + '% brighter'; }",
            modal_title="Request a consultation",
        )

    def _generate_dining_site(self, name: str, cat: str, city: str, phone: str) -> str:
        return self._shell(
            name=name,
            city=city,
            phone=phone,
            title=f"{name} · Dining · {city}",
            kicker="Hospitality",
            headline="An evening shaped<br>by craft and calm",
            lead=f"{name} is a refined dining room in {city} — seasonal plates, considered service, and reservations that feel effortless.",
            cta="Reserve a table",
            cards=[
                ("Seasonal menu", "A rotating selection built around peak ingredients and restrained plating."),
                ("Wine & pairing", "Curated bottles chosen to support the kitchen, not overshadow it."),
                ("Private dining", "Quiet rooms for celebrations and client dinners."),
            ],
            tool_title="Private dining estimator",
            tool_body="Adjust guest count to estimate a tasting-menu package for your group.",
            tool_html='<div class="tool-val" id="tool-val">12 guests · est. $4,560</div><input type="range" min="2" max="40" value="12" oninput="updateTool(this.value)">',
            tool_js="function updateTool(v){ document.getElementById('tool-val').innerText = v + ' guests · est. $' + (v*380).toLocaleString(); }",
            modal_title="Reservation request",
        )

    def _generate_legal_site(self, name: str, cat: str, city: str, phone: str) -> str:
        return self._shell(
            name=name,
            city=city,
            phone=phone,
            title=f"{name} · Legal Counsel · {city}",
            kicker="Counsel",
            headline="Clear advocacy.<br>Measured strategy.",
            lead=f"{name} represents clients in {city} with disciplined preparation, direct communication, and discreet handling of complex matters.",
            cta="Request consultation",
            cards=[
                ("Dispute resolution", "Commercial and civil matters handled with structured case planning."),
                ("Advisory", "Contracts, governance, and risk guidance before conflict escalates."),
                ("Confidential matters", "Private engagement model for executives and family offices."),
            ],
            tool_title="Case scale indicator",
            tool_body="Slide to express approximate dispute scale for a confidential intake conversation.",
            tool_html='<div class="tool-val" id="tool-val">$1,500,000 matter scale</div><input type="range" min="100000" max="10000000" step="100000" value="1500000" oninput="updateTool(this.value)">',
            tool_js="function updateTool(v){ document.getElementById('tool-val').innerText = '$' + parseInt(v).toLocaleString() + ' matter scale'; }",
            modal_title="Confidential inquiry",
        )

    def _generate_realty_site(self, name: str, cat: str, city: str, phone: str) -> str:
        return self._shell(
            name=name,
            city=city,
            phone=phone,
            title=f"{name} · Property · {city}",
            kicker="Property desk",
            headline="Residences and<br>investments, curated",
            lead=f"{name} helps buyers and investors in {city} evaluate properties with calm clarity — architecture, location, and long-term yield.",
            cta="Book a showing",
            cards=[
                ("Residential search", "Private shortlists matched to lifestyle and budget."),
                ("Investment analysis", "Simple yield framing before you commit capital."),
                ("Off-market access", "Quiet introductions when discretion matters."),
            ],
            tool_title="Yield sketch",
            tool_body="Adjust assumed purchase price to sketch an annual net yield at 8.5%.",
            tool_html='<div class="tool-val" id="tool-val">$2,500,000 · ~$212,500 / yr</div><input type="range" min="500000" max="12000000" step="100000" value="2500000" oninput="updateTool(this.value)">',
            tool_js="function updateTool(v){ const y=Math.round(v*0.085); document.getElementById('tool-val').innerText = '$' + parseInt(v).toLocaleString() + ' · ~$' + y.toLocaleString() + ' / yr'; }",
            modal_title="Showing request",
        )

    def _generate_universal_dynamic_site(self, name: str, cat: str, city: str, phone: str) -> str:
        cat_title = (cat or "Professional Services").title()
        return self._shell(
            name=name,
            city=city,
            phone=phone,
            title=f"{name} · {cat_title} · {city}",
            kicker=cat_title,
            headline=f"A clearer digital<br>home for {cat_title.lower()}",
            lead=f"{name} serves clients in {city} with a focused offer, trustworthy presentation, and a booking path that feels simple.",
            cta="Get in touch",
            cards=[
                ("Signature service", f"Core {cat_title.lower()} work delivered with consistency and care."),
                ("Client experience", "Transparent communication from inquiry to completion."),
                ("Local presence", f"Built for people searching in and around {city}."),
            ],
            tool_title="Engagement scale",
            tool_body="Slide to indicate the approximate size of project you have in mind.",
            tool_html='<div class="tool-val" id="tool-val">Medium engagement</div><input type="range" min="1" max="5" value="3" oninput="updateTool(this.value)">',
            tool_js="function updateTool(v){ const m={1:'Starter',2:'Focused',3:'Medium engagement',4:'Growth',5:'Enterprise'}; document.getElementById('tool-val').innerText = m[v]||'Medium engagement'; }",
            modal_title="Contact request",
        )


if __name__ == "__main__":
    g = ShadowInfiltrator()
    print(g.generate_luxury_site("Apex Dental Lounge", "Dental Clinic", "Toronto", "+1 416 555 0199")["live_cloud_demo_url"])
