"""
LeadFlow.AI - Shadow Infiltrator
Industry-specific creative website generator.

Design principle:
- Each profession gets a DISTINCT visual system tailored to buyer psychology.
- Not a clone of the LeadFlow product UI.
- Not neon/cyber cyan glow kitsch.
"""

from __future__ import annotations

import os
from typing import Dict, Any, List, Tuple
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

        cat = (category or "").lower()
        name_l = business_name.lower()
        blob = f"{cat} {name_l}"

        if any(w in blob for w in ["dental", "clinic", "doctor", "health", "medical", "vet", "veterinary", "hospital"]):
            html_content = self._medical(business_name, category, city, phone)
            paradigm = "Healthcare · clinical calm (trust / hygiene / clarity)"
        elif any(w in blob for w in ["restaurant", "dining", "food", "lounge", "bistro", "cafe", "gourmet"]):
            html_content = self._dining(business_name, category, city, phone)
            paradigm = "Hospitality · warm nocturnal fine dining"
        elif any(w in blob for w in ["law", "legal", "attorney", "lawyer", "justice", "counsel"]):
            html_content = self._legal(business_name, category, city, phone)
            paradigm = "Legal · authoritative editorial counsel"
        elif any(w in blob for w in ["estate", "realty", "property", "architecture", "builder", "architectural"]):
            html_content = self._realty(business_name, category, city, phone)
            paradigm = "Property · architectural photography magazine"
        elif any(w in blob for w in ["gym", "fitness", "performance", "sport", "training"]):
            html_content = self._gym(business_name, category, city, phone)
            paradigm = "Fitness · bold athletic energy"
        elif any(w in blob for w in ["spa", "aesthetic", "salon", "beauty", "wellness", "sanctuary"]):
            html_content = self._spa(business_name, category, city, phone)
            paradigm = "Wellness · soft sanctuary ritual"
        elif any(w in blob for w in ["jewelry", "jewel", "watch", "diamond", "crown"]):
            html_content = self._jewelry(business_name, category, city, phone)
            paradigm = "Jewelry · high jewelry atelier"
        elif any(w in blob for w in ["wealth", "advisory", "finance", "private", "capital", "invest"]):
            html_content = self._wealth(business_name, category, city, phone)
            paradigm = "Wealth · private bank discretion"
        else:
            html_content = self._universal(business_name, category, city, phone)
            paradigm = f"Services · category-tuned studio ({(category or 'professional').title()})"

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
                f"We built a free live website preview tailored for your industry in {city}:\n"
                f"{demo_res['live_cloud_url']}\n\n"
                f"Design direction: {paradigm}.\n"
                f"If you want ownership + deployment package for `{custom_domain}`, we can transfer it after payment.\n"
                f"Happy to adjust copy, services, or colors."
            ),
        }

    # ------------------------------------------------------------------ helpers
    def _esc(self, s: str) -> str:
        return (
            (s or "")
            .replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
            .replace('"', "&quot;")
        )

    def _cards(self, items: List[Tuple[str, str]], card_class: str = "card") -> str:
        out = []
        for t, d in items:
            out.append(f'<article class="{card_class}"><h3>{self._esc(t)}</h3><p>{self._esc(d)}</p></article>')
        return "\n".join(out)

    # ================================================================== MEDICAL
    def _medical(self, name: str, cat: str, city: str, phone: str) -> str:
        n, c, p = self._esc(name), self._esc(city), self._esc(phone)
        cards = self._cards([
            ("Gentle diagnostics", "Clear explanations, digital charting, and zero-rush consults."),
            ("Restorative artistry", "Natural-looking results planned around facial harmony."),
            ("Family continuity", "Recall systems and prevention that keep care simple over years."),
        ])
        return f"""<!DOCTYPE html>
<html lang="en"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{n} · Care in {c}</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Fraunces:opsz,wght@9..144,500;9..144,700&display=swap');
:root{{--bg:#F7FBFA;--ink:#16302B;--mute:#5B726C;--line:#D7E5E1;--sea:#2F6F68;--sea-soft:#E4F3F0;--sand:#FFF9F2}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:'DM Sans',sans-serif;background:var(--bg);color:var(--ink);line-height:1.7}}
.nav{{display:flex;justify-content:space-between;align-items:center;padding:20px 7vw;background:rgba(247,251,250,.92);backdrop-filter:blur(10px);border-bottom:1px solid var(--line);position:sticky;top:0;z-index:20}}
.logo{{font-family:'Fraunces',serif;font-size:1.35rem;font-weight:700;color:var(--ink);text-decoration:none}}
.btn{{background:var(--sea);color:#fff;border:0;padding:12px 20px;border-radius:999px;font-weight:700;cursor:pointer;text-decoration:none;display:inline-block}}
.btn:hover{{filter:brightness(1.05)}}
.btn-soft{{background:var(--sea-soft);color:var(--sea)}}
.hero{{display:grid;grid-template-columns:1.15fr .85fr;gap:40px;padding:70px 7vw;align-items:center}}
@media(max-width:900px){{.hero{{grid-template-columns:1fr;padding:40px 6vw}}}}
.pill{{display:inline-block;background:var(--sea-soft);color:var(--sea);padding:6px 12px;border-radius:999px;font-size:.78rem;font-weight:700;letter-spacing:.04em;text-transform:uppercase;margin-bottom:14px}}
h1{{font-family:'Fraunces',serif;font-size:clamp(2.2rem,4vw,3.4rem);line-height:1.12;margin-bottom:16px;font-weight:700}}
.lead{{color:var(--mute);font-size:1.08rem;max-width:34rem;margin-bottom:28px}}
.actions{{display:flex;gap:12px;flex-wrap:wrap}}
.side{{background:linear-gradient(160deg,var(--sand),#fff);border:1px solid var(--line);border-radius:28px;padding:28px;box-shadow:0 18px 50px rgba(22,48,43,.06)}}
.metric{{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:18px}}
.metric div{{background:#fff;border:1px solid var(--line);border-radius:18px;padding:16px}}
.metric strong{{display:block;font-family:'Fraunces',serif;font-size:1.6rem}}
.metric span{{color:var(--mute);font-size:.82rem}}
.section{{padding:20px 7vw 70px}}
.section h2{{font-family:'Fraunces',serif;font-size:2rem;margin-bottom:8px}}
.section .sub{{color:var(--mute);margin-bottom:24px}}
.grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}}
@media(max-width:900px){{.grid{{grid-template-columns:1fr}}}}
.card{{background:#fff;border:1px solid var(--line);border-radius:22px;padding:24px}}
.card h3{{font-size:1.1rem;margin-bottom:8px}}
.card p{{color:var(--mute);font-size:.95rem}}
.tool{{margin:10px 7vw 70px;background:#fff;border:1px solid var(--line);border-radius:28px;padding:36px;text-align:center}}
.tool h2{{font-family:'Fraunces',serif;margin-bottom:8px}}
.val{{font-family:'Fraunces',serif;font-size:2.2rem;color:var(--sea);margin:14px 0}}
input[type=range]{{width:min(100%,420px);accent-color:var(--sea)}}
footer{{padding:40px 7vw;border-top:1px solid var(--line);color:var(--mute);text-align:center;background:#fff}}
.modal{{display:none;position:fixed;inset:0;background:rgba(22,48,43,.45);align-items:center;justify-content:center;padding:18px;z-index:50}}
.modal.open{{display:flex}}
.modal-card{{background:#fff;border-radius:22px;padding:28px;width:min(440px,100%);position:relative}}
.modal-card input{{width:100%;margin:8px 0;padding:12px 14px;border:1px solid var(--line);border-radius:12px}}
.close{{position:absolute;right:14px;top:10px;border:0;background:none;font-size:1.4rem;cursor:pointer;color:var(--mute)}}
</style></head><body>
<nav><a class="logo" href="#">{n}</a><button class="btn" onclick="openM()">Book visit</button></nav>
<section class="hero">
  <div>
    <div class="pill">Healthcare · {c}</div>
    <h1>Care that feels calm, clear, and human</h1>
    <p class="lead">{n} is built for patients who want modern clinical standards without the clinical coldness — in the heart of {c}.</p>
    <div class="actions">
      <button class="btn" onclick="openM()">Request appointment</button>
      <a class="btn btn-soft" href="#services">Explore services</a>
    </div>
  </div>
  <aside class="side">
    <div class="pill">Patient desk</div>
    <h2 style="font-family:'Fraunces',serif;font-size:1.5rem;margin:8px 0 10px">Same-week consults</h2>
    <p style="color:var(--mute);margin-bottom:8px">Direct line: <strong style="color:var(--ink)">{p}</strong></p>
    <div class="metric">
      <div><strong>4.9</strong><span>avg. patient rating</span></div>
      <div><strong>15m</strong><span>on-time arrival goal</span></div>
    </div>
  </aside>
</section>
<section class="section" id="services">
  <h2>Services designed around comfort</h2>
  <p class="sub">Healthcare UX: soft color, high readability, obvious next step — because anxious patients scan, they don’t study.</p>
  <div class="grid">{cards}</div>
</section>
<section class="tool">
  <div class="pill">Interactive preview</div>
  <h2>Smile brightness planner</h2>
  <p style="color:var(--mute)">A simple visual for whitening conversations — not a medical claim, a conversation starter.</p>
  <div class="val" id="v">70% brighter target</div>
  <input type="range" min="20" max="100" value="70" oninput="document.getElementById('v').textContent=this.value+'% brighter target'">
  <div style="margin-top:18px"><button class="btn" onclick="openM()">Discuss this plan</button></div>
</section>
<footer><strong style="color:var(--ink);font-family:'Fraunces',serif;font-size:1.2rem">{n}</strong><br>{c} · {p}</footer>
<div class="modal" id="m"><div class="modal-card">
  <button class="close" onclick="closeM()">×</button>
  <h3 style="font-family:'Fraunces',serif;margin-bottom:8px">Request a visit</h3>
  <p style="color:var(--mute);font-size:.92rem;margin-bottom:10px">We’ll confirm availability with {n}.</p>
  <form onsubmit="event.preventDefault();closeM();alert('Request received. {n} will follow up.');">
    <input placeholder="Full name *" required>
    <input placeholder="Phone *" required>
    <input placeholder="Preferred time window">
    <button class="btn" style="width:100%;margin-top:8px">Send request</button>
  </form>
</div></div>
<script>function openM(){{document.getElementById('m').classList.add('open')}}function closeM(){{document.getElementById('m').classList.remove('open')}}</script>
</body></html>"""

    # ================================================================== DINING
    def _dining(self, name: str, cat: str, city: str, phone: str) -> str:
        n, c, p = self._esc(name), self._esc(city), self._esc(phone)
        cards = self._cards([
            ("Seasonal tasting", "A kitchen-led sequence that changes with the market, not the calendar app."),
            ("Cellar pairing", "Bottles chosen to support the plate — quiet luxury, not spectacle."),
            ("Chef’s table", "Intimate service for celebrations and client dinners."),
        ], "mc")
        return f"""<!DOCTYPE html>
<html lang="en"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{n} · {c}</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500&family=Outfit:wght@300;400;500;600&display=swap');
:root{{--bg:#14110F;--panel:#1C1816;--ink:#F4EFE6;--mute:#B7A99A;--line:rgba(244,239,230,.12);--ember:#C45C26;--gold:#D8B56A}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:'Outfit',sans-serif;background:var(--bg);color:var(--ink);line-height:1.75}}
.nav{{display:flex;justify-content:space-between;align-items:center;padding:22px 7vw;border-bottom:1px solid var(--line);position:sticky;top:0;background:rgba(20,17,15,.9);backdrop-filter:blur(12px);z-index:20}}
.logo{{font-family:'Cormorant Garamond',serif;font-size:1.7rem;letter-spacing:.04em;color:var(--ink);text-decoration:none}}
.btn{{background:var(--ember);color:#fff;border:0;padding:12px 22px;font-weight:600;letter-spacing:.06em;text-transform:uppercase;font-size:.72rem;cursor:pointer}}
.btn:hover{{background:var(--gold);color:#1a1208}}
.hero{{min-height:72vh;display:grid;place-items:center;text-align:center;padding:80px 7vw;background:
 radial-gradient(ellipse at 50% 0%, rgba(196,92,38,.22), transparent 55%),
 linear-gradient(180deg,#1a1512 0%, #14110F 70%);}}
.kicker{{color:var(--gold);letter-spacing:.28em;text-transform:uppercase;font-size:.72rem;margin-bottom:18px}}
h1{{font-family:'Cormorant Garamond',serif;font-size:clamp(2.8rem,7vw,5rem);font-weight:500;line-height:1.05;margin-bottom:18px}}
h1 em{{font-style:italic;color:var(--gold)}}
.lead{{color:var(--mute);max-width:36rem;margin:0 auto 30px;font-weight:300;font-size:1.08rem}}
.section{{padding:70px 7vw}}
.section h2{{font-family:'Cormorant Garamond',serif;font-size:2.4rem;font-weight:500;margin-bottom:10px;text-align:center}}
.sub{{color:var(--mute);text-align:center;margin-bottom:34px}}
.grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}}
@media(max-width:900px){{.grid{{grid-template-columns:1fr}}}}
.mc{{background:var(--panel);border:1px solid var(--line);padding:28px}}
.mc h3{{font-family:'Cormorant Garamond',serif;font-size:1.55rem;font-weight:500;margin-bottom:10px;color:var(--gold)}}
.mc p{{color:var(--mute);font-weight:300}}
.tool{{margin:0 7vw 70px;border:1px solid var(--line);background:var(--panel);padding:42px;text-align:center}}
.val{{font-family:'Cormorant Garamond',serif;font-size:2.6rem;color:var(--gold);margin:12px 0}}
input[type=range]{{width:min(100%,420px);accent-color:var(--ember)}}
footer{{padding:42px 7vw;border-top:1px solid var(--line);text-align:center;color:var(--mute);font-weight:300}}
.modal{{display:none;position:fixed;inset:0;background:rgba(0,0,0,.65);align-items:center;justify-content:center;padding:18px;z-index:40}}
.modal.open{{display:flex}}
.modal-card{{background:#1C1816;border:1px solid var(--line);padding:28px;width:min(440px,100%);position:relative}}
.modal-card input{{width:100%;margin:8px 0;padding:12px;background:#14110F;border:1px solid var(--line);color:var(--ink)}}
.close{{position:absolute;right:12px;top:8px;border:0;background:none;color:var(--mute);font-size:1.4rem;cursor:pointer}}
</style></head><body>
<nav><a class="logo" href="#">{n}</a><button class="btn" onclick="openM()">Reserve</button></nav>
<section class="hero">
  <div>
    <div class="kicker">Dining room · {c}</div>
    <h1>An evening of <em>fire, craft & quiet luxury</em></h1>
    <p class="lead">{n} is a warm nocturnal dining room — ember light, considered pacing, and plates built for memory, not trends.</p>
    <button class="btn" onclick="openM()">Request a table</button>
  </div>
</section>
<section class="section">
  <h2>The room, the kitchen, the cellar</h2>
  <p class="sub">Hospitality design: dark timber mood, serif romance, restrained gold — appetite without neon carnival.</p>
  <div class="grid">{cards}</div>
</section>
<section class="tool">
  <div class="kicker">Private dining</div>
  <h2 style="font-family:'Cormorant Garamond',serif;font-size:2rem;font-weight:500;margin:8px 0">Guest count estimator</h2>
  <p class="sub" style="margin-bottom:8px">Estimate a tasting package for your celebration.</p>
  <div class="val" id="v">12 guests · ~$4,560</div>
  <input type="range" min="2" max="40" value="12" oninput="document.getElementById('v').textContent=this.value+' guests · ~$'+(this.value*380).toLocaleString()">
  <div style="margin-top:18px"><button class="btn" onclick="openM()">Hold a private room</button></div>
</section>
<footer>{n} · {c} · Reservations {p}</footer>
<div class="modal" id="m"><div class="modal-card">
  <button class="close" onclick="closeM()">×</button>
  <h3 style="font-family:'Cormorant Garamond',serif;font-size:1.8rem;margin-bottom:8px">Table request</h3>
  <form onsubmit="event.preventDefault();closeM();alert('Reservation request sent to {n}.');">
    <input placeholder="Name *" required><input placeholder="Phone *" required><input placeholder="Date / time preference">
    <button class="btn" style="width:100%;margin-top:8px">Send</button>
  </form>
</div></div>
<script>function openM(){{document.getElementById('m').classList.add('open')}}function closeM(){{document.getElementById('m').classList.remove('open')}}</script>
</body></html>"""

    # ================================================================== LEGAL
    def _legal(self, name: str, cat: str, city: str, phone: str) -> str:
        n, c, p = self._esc(name), self._esc(city), self._esc(phone)
        cards = self._cards([
            ("Disputes", "Commercial and civil matters with disciplined case architecture."),
            ("Counsel", "Contracts and governance before conflict becomes expensive."),
            ("Confidential matters", "Discreet engagement for executives and family offices."),
        ])
        return f"""<!DOCTYPE html>
<html lang="en"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{n} · Counsel · {c}</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Libre+Baskerville:ital,wght@0,400;0,700;1,400&family=Source+Sans+3:wght@400;600;700&display=swap');
:root{{--bg:#F7F4EF;--ink:#1B1A17;--mute:#6B6560;--line:#E4DDD2;--navy:#1F2A44;--brass:#9C7A3C}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:'Source Sans 3',sans-serif;background:var(--bg);color:var(--ink);line-height:1.75}}
header{{display:flex;justify-content:space-between;align-items:center;padding:26px 8vw;border-bottom:1px solid var(--line);background:#FFFEFB;position:sticky;top:0;z-index:10}}
.logo{{font-family:'Libre Baskerville',serif;font-size:1.15rem;letter-spacing:.12em;text-transform:uppercase;text-decoration:none;color:var(--navy)}}
.btn{{background:var(--navy);color:#fff;border:0;padding:12px 18px;font-size:.78rem;font-weight:700;letter-spacing:.08em;text-transform:uppercase;cursor:pointer}}
.btn.gold{{background:var(--brass);color:#fff}}
.hero{{display:grid;grid-template-columns:1.2fr .8fr;gap:48px;padding:80px 8vw;align-items:start;border-bottom:1px solid var(--line);background:#FFFEFB}}
@media(max-width:900px){{.hero{{grid-template-columns:1fr;padding:40px 6vw}}}}
.k{{color:var(--brass);font-size:.78rem;letter-spacing:.18em;text-transform:uppercase;font-weight:700;margin-bottom:14px}}
h1{{font-family:'Libre Baskerville',serif;font-size:clamp(2rem,4vw,3.2rem);line-height:1.2;color:var(--navy);margin-bottom:18px}}
.lead{{color:var(--mute);max-width:34rem;margin-bottom:28px;font-size:1.05rem}}
.panel{{border:1px solid var(--line);background:var(--bg);padding:28px}}
.panel h3{{font-family:'Libre Baskerville',serif;font-size:1.25rem;margin-bottom:10px;color:var(--navy)}}
.section{{padding:64px 8vw}}
.section h2{{font-family:'Libre Baskerville',serif;font-size:1.9rem;color:var(--navy);margin-bottom:8px}}
.sub{{color:var(--mute);margin-bottom:24px}}
.grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}}
@media(max-width:900px){{.grid{{grid-template-columns:1fr}}}}
.card{{background:#FFFEFB;border:1px solid var(--line);padding:24px}}
.card h3{{font-family:'Libre Baskerville',serif;font-size:1.15rem;margin-bottom:8px;color:var(--navy)}}
.card p{{color:var(--mute)}}
.tool{{margin:0 8vw 70px;background:#FFFEFB;border:1px solid var(--line);padding:36px;text-align:center}}
.val{{font-family:'Libre Baskerville',serif;font-size:2rem;color:var(--brass);margin:12px 0}}
input[type=range]{{width:min(100%,420px);accent-color:var(--navy)}}
footer{{background:var(--navy);color:#C9C4B8;padding:42px 8vw;text-align:center}}
.modal{{display:none;position:fixed;inset:0;background:rgba(27,26,23,.5);align-items:center;justify-content:center;padding:18px;z-index:40}}
.modal.open{{display:flex}}
.modal-card{{background:#FFFEFB;padding:28px;width:min(440px,100%);border:1px solid var(--line);position:relative}}
.modal-card input{{width:100%;margin:8px 0;padding:12px;border:1px solid var(--line)}}
.close{{position:absolute;right:12px;top:8px;border:0;background:none;font-size:1.4rem;cursor:pointer;color:var(--mute)}}
</style></head><body>
<header><a class="logo" href="#">{n}</a><button class="btn" onclick="openM()">Consultation</button></header>
<section class="hero">
  <div>
    <div class="k">Counsel · {c}</div>
    <h1>Advocacy with composure. Strategy without theatrics.</h1>
    <p class="lead">{n} advises and represents clients who value preparation, discretion, and direct communication.</p>
    <button class="btn gold" onclick="openM()">Schedule evaluation</button>
  </div>
  <aside class="panel">
    <div class="k">Intake</div>
    <h3>Privileged first conversation</h3>
    <p style="color:var(--mute);margin-bottom:14px">Direct attorney line: <strong style="color:var(--ink)">{p}</strong></p>
    <p style="color:var(--mute);font-size:.92rem">Legal design language: paper, brass, navy — authority that feels institutional, not flashy.</p>
  </aside>
</section>
<section class="section">
  <h2>Practice focus</h2>
  <p class="sub">Structured for trust: long-form readability, serif headlines, zero gimmicks.</p>
  <div class="grid">{cards}</div>
</section>
<section class="tool">
  <div class="k">Matter scale</div>
  <h2 style="font-family:'Libre Baskerville',serif;font-size:1.6rem;color:var(--navy);margin:8px 0">Confidential range indicator</h2>
  <div class="val" id="v">$1,500,000 matter scale</div>
  <input type="range" min="100000" max="10000000" step="100000" value="1500000" oninput="document.getElementById('v').textContent='$'+parseInt(this.value).toLocaleString()+' matter scale'">
  <div style="margin-top:16px"><button class="btn" onclick="openM()">Begin confidential inquiry</button></div>
</section>
<footer>{n}<br>{c} · {p}</footer>
<div class="modal" id="m"><div class="modal-card">
  <button class="close" onclick="closeM()">×</button>
  <h3 style="font-family:'Libre Baskerville',serif;margin-bottom:8px">Confidential inquiry</h3>
  <form onsubmit="event.preventDefault();closeM();alert('Inquiry received by {n}.');">
    <input placeholder="Name *" required><input placeholder="Phone *" required><input placeholder="Brief matter summary">
    <button class="btn" style="width:100%;margin-top:8px">Submit</button>
  </form>
</div></div>
<script>function openM(){{document.getElementById('m').classList.add('open')}}function closeM(){{document.getElementById('m').classList.remove('open')}}</script>
</body></html>"""

    # ================================================================== REALTY
    def _realty(self, name: str, cat: str, city: str, phone: str) -> str:
        n, c, p = self._esc(name), self._esc(city), self._esc(phone)
        return f"""<!DOCTYPE html>
<html lang="en"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{n} · Properties · {c}</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Manrope:wght@400;500;600;700&display=swap');
:root{{--bg:#F3EFE7;--ink:#1C1916;--mute:#6F675E;--line:#DDD4C6;--forest:#2F4F3E;--clay:#A56B45}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:'Manrope',sans-serif;background:var(--bg);color:var(--ink);line-height:1.7}}
.nav{{display:flex;justify-content:space-between;align-items:center;padding:18px 6vw;position:absolute;left:0;right:0;top:0;z-index:5;color:#fff}}
.logo{{font-family:'Instrument Serif',serif;font-size:1.6rem;color:#fff;text-decoration:none}}
.btn{{background:#fff;color:var(--ink);border:0;padding:11px 18px;font-weight:700;font-size:.78rem;letter-spacing:.04em;text-transform:uppercase;cursor:pointer}}
.btn.dark{{background:var(--forest);color:#fff}}
.hero{{min-height:78vh;display:flex;align-items:flex-end;padding:0 6vw 70px;background:
 linear-gradient(180deg,rgba(28,25,22,.15),rgba(28,25,22,.72)),
 url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="1000"><defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop stop-color="%233a4d3f"/><stop offset="1" stop-color="%237a5a3a"/></linearGradient></defs><rect width="100%" height="100%" fill="url(%23g)"/><circle cx="70%" cy="30%" r="220" fill="%23ffffff11"/><rect x="8%" y="48%" width="38%" height="28%" fill="%2300000018"/></svg>');
 background-size:cover;color:#fff}}
.hero .k{{letter-spacing:.22em;text-transform:uppercase;font-size:.72rem;opacity:.85;margin-bottom:12px}}
.hero h1{{font-family:'Instrument Serif',serif;font-size:clamp(2.6rem,6vw,4.6rem);line-height:1.05;max-width:14ch;font-weight:400;margin-bottom:14px}}
.hero p{{max-width:34rem;opacity:.9;margin-bottom:22px}}
.section{{padding:70px 6vw}}
.section h2{{font-family:'Instrument Serif',serif;font-size:2.4rem;font-weight:400;margin-bottom:8px}}
.sub{{color:var(--mute);margin-bottom:26px}}
.listings{{display:grid;grid-template-columns:1.2fr .8fr;gap:18px}}
@media(max-width:900px){{.listings{{grid-template-columns:1fr}}}}
.photo{{min-height:320px;background:linear-gradient(135deg,#6d7f6a,#c2a27a);border:1px solid var(--line);padding:24px;display:flex;flex-direction:column;justify-content:flex-end;color:#fff}}
.photo h3{{font-family:'Instrument Serif',serif;font-size:2rem;font-weight:400}}
.side-card{{background:#fff;border:1px solid var(--line);padding:24px}}
.side-card + .side-card{{margin-top:14px}}
.price{{font-family:'Instrument Serif',serif;font-size:1.8rem;color:var(--forest);margin-top:8px}}
.tool{{margin:0 6vw 70px;background:#fff;border:1px solid var(--line);padding:36px;text-align:center}}
.val{{font-family:'Instrument Serif',serif;font-size:2.2rem;color:var(--clay);margin:12px 0}}
input[type=range]{{width:min(100%,440px);accent-color:var(--forest)}}
footer{{padding:40px 6vw;border-top:1px solid var(--line);color:var(--mute);text-align:center}}
.modal{{display:none;position:fixed;inset:0;background:rgba(28,25,22,.5);align-items:center;justify-content:center;padding:18px;z-index:40}}
.modal.open{{display:flex}}
.modal-card{{background:#fff;padding:28px;width:min(440px,100%);position:relative;border:1px solid var(--line)}}
.modal-card input{{width:100%;margin:8px 0;padding:12px;border:1px solid var(--line)}}
.close{{position:absolute;right:12px;top:8px;border:0;background:none;font-size:1.4rem;cursor:pointer}}
</style></head><body>
<nav><a class="logo" href="#">{n}</a><button class="btn" onclick="openM()">Book showing</button></nav>
<section class="hero">
  <div>
    <div class="k">Property · {c}</div>
    <h1>Spaces with architecture, light, and long views</h1>
    <p>{n} curates residences and investments for buyers who care about proportion, materials, and neighborhood texture — not listing spam.</p>
    <button class="btn dark" onclick="openM()">Request private shortlist</button>
  </div>
</section>
<section class="section">
  <h2>Selected inventory mood</h2>
  <p class="sub">Real-estate design: large hero, material palette, magazine serif — like an architecture folio.</p>
  <div class="listings">
    <div class="photo">
      <div class="k">Featured</div>
      <h3>Skyline residence</h3>
      <p style="opacity:.9;max-width:28rem">Open plan, stone kitchen, evening terrace light. Built for slow living above the city.</p>
    </div>
    <div>
      <div class="side-card">
        <div class="k" style="color:var(--mute)">Listing study</div>
        <h3 style="font-family:'Instrument Serif',serif;font-size:1.5rem;font-weight:400">Waterfront house</h3>
        <p style="color:var(--mute)">Dock access, garden rooms, quiet morning light.</p>
        <div class="price">$7.2M</div>
      </div>
      <div class="side-card">
        <div class="k" style="color:var(--mute)">Advisory</div>
        <h3 style="font-family:'Instrument Serif',serif;font-size:1.5rem;font-weight:400">Yield framing</h3>
        <p style="color:var(--mute)">We help investors read a property beyond the brochure.</p>
        <p style="margin-top:10px"><strong>Desk:</strong> {p}</p>
      </div>
    </div>
  </div>
</section>
<section class="tool">
  <div class="k" style="letter-spacing:.18em;text-transform:uppercase;font-size:.72rem;color:var(--mute)">Yield sketch</div>
  <h2 style="font-family:'Instrument Serif',serif;font-size:2rem;font-weight:400;margin:8px 0">Purchase price → annual yield</h2>
  <div class="val" id="v">$2,500,000 · ~$212,500 / yr</div>
  <input type="range" min="500000" max="12000000" step="100000" value="2500000" oninput="const y=Math.round(this.value*0.085);document.getElementById('v').textContent='$'+parseInt(this.value).toLocaleString()+' · ~$'+y.toLocaleString()+' / yr'">
  <div style="margin-top:16px"><button class="btn dark" onclick="openM()">Talk to an advisor</button></div>
</section>
<footer>{n} · {c} · {p}</footer>
<div class="modal" id="m"><div class="modal-card">
  <button class="close" onclick="closeM()">×</button>
  <h3 style="font-family:'Instrument Serif',serif;font-size:1.6rem;margin-bottom:8px">Showing request</h3>
  <form onsubmit="event.preventDefault();closeM();alert('Request sent to {n}.');">
    <input placeholder="Name *" required><input placeholder="Phone *" required><input placeholder="Budget window">
    <button class="btn dark" style="width:100%;margin-top:8px">Submit</button>
  </form>
</div></div>
<script>function openM(){{document.getElementById('m').classList.add('open')}}function closeM(){{document.getElementById('m').classList.remove('open')}}</script>
</body></html>"""

    # ================================================================== GYM
    def _gym(self, name: str, cat: str, city: str, phone: str) -> str:
        n, c, p = self._esc(name), self._esc(city), self._esc(phone)
        cards = self._cards([
            ("Strength programming", "Progressive blocks for real lifts, not random workouts."),
            ("Conditioning", "Engine work that respects joints and recovery."),
            ("Coaching desk", "Form checks, accountability, and measurable PRs."),
        ])
        return f"""<!DOCTYPE html>
<html lang="en"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{n} · Training · {c}</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Archivo+Black&family=Space+Grotesk:wght@400;500;600;700&display=swap');
:root{{--bg:#0B0B0C;--panel:#141416;--ink:#F5F5F5;--mute:#A1A1AA;--line:#27272A;--volt:#FF4D00}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:'Space Grotesk',sans-serif;background:var(--bg);color:var(--ink);line-height:1.65}}
.nav{{display:flex;justify-content:space-between;align-items:center;padding:18px 6vw;border-bottom:1px solid var(--line);position:sticky;top:0;background:rgba(11,11,12,.92);z-index:10}}
.logo{{font-family:'Archivo Black',sans-serif;font-size:1.1rem;letter-spacing:.02em;text-decoration:none;color:#fff}}
.btn{{background:var(--volt);color:#000;border:0;padding:12px 18px;font-weight:700;text-transform:uppercase;letter-spacing:.06em;font-size:.75rem;cursor:pointer}}
.hero{{padding:80px 6vw 60px;display:grid;grid-template-columns:1.1fr .9fr;gap:30px;align-items:end;border-bottom:1px solid var(--line)}}
@media(max-width:900px){{.hero{{grid-template-columns:1fr;padding:50px 6vw}}}}
.k{{color:var(--volt);font-weight:700;letter-spacing:.16em;text-transform:uppercase;font-size:.75rem;margin-bottom:14px}}
h1{{font-family:'Archivo Black',sans-serif;font-size:clamp(2.6rem,7vw,4.8rem);line-height:.95;text-transform:uppercase;margin-bottom:18px}}
.lead{{color:var(--mute);max-width:32rem;margin-bottom:24px}}
.statbox{{background:var(--panel);border:1px solid var(--line);padding:24px}}
.statbox strong{{display:block;font-family:'Archivo Black',sans-serif;font-size:2.4rem;color:var(--volt)}}
.section{{padding:60px 6vw}}
.section h2{{font-family:'Archivo Black',sans-serif;text-transform:uppercase;font-size:1.8rem;margin-bottom:8px}}
.sub{{color:var(--mute);margin-bottom:22px}}
.grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}}
@media(max-width:900px){{.grid{{grid-template-columns:1fr}}}}
.card{{background:var(--panel);border:1px solid var(--line);padding:22px}}
.card h3{{font-size:1.05rem;margin-bottom:8px;text-transform:uppercase;letter-spacing:.04em}}
.card p{{color:var(--mute)}}
.tool{{margin:0 6vw 70px;border:1px solid var(--line);background:var(--panel);padding:34px;text-align:center}}
.val{{font-family:'Archivo Black',sans-serif;font-size:2.4rem;color:var(--volt);margin:12px 0}}
input[type=range]{{width:min(100%,420px);accent-color:var(--volt)}}
footer{{padding:36px 6vw;border-top:1px solid var(--line);color:var(--mute);text-align:center}}
.modal{{display:none;position:fixed;inset:0;background:rgba(0,0,0,.7);align-items:center;justify-content:center;padding:18px;z-index:40}}
.modal.open{{display:flex}}
.modal-card{{background:#141416;border:1px solid var(--line);padding:26px;width:min(440px,100%);position:relative}}
.modal-card input{{width:100%;margin:8px 0;padding:12px;background:#0B0B0C;border:1px solid var(--line);color:#fff}}
.close{{position:absolute;right:12px;top:8px;border:0;background:none;color:var(--mute);font-size:1.4rem;cursor:pointer}}
</style></head><body>
<nav><a class="logo" href="#">{n}</a><button class="btn" onclick="openM()">Join / Trial</button></nav>
<section class="hero">
  <div>
    <div class="k">Training floor · {c}</div>
    <h1>Train hard.<br>Recover smarter.</h1>
    <p class="lead">{n} is an athletic room for people who want strength, sweat, and accountability — bold type, high contrast, zero pastel fluff.</p>
    <button class="btn" onclick="openM()">Start a trial week</button>
  </div>
  <div class="statbox">
    <div class="k">Floor metrics</div>
    <strong>240+</strong>
    <span style="color:var(--mute)">active members pushing weekly PRs</span>
    <p style="margin-top:16px;color:var(--mute)">Coach line: <span style="color:#fff">{p}</span></p>
  </div>
</section>
<section class="section">
  <h2>Programming pillars</h2>
  <p class="sub">Fitness psychology: urgency, power, clarity. Orange voltage on black — energy without cyber neon.</p>
  <div class="grid">{cards}</div>
</section>
<section class="tool">
  <div class="k">Session builder</div>
  <h2 style="font-family:'Archivo Black',sans-serif;text-transform:uppercase;font-size:1.5rem;margin:8px 0">Weekly training days</h2>
  <div class="val" id="v">4 days / week</div>
  <input type="range" min="2" max="6" value="4" oninput="document.getElementById('v').textContent=this.value+' days / week'">
  <div style="margin-top:16px"><button class="btn" onclick="openM()">Lock my plan</button></div>
</section>
<footer>{n} · {c} · {p}</footer>
<div class="modal" id="m"><div class="modal-card">
  <button class="close" onclick="closeM()">×</button>
  <h3 style="text-transform:uppercase;letter-spacing:.06em;margin-bottom:8px">Trial request</h3>
  <form onsubmit="event.preventDefault();closeM();alert('Trial request sent to {n}.');">
    <input placeholder="Name *" required><input placeholder="Phone *" required><input placeholder="Goal (strength / fat loss / hybrid)">
    <button class="btn" style="width:100%;margin-top:8px">Send</button>
  </form>
</div></div>
<script>function openM(){{document.getElementById('m').classList.add('open')}}function closeM(){{document.getElementById('m').classList.remove('open')}}</script>
</body></html>"""

    # ================================================================== SPA
    def _spa(self, name: str, cat: str, city: str, phone: str) -> str:
        n, c, p = self._esc(name), self._esc(city), self._esc(phone)
        cards = self._cards([
            ("Facial rituals", "Skin-first protocols with unhurried pacing."),
            ("Body treatments", "Tension release and recovery in quiet rooms."),
            ("Membership calm", "Recurring care without membership pressure theater."),
        ])
        return f"""<!DOCTYPE html>
<html lang="en"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{n} · Sanctuary · {c}</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant:wght@400;500;600&family=Nunito+Sans:wght@300;400;600;700&display=swap');
:root{{--bg:#F8F1EC;--ink:#3D2C29;--mute:#8A736C;--line:#E8D8D0;--rose:#C9897B;--cream:#FFFCF9}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:'Nunito Sans',sans-serif;background:var(--bg);color:var(--ink);line-height:1.8}}
.nav{{display:flex;justify-content:space-between;align-items:center;padding:22px 7vw;background:rgba(248,241,236,.9);border-bottom:1px solid var(--line);position:sticky;top:0;z-index:10}}
.logo{{font-family:'Cormorant',serif;font-size:1.7rem;font-weight:500;text-decoration:none;color:var(--ink)}}
.btn{{background:var(--rose);color:#fff;border:0;padding:12px 20px;border-radius:999px;font-weight:700;cursor:pointer}}
.hero{{padding:70px 7vw;display:grid;grid-template-columns:1fr 1fr;gap:36px;align-items:center}}
@media(max-width:900px){{.hero{{grid-template-columns:1fr;padding:40px 6vw}}}}
.k{{color:var(--rose);letter-spacing:.18em;text-transform:uppercase;font-size:.72rem;font-weight:700;margin-bottom:12px}}
h1{{font-family:'Cormorant',serif;font-size:clamp(2.4rem,5vw,3.8rem);font-weight:500;line-height:1.12;margin-bottom:14px}}
.lead{{color:var(--mute);margin-bottom:24px;font-weight:300;font-size:1.05rem}}
.blob{{min-height:340px;border-radius:40% 60% 55% 45% / 50% 40% 60% 50%;background:
 radial-gradient(circle at 30% 30%, #fff, transparent 45%),
 linear-gradient(160deg,#E7C4B8,#F3E0D6 55%, #D9B7A8);border:1px solid var(--line)}}
.section{{padding:20px 7vw 70px}}
.section h2{{font-family:'Cormorant',serif;font-size:2.2rem;font-weight:500;margin-bottom:8px}}
.sub{{color:var(--mute);margin-bottom:22px}}
.grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}}
@media(max-width:900px){{.grid{{grid-template-columns:1fr}}}}
.card{{background:var(--cream);border:1px solid var(--line);border-radius:24px;padding:24px}}
.card h3{{font-family:'Cormorant',serif;font-size:1.45rem;font-weight:500;margin-bottom:8px}}
.card p{{color:var(--mute);font-weight:300}}
.tool{{margin:0 7vw 70px;background:var(--cream);border:1px solid var(--line);border-radius:28px;padding:36px;text-align:center}}
.val{{font-family:'Cormorant',serif;font-size:2.2rem;color:var(--rose);margin:12px 0}}
input[type=range]{{width:min(100%,400px);accent-color:var(--rose)}}
footer{{padding:40px 7vw;text-align:center;color:var(--mute);border-top:1px solid var(--line)}}
.modal{{display:none;position:fixed;inset:0;background:rgba(61,44,41,.35);align-items:center;justify-content:center;padding:18px;z-index:40}}
.modal.open{{display:flex}}
.modal-card{{background:var(--cream);border-radius:22px;padding:28px;width:min(440px,100%);position:relative;border:1px solid var(--line)}}
.modal-card input{{width:100%;margin:8px 0;padding:12px;border:1px solid var(--line);border-radius:12px;background:#fff}}
.close{{position:absolute;right:12px;top:8px;border:0;background:none;font-size:1.4rem;cursor:pointer;color:var(--mute)}}
</style></head><body>
<nav><a class="logo" href="#">{n}</a><button class="btn" onclick="openM()">Book ritual</button></nav>
<section class="hero">
  <div>
    <div class="k">Sanctuary · {c}</div>
    <h1>Soft rooms. Slow rituals. Skin that looks rested.</h1>
    <p class="lead">{n} is a wellness house for people who want restoration without clinical coldness or flashy spa clichés.</p>
    <button class="btn" onclick="openM()">Reserve a treatment</button>
  </div>
  <div class="blob" aria-hidden="true"></div>
</section>
<section class="section">
  <h2>Rituals</h2>
  <p class="sub">Wellness design: blush, cream, organic curves — parasympathetic, not promotional neon.</p>
  <div class="grid">{cards}</div>
</section>
<section class="tool">
  <div class="k">Session length</div>
  <h2 style="font-family:'Cormorant',serif;font-size:1.8rem;font-weight:500;margin:8px 0">How long do you want to unplug?</h2>
  <div class="val" id="v">75 minutes</div>
  <input type="range" min="45" max="120" step="15" value="75" oninput="document.getElementById('v').textContent=this.value+' minutes'">
  <div style="margin-top:16px"><button class="btn" onclick="openM()">Book this length</button></div>
</section>
<footer>{n} · {c} · {p}</footer>
<div class="modal" id="m"><div class="modal-card">
  <button class="close" onclick="closeM()">×</button>
  <h3 style="font-family:'Cormorant',serif;font-size:1.6rem;margin-bottom:8px">Treatment request</h3>
  <form onsubmit="event.preventDefault();closeM();alert('Request received by {n}.');">
    <input placeholder="Name *" required><input placeholder="Phone *" required><input placeholder="Treatment interest">
    <button class="btn" style="width:100%;margin-top:8px">Send</button>
  </form>
</div></div>
<script>function openM(){{document.getElementById('m').classList.add('open')}}function closeM(){{document.getElementById('m').classList.remove('open')}}</script>
</body></html>"""

    # ================================================================== JEWELRY
    def _jewelry(self, name: str, cat: str, city: str, phone: str) -> str:
        n, c, p = self._esc(name), self._esc(city), self._esc(phone)
        return f"""<!DOCTYPE html>
<html lang="en"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{n} · Atelier · {c}</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Bodoni+Moda:opsz,wght@6..96,500;6..96,600&family=Inter:wght@300;400;500;600&display=swap');
:root{{--bg:#0E0E0F;--ink:#F7F3EA;--mute:#A39E93;--line:rgba(247,243,234,.14);--gold:#C2A46B}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:'Inter',sans-serif;background:var(--bg);color:var(--ink);line-height:1.75}}
.nav{{display:flex;justify-content:space-between;align-items:center;padding:22px 7vw;border-bottom:1px solid var(--line)}}
.logo{{font-family:'Bodoni Moda',serif;font-size:1.5rem;letter-spacing:.08em;text-decoration:none;color:var(--ink)}}
.btn{{border:1px solid var(--gold);color:var(--gold);background:transparent;padding:11px 18px;letter-spacing:.12em;text-transform:uppercase;font-size:.68rem;cursor:pointer}}
.btn.fill{{background:var(--gold);color:#111}}
.hero{{padding:90px 7vw;text-align:center;border-bottom:1px solid var(--line)}}
.k{{color:var(--gold);letter-spacing:.28em;text-transform:uppercase;font-size:.7rem;margin-bottom:18px}}
h1{{font-family:'Bodoni Moda',serif;font-size:clamp(2.6rem,6vw,4.4rem);font-weight:500;line-height:1.08;margin-bottom:16px}}
.lead{{color:var(--mute);max-width:34rem;margin:0 auto 28px;font-weight:300}}
.ring{{width:min(280px,70vw);height:min(280px,70vw);margin:30px auto 10px;border-radius:50%;border:1px solid var(--gold);box-shadow:inset 0 0 0 18px rgba(194,164,107,.08);position:relative}}
.ring:after{{content:"";position:absolute;inset:28%;border-radius:50%;border:1px solid rgba(194,164,107,.35)}}
.section{{padding:70px 7vw}}
.grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}}
@media(max-width:900px){{.grid{{grid-template-columns:1fr}}}}
.card{{border:1px solid var(--line);padding:26px;text-align:center}}
.card h3{{font-family:'Bodoni Moda',serif;font-size:1.5rem;font-weight:500;margin-bottom:8px;color:var(--gold)}}
.card p{{color:var(--mute);font-weight:300;font-size:.95rem}}
.tool{{margin:0 7vw 70px;border:1px solid var(--line);padding:40px;text-align:center}}
.val{{font-family:'Bodoni Moda',serif;font-size:2.2rem;color:var(--gold);margin:12px 0}}
input[type=range]{{width:min(100%,400px);accent-color:var(--gold)}}
footer{{padding:40px 7vw;border-top:1px solid var(--line);text-align:center;color:var(--mute);font-weight:300}}
.modal{{display:none;position:fixed;inset:0;background:rgba(0,0,0,.7);align-items:center;justify-content:center;padding:18px;z-index:40}}
.modal.open{{display:flex}}
.modal-card{{background:#141414;border:1px solid var(--line);padding:28px;width:min(440px,100%);position:relative}}
.modal-card input{{width:100%;margin:8px 0;padding:12px;background:#0E0E0F;border:1px solid var(--line);color:var(--ink)}}
.close{{position:absolute;right:12px;top:8px;border:0;background:none;color:var(--mute);font-size:1.4rem;cursor:pointer}}
</style></head><body>
<nav><a class="logo" href="#">{n}</a><button class="btn" onclick="openM()">Private viewing</button></nav>
<section class="hero">
  <div class="k">High jewelry · {c}</div>
  <h1>Quiet brilliance. Precise craft.</h1>
  <p class="lead">{n} presents jewels with atelier restraint — black field, ivory type, thin gold lines. Luxury that whispers.</p>
  <div class="ring" aria-hidden="true"></div>
  <button class="btn fill" onclick="openM()">Request a viewing</button>
</section>
<section class="section">
  <div class="grid">
    <article class="card"><h3>Bridal</h3><p>Engagement studies and eternity lines with measured sparkle.</p></article>
    <article class="card"><h3>Atelier custom</h3><p>Bespoke commissions guided by stone, proportion, and story.</p></article>
    <article class="card"><h3>Heritage service</h3><p>Resetting, polishing, and confidential evaluations.</p></article>
  </div>
</section>
<section class="tool">
  <div class="k">Carat conversation</div>
  <h2 style="font-family:'Bodoni Moda',serif;font-size:1.8rem;font-weight:500;margin:8px 0">Center-stone preference</h2>
  <div class="val" id="v">1.50 ct</div>
  <input type="range" min="50" max="500" value="150" oninput="document.getElementById('v').textContent=(this.value/100).toFixed(2)+' ct'">
  <div style="margin-top:16px"><button class="btn fill" onclick="openM()">Discuss this stone</button></div>
</section>
<footer>{n} · {c} · {p}</footer>
<div class="modal" id="m"><div class="modal-card">
  <button class="close" onclick="closeM()">×</button>
  <h3 style="font-family:'Bodoni Moda',serif;font-size:1.5rem;margin-bottom:8px">Private viewing</h3>
  <form onsubmit="event.preventDefault();closeM();alert('Viewing request sent to {n}.');">
    <input placeholder="Name *" required><input placeholder="Phone *" required><input placeholder="Interest (bridal / custom / service)">
    <button class="btn fill" style="width:100%;margin-top:8px">Send</button>
  </form>
</div></div>
<script>function openM(){{document.getElementById('m').classList.add('open')}}function closeM(){{document.getElementById('m').classList.remove('open')}}</script>
</body></html>"""

    # ================================================================== WEALTH
    def _wealth(self, name: str, cat: str, city: str, phone: str) -> str:
        n, c, p = self._esc(name), self._esc(city), self._esc(phone)
        cards = self._cards([
            ("Portfolio architecture", "Allocation frameworks matched to time horizon and risk."),
            ("Family office liaison", "Multi-generational planning with discreet coordination."),
            ("Liquidity events", "Pre- and post-exit structuring conversations."),
        ])
        return f"""<!DOCTYPE html>
<html lang="en"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{n} · Private advisory · {c}</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Newsreader:opsz,wght@6..72,500;6..72,600&family=IBM+Plex+Sans:wght@300;400;500;600&display=swap');
:root{{--bg:#F2EFE8;--ink:#171A21;--mute:#667084;--line:#D9D3C7;--navy:#18233A;--gold:#8E7340}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:'IBM Plex Sans',sans-serif;background:var(--bg);color:var(--ink);line-height:1.75}}
.nav{{display:flex;justify-content:space-between;align-items:center;padding:20px 7vw;background:rgba(242,239,232,.94);border-bottom:1px solid var(--line);position:sticky;top:0;z-index:10}}
.logo{{font-family:'Newsreader',serif;font-size:1.35rem;text-decoration:none;color:var(--navy);font-weight:600}}
.btn{{background:var(--navy);color:#fff;border:0;padding:12px 18px;font-size:.78rem;font-weight:600;letter-spacing:.04em;cursor:pointer}}
.hero{{padding:70px 7vw;display:grid;grid-template-columns:1.15fr .85fr;gap:36px;align-items:center}}
@media(max-width:900px){{.hero{{grid-template-columns:1fr;padding:40px 6vw}}}}
.k{{color:var(--gold);font-size:.75rem;letter-spacing:.16em;text-transform:uppercase;font-weight:600;margin-bottom:12px}}
h1{{font-family:'Newsreader',serif;font-size:clamp(2.2rem,4.5vw,3.3rem);line-height:1.15;color:var(--navy);margin-bottom:14px;font-weight:600}}
.lead{{color:var(--mute);margin-bottom:24px;font-weight:300;max-width:34rem}}
.panel{{background:#FFFEFA;border:1px solid var(--line);padding:26px}}
.panel h3{{font-family:'Newsreader',serif;font-size:1.35rem;margin-bottom:8px;color:var(--navy)}}
.section{{padding:20px 7vw 70px}}
.section h2{{font-family:'Newsreader',serif;font-size:2rem;color:var(--navy);margin-bottom:8px}}
.sub{{color:var(--mute);margin-bottom:22px}}
.grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}}
@media(max-width:900px){{.grid{{grid-template-columns:1fr}}}}
.card{{background:#FFFEFA;border:1px solid var(--line);padding:22px}}
.card h3{{font-family:'Newsreader',serif;font-size:1.15rem;margin-bottom:8px;color:var(--navy)}}
.card p{{color:var(--mute);font-weight:300}}
.tool{{margin:0 7vw 70px;background:#FFFEFA;border:1px solid var(--line);padding:34px;text-align:center}}
.val{{font-family:'Newsreader',serif;font-size:2rem;color:var(--gold);margin:12px 0}}
input[type=range]{{width:min(100%,420px);accent-color:var(--navy)}}
footer{{background:var(--navy);color:#B7BFCLE;color:#B7BFC9;padding:40px 7vw;text-align:center}}
.modal{{display:none;position:fixed;inset:0;background:rgba(23,26,33,.45);align-items:center;justify-content:center;padding:18px;z-index:40}}
.modal.open{{display:flex}}
.modal-card{{background:#FFFEFA;padding:28px;width:min(440px,100%);border:1px solid var(--line);position:relative}}
.modal-card input{{width:100%;margin:8px 0;padding:12px;border:1px solid var(--line)}}
.close{{position:absolute;right:12px;top:8px;border:0;background:none;font-size:1.4rem;cursor:pointer;color:var(--mute)}}
</style></head><body>
<nav><a class="logo" href="#">{n}</a><button class="btn" onclick="openM()">Private intro</button></nav>
<section class="hero">
  <div>
    <div class="k">Private advisory · {c}</div>
    <h1>Stewardship for capital that must outlast the moment.</h1>
    <p class="lead">{n} works with families and principals who prefer measured process, plain language, and rooms that feel like a private bank — not a fintech billboard.</p>
    <button class="btn" onclick="openM()">Request an introduction</button>
  </div>
  <aside class="panel">
    <div class="k">Desk</div>
    <h3>Confidential first meeting</h3>
    <p style="color:var(--mute);margin-bottom:10px">Direct line: <strong style="color:var(--ink)">{p}</strong></p>
    <p style="color:var(--mute);font-size:.92rem;font-weight:300">Design cues: parchment, navy, restrained brass — institutional calm.</p>
  </aside>
</section>
<section class="section">
  <h2>Advisory pillars</h2>
  <p class="sub">Wealth UX: trust density over visual excitement.</p>
  <div class="grid">{cards}</div>
</section>
<section class="tool">
  <div class="k">Planning horizon</div>
  <h2 style="font-family:'Newsreader',serif;font-size:1.6rem;color:var(--navy);margin:8px 0">Years under consideration</h2>
  <div class="val" id="v">15-year horizon</div>
  <input type="range" min="3" max="40" value="15" oninput="document.getElementById('v').textContent=this.value+'-year horizon'">
  <div style="margin-top:16px"><button class="btn" onclick="openM()">Discuss this horizon</button></div>
</section>
<footer>{n}<br>{c} · {p}</footer>
<div class="modal" id="m"><div class="modal-card">
  <button class="close" onclick="closeM()">×</button>
  <h3 style="font-family:'Newsreader',serif;margin-bottom:8px">Private introduction</h3>
  <form onsubmit="event.preventDefault();closeM();alert('Introduction request received by {n}.');">
    <input placeholder="Name *" required><input placeholder="Phone *" required><input placeholder="Context (family / liquidity / portfolio)">
    <button class="btn" style="width:100%;margin-top:8px">Submit</button>
  </form>
</div></div>
<script>function openM(){{document.getElementById('m').classList.add('open')}}function closeM(){{document.getElementById('m').classList.remove('open')}}</script>
</body></html>"""

    # ================================================================== UNIVERSAL
    def _universal(self, name: str, cat: str, city: str, phone: str) -> str:
        n, c, p = self._esc(name), self._esc(city), self._esc(phone)
        cat_title = self._esc((cat or "Professional Services").title())
        cards = self._cards([
            (f"Core {cat_title}", f"Signature {cat_title.lower()} work delivered with consistency."),
            ("Client path", "Clear inquiry → consult → delivery without friction."),
            ("Local trust", f"Built for people searching around {c}."),
        ])
        # Distinct from LeadFlow product: deep ink + electric indigo accent (not cyan neon)
        return f"""<!DOCTYPE html>
<html lang="en"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{n} · {cat_title} · {c}</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Sora:wght@400;500;600;700&family=IBM+Plex+Sans:wght@300;400;600&display=swap');
:root{{--bg:#F4F6FB;--ink:#12141C;--mute:#5C6478;--line:#D9DEEA;--ind:#3B4CCA;--soft:#E8EBFF}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:'IBM Plex Sans',sans-serif;background:var(--bg);color:var(--ink);line-height:1.7}}
.nav{{display:flex;justify-content:space-between;align-items:center;padding:18px 6vw;background:#fff;border-bottom:1px solid var(--line);position:sticky;top:0;z-index:10}}
.logo{{font-family:'Sora',sans-serif;font-weight:700;text-decoration:none;color:var(--ink)}}
.btn{{background:var(--ind);color:#fff;border:0;padding:12px 18px;border-radius:12px;font-weight:700;cursor:pointer}}
.hero{{padding:70px 6vw;display:grid;grid-template-columns:1.15fr .85fr;gap:28px;align-items:center}}
@media(max-width:900px){{.hero{{grid-template-columns:1fr;padding:40px 6vw}}}}
.k{{display:inline-block;background:var(--soft);color:var(--ind);padding:6px 10px;border-radius:999px;font-size:.75rem;font-weight:700;margin-bottom:12px}}
h1{{font-family:'Sora',sans-serif;font-size:clamp(2rem,4vw,3rem);line-height:1.15;margin-bottom:14px}}
.lead{{color:var(--mute);margin-bottom:22px;max-width:34rem}}
.panel{{background:#fff;border:1px solid var(--line);border-radius:20px;padding:24px}}
.section{{padding:20px 6vw 70px}}
.section h2{{font-family:'Sora',sans-serif;font-size:1.7rem;margin-bottom:8px}}
.sub{{color:var(--mute);margin-bottom:20px}}
.grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}}
@media(max-width:900px){{.grid{{grid-template-columns:1fr}}}}
.card{{background:#fff;border:1px solid var(--line);border-radius:18px;padding:22px}}
.card h3{{font-family:'Sora',sans-serif;font-size:1.05rem;margin-bottom:8px}}
.card p{{color:var(--mute)}}
.tool{{margin:0 6vw 70px;background:#fff;border:1px solid var(--line);border-radius:20px;padding:32px;text-align:center}}
.val{{font-family:'Sora',sans-serif;font-size:1.8rem;color:var(--ind);margin:12px 0}}
input[type=range]{{width:min(100%,400px);accent-color:var(--ind)}}
footer{{padding:36px 6vw;border-top:1px solid var(--line);text-align:center;color:var(--mute);background:#fff}}
.modal{{display:none;position:fixed;inset:0;background:rgba(18,20,28,.4);align-items:center;justify-content:center;padding:18px;z-index:40}}
.modal.open{{display:flex}}
.modal-card{{background:#fff;border-radius:18px;padding:26px;width:min(440px,100%);position:relative;border:1px solid var(--line)}}
.modal-card input{{width:100%;margin:8px 0;padding:12px;border:1px solid var(--line);border-radius:10px}}
.close{{position:absolute;right:12px;top:8px;border:0;background:none;font-size:1.4rem;cursor:pointer;color:var(--mute)}}
</style></head><body>
<nav><a class="logo" href="#">{n}</a><button class="btn" onclick="openM()">Contact</button></nav>
<section class="hero">
  <div>
    <div class="k">{cat_title} · {c}</div>
    <h1>A sharper digital front door for {cat_title.lower()}</h1>
    <p class="lead">{n} helps clients in {c} understand the offer fast, trust the process, and take the next step without friction.</p>
    <button class="btn" onclick="openM()">Start a conversation</button>
  </div>
  <aside class="panel">
    <div class="k">Studio notes</div>
    <h3 style="font-family:'Sora',sans-serif;margin:8px 0">Category-tuned layout</h3>
    <p style="color:var(--mute)">This template deliberately does <em>not</em> copy the LeadFlow product skin. Indigo studio system for general services.</p>
    <p style="margin-top:12px;color:var(--mute)">Line: <strong style="color:var(--ink)">{p}</strong></p>
  </aside>
</section>
<section class="section">
  <h2>What clients get</h2>
  <p class="sub">Clear modules, product-like spacing, conversion-focused CTA.</p>
  <div class="grid">{cards}</div>
</section>
<section class="tool">
  <div class="k">Engagement size</div>
  <h2 style="font-family:'Sora',sans-serif;font-size:1.4rem;margin:8px 0">Project scale</h2>
  <div class="val" id="v">Medium</div>
  <input type="range" min="1" max="5" value="3" oninput="const m={{1:'Starter',2:'Focused',3:'Medium',4:'Growth',5:'Enterprise'}};document.getElementById('v').textContent=m[this.value]">
  <div style="margin-top:16px"><button class="btn" onclick="openM()">Match me to a plan</button></div>
</section>
<footer>{n} · {c} · {p}</footer>
<div class="modal" id="m"><div class="modal-card">
  <button class="close" onclick="closeM()">×</button>
  <h3 style="font-family:'Sora',serif;font-family:'Sora',sans-serif;margin-bottom:8px">Contact</h3>
  <form onsubmit="event.preventDefault();closeM();alert('Message sent to {n}.');">
    <input placeholder="Name *" required><input placeholder="Phone *" required><input placeholder="What do you need?">
    <button class="btn" style="width:100%;margin-top:8px">Send</button>
  </form>
</div></div>
<script>function openM(){{document.getElementById('m').classList.add('open')}}function closeM(){{document.getElementById('m').classList.remove('open')}}</script>
</body></html>"""


if __name__ == "__main__":
    g = ShadowInfiltrator()
    for args in [
        ("Apex Dental Lounge", "Dental Clinic", "Toronto", "+1 416 555 0199"),
        ("Lumiere Fine Dining", "Restaurant", "Paris", "+33 1 42 68 55 00"),
        ("Vanguard Legal Counsel", "Law Firm", "New York", "+1 212 555 0100"),
        ("Skyline Real Estate", "Real Estate", "Dubai", "+971 4 318 8888"),
        ("Titan Elite Performance Gym", "Gym", "London", "+44 20 5555 0100"),
        ("Aura Aesthetic Spa", "Spa", "Munich", "+49 89 555 0100"),
        ("Royal Crown Fine Jewelry", "Jewelry", "Singapore", "+65 6555 0100"),
        ("Horizon Private Wealth Advisory", "Wealth", "Melbourne", "+61 3 5550 0100"),
    ]:
        r = g.generate_luxury_site(*args)
        print(r["industry_paradigm_applied"], "->", r["live_cloud_demo_url"])
