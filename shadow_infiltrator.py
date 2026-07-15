"""
LeadFlow.AI - Shadow Infiltrator (v8 media + About/Team + lead API)
Creative, profession-specific client websites.

Rules:
- Distinct visual system per industry (NOT LeadFlow product UI clone)
- No neon cyan / cyber glow kitsch
- Deep sections: proof, galleries/SVG art, fee tables, FAQs, process, CTAs
- Design cues informed by skills/ui-ux-pro-max data (colors/styles/typography)
"""

from __future__ import annotations

import os
from typing import Any, Dict, List, Tuple
from cloud_deployer import CloudDeploymentEngine


class ShadowInfiltrator:
    def __init__(self, output_dir: str = None):
        if output_dir is None:
            output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "generated_sites")
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)
        self.deployer = CloudDeploymentEngine(base_output_dir=self.output_dir)

    # ------------------------------------------------------------------ public
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

        kind, html_content, paradigm = self._route(business_name, category, city, phone)

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
            "design_kind": kind,
            "generated_filename": filename,
            "generated_filepath": filepath,
            "live_cloud_demo_url": demo_res["live_cloud_url"],
            "client_handover_zip": pkg_res["handover_zip_path"],
            "custom_domain_configured": custom_domain,
            "upsell_pitch": (
                f"Hi {business_name} team,\n\n"
                f"We prepared a free live website preview designed specifically for your industry in {city}:\n"
                f"{demo_res['live_cloud_url']}\n\n"
                f"Design system: {paradigm}.\n"
                f"If you want ownership + the full deployment ZIP for `{custom_domain}`, we can transfer after payment.\n"
                f"Happy to adjust services, photos, hours, or colors."
            ),
        }

    def _route(self, name: str, category: str, city: str, phone: str):
        blob = f"{(category or '')} {name}".lower()
        if any(w in blob for w in ["dental", "clinic", "doctor", "health", "medical", "vet", "veterinary", "hospital"]):
            return "medical", self._medical(name, category, city, phone), "Healthcare · Trust & Authority + clinical calm"
        if any(w in blob for w in ["restaurant", "dining", "food", "lounge", "bistro", "cafe", "gourmet"]):
            return "dining", self._dining(name, category, city, phone), "Restaurant · Warm nocturnal hospitality storytelling"
        if any(w in blob for w in ["law", "legal", "attorney", "lawyer", "justice", "counsel"]):
            return "legal", self._legal(name, category, city, phone), "Legal · Authority editorial (navy/brass)"
        if any(w in blob for w in ["estate", "realty", "property", "architecture", "builder", "architectural"]):
            return "realty", self._realty(name, category, city, phone), "Property · Architectural magazine + listings"
        if any(w in blob for w in ["gym", "fitness", "performance", "sport", "training"]):
            return "gym", self._gym(name, category, city, phone), "Fitness · Bold athletic conversion layout"
        if any(w in blob for w in ["spa", "aesthetic", "salon", "beauty", "wellness", "sanctuary"]):
            return "spa", self._spa(name, category, city, phone), "Wellness · Organic biophilic sanctuary"
        if any(w in blob for w in ["jewelry", "jewel", "watch", "diamond", "crown"]):
            return "jewelry", self._jewelry(name, category, city, phone), "Jewelry · High-jewelry atelier"
        if any(w in blob for w in ["wealth", "advisory", "finance", "private", "capital", "invest"]):
            return "wealth", self._wealth(name, category, city, phone), "Wealth · Private bank discretion"
        return "universal", self._universal(name, category, city, phone), f"Services · category studio ({(category or 'pro').title()})"

    # ------------------------------------------------------------------ utils
    def _e(self, s: str) -> str:
        return (
            (s or "")
            .replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
            .replace('"', "&quot;")
        )


    def _photo(self, kind: str, w: int = 1200, h: int = 800, sig: int = 1) -> str:
        queries = {
            "medical": "dental,clinic,healthcare",
            "medical2": "dentist,smile,healthcare",
            "vet": "veterinary,clinic,pet",
            "dining": "restaurant,fine-dining,food",
            "dining2": "chef,kitchen,plating",
            "legal": "law,office,library",
            "legal2": "architecture,office,building",
            "realty": "interior,architecture,home",
            "realty2": "apartment,living-room,design",
            "realty3": "house,exterior,architecture",
            "gym": "gym,fitness,training",
            "gym2": "weightlifting,athlete,fitness",
            "spa": "spa,wellness,massage",
            "spa2": "skincare,beauty,spa",
            "jewelry": "jewelry,ring,diamond",
            "jewelry2": "necklace,gold,jewelry",
            "wealth": "office,finance,architecture",
            "wealth2": "skyline,city,office",
            "team": "portrait,professional,business",
            "team2": "team,office,business",
            "universal": "office,workspace,modern",
        }
        q = queries.get(kind, "office,workspace")
        return f"https://loremflickr.com/{w}/{h}/{q}?lock={sig}"

    def _img(self, kind: str, alt: str, w: int = 1200, h: int = 800, sig: int = 1, cls: str = "shot") -> str:
        src = self._photo(kind, w, h, sig)
        return f'<figure class="{cls}"><img src="{src}" alt="{self._e(alt)}" loading="lazy" width="{w}" height="{h}"/></figure>'

    def _ba(self, before_kind: str, after_kind: str, label_before: str, label_after: str, sig: int = 11) -> str:
        b = self._photo(before_kind, 900, 700, sig)
        a = self._photo(after_kind, 900, 700, sig + 7)
        return f"""
<section class="section" id="results">
  <h2>Before / after</h2>
  <p class="lead">Visual proof clients look for - illustrative demo imagery.</p>
  <div class="ba">
    <figure><img src="{b}" alt="{self._e(label_before)}" loading="lazy"/><figcaption>{self._e(label_before)}</figcaption></figure>
    <figure><img src="{a}" alt="{self._e(label_after)}" loading="lazy"/><figcaption>{self._e(label_after)}</figcaption></figure>
  </div>
</section>"""

    def _team(self, members, photo_kind: str = "team") -> str:
        cards = []
        for i, (nm, role, blurb) in enumerate(members, 1):
            src = self._photo(photo_kind, 600, 600, 40 + i)
            cards.append(
                "<article class='card team-card'>"
                f"<img class='avatar' src='{src}' alt='{self._e(nm)}' loading='lazy'/>"
                f"<h3>{self._e(nm)}</h3><div class='role'>{self._e(role)}</div>"
                f"<p>{self._e(blurb)}</p></article>"
            )
        return "<section class='section' id='team'><h2>Team</h2><p class='lead'>The people clients actually meet.</p><div class='grid-3'>" + "".join(cards) + "</div></section>"

    def _about(self, name: str, city: str, body: str, photo_kind: str, sig: int = 3) -> str:
        img = self._img(photo_kind, f"{name} in {city}", 1200, 900, sig, "shot tall")
        return f"""
<section class="section" id="about">
  <div class="grid-2">
    <div>
      <h2>About {self._e(name)}</h2>
      <p class="lead">{self._e(body)}</p>
      <ul class="bullets">
        <li>Based in {self._e(city)}</li>
        <li>Appointment-first operations</li>
        <li>Human follow-up after every inquiry</li>
      </ul>
    </div>
    {img}
  </div>
</section>"""

    def _modal(self, name: str, title: str, fields=None, btn: str = "Send", dark: bool = False, studio: str = "DEMO_SITE") -> str:
        if fields is None:
            fields = []
        n = self._e(name)
        bg = "#141414" if dark else "#fff"
        fg = "#f5f5f5" if dark else "#111"
        border = "rgba(255,255,255,.12)" if dark else "#e5e5e5"
        note_ph = self._e(fields[-1] if fields else "How can we help?")
        btn_e = self._e(btn)
        studio_js = studio.replace("\\", "\\\\").replace("'", "\\'")
        name_js = name.replace("\\", "\\\\").replace("'", "\\'")
        btn_js = btn.replace("\\", "\\\\").replace("'", "\\'")
        return f"""
<div class="modal" id="m" role="dialog" aria-modal="true">
  <div class="modal-card" style="background:{bg};color:{fg};border-color:{border}">
    <button class="close" type="button" onclick="closeM()" aria-label="Close">x</button>
    <h3>{self._e(title)}</h3>
    <p class="muted">Sent to {n}. On LeadFlow host this stores via /api/lead/capture.</p>
    <form id="lead-form" onsubmit="return submitLead(event)">
      <input name="name" placeholder="Full name *" required>
      <input name="email" type="email" placeholder="Email *" required>
      <input name="phone" placeholder="Phone / WhatsApp *" required>
      <input name="company" type="hidden" value="{n}">
      <input name="note" placeholder="{note_ph}">
      <button class="btn primary" id="lead-btn" type="submit" style="width:100%;margin-top:8px">{btn_e}</button>
      <p id="lead-status" class="muted" style="margin-top:10px;font-size:.85rem"></p>
    </form>
  </div>
</div>
<script>
const LEAD_STUDIO = '{studio_js}';
const LEAD_COMPANY = '{name_js}';
function openM(){{document.getElementById('m').classList.add('open');}}
function closeM(){{document.getElementById('m').classList.remove('open');}}
document.addEventListener('keydown',e=>{{if(e.key==='Escape')closeM();}});
async function submitLead(e){{
  e.preventDefault();
  const form = e.target;
  const btn = document.getElementById('lead-btn');
  const status = document.getElementById('lead-status');
  const payload = {{
    email: form.email.value.trim(),
    name: form.name.value.trim(),
    company: form.company.value.trim() || LEAD_COMPANY,
    studio_source: LEAD_STUDIO + (form.note.value ? (':' + form.note.value.slice(0,80)) : '')
  }};
  btn.disabled = true; btn.textContent = 'Sending...'; status.textContent = '';
  try {{
    const res = await fetch('/api/lead/capture', {{
      method: 'POST',
      headers: {{'Content-Type': 'application/json'}},
      body: JSON.stringify(payload)
    }});
    if(res.ok){{
      status.textContent = 'Request received. We will follow up shortly.';
      form.reset();
      setTimeout(()=>{{closeM(); btn.disabled=false; btn.textContent='{btn_js}'; status.textContent='';}}, 1200);
    }} else {{
      throw new Error('API ' + res.status);
    }}
  }} catch (err) {{
    status.textContent = 'Demo note: lead API works on LeadFlow host. UI confirmation saved.';
    console.warn('lead capture', err);
    setTimeout(()=>{{closeM(); btn.disabled=false; btn.textContent='{btn_js}'; status.textContent='';}}, 1500);
  }}
  return false;
}}
</script>"""

    def _faq(self, pairs: List[Tuple[str, str]]) -> str:
        parts = []
        for q, a in pairs:
            parts.append(
                f"<details class='faq'><summary>{self._e(q)}</summary><p>{self._e(a)}</p></details>"
            )
        return "\n".join(parts)

    def _steps(self, items: List[Tuple[str, str]]) -> str:
        out = []
        for i, (t, d) in enumerate(items, 1):
            out.append(
                f"<div class='step'><div class='num'>{i:02d}</div><div><h4>{self._e(t)}</h4><p>{self._e(d)}</p></div></div>"
            )
        return "\n".join(out)

    def _base_css_common(self) -> str:
        return """
*{box-sizing:border-box;margin:0;padding:0}
img,svg{display:block;max-width:100%}
button,input,select,textarea{font:inherit}
.muted{opacity:.78}
.wrap{width:min(1120px,92vw);margin:0 auto}
.grid-3{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
.grid-2{display:grid;grid-template-columns:1.1fr .9fr;gap:22px;align-items:center}
@media(max-width:900px){.grid-3,.grid-2{grid-template-columns:1fr}}
.section{padding:72px 0}
.section h2{font-size:clamp(1.6rem,3vw,2.2rem);line-height:1.15;margin-bottom:10px}
.section .lead{max-width:40rem;margin-bottom:26px}
.card{padding:22px;border-radius:18px}
.card h3{font-size:1.1rem;margin-bottom:8px}
.card p{font-size:.95rem;line-height:1.65}
.pill{display:inline-flex;align-items:center;gap:8px;padding:6px 12px;border-radius:999px;font-size:.75rem;font-weight:700;letter-spacing:.04em;text-transform:uppercase}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:8px;border:0;cursor:pointer;text-decoration:none;padding:12px 18px;border-radius:999px;font-weight:700}
.btn.ghost{background:transparent}
.actions{display:flex;flex-wrap:wrap;gap:12px}
.nav{position:sticky;top:0;z-index:30;display:flex;justify-content:space-between;align-items:center;padding:16px 4vw;backdrop-filter:blur(12px)}
.logo{font-weight:700;text-decoration:none}
.footer{padding:42px 4vw;text-align:center;font-size:.92rem}
.modal{display:none;position:fixed;inset:0;background:rgba(0,0,0,.5);align-items:center;justify-content:center;padding:18px;z-index:80}
.modal.open{display:flex}
.modal-card{width:min(460px,100%);padding:26px;border-radius:18px;border:1px solid;position:relative}
.modal-card h3{font-size:1.35rem;margin-bottom:6px}
.modal-card input,.modal-card select,.modal-card textarea{width:100%;margin:8px 0;padding:12px 14px;border-radius:12px;border:1px solid #d4d4d8;background:#fff}
.modal-card .close{position:absolute;right:12px;top:8px;border:0;background:none;font-size:1.4rem;cursor:pointer;opacity:.7}
.faq{border:1px solid;border-radius:14px;padding:14px 16px;margin:10px 0;background:transparent}
.faq summary{cursor:pointer;font-weight:700}
.faq p{margin-top:8px;opacity:.8}
.step{display:flex;gap:14px;padding:14px 0;border-bottom:1px solid rgba(0,0,0,.06)}
.step .num{font-weight:800;opacity:.45;min-width:2.2rem}
.table{width:100%;border-collapse:collapse;font-size:.95rem}
.table th,.table td{padding:12px 10px;border-bottom:1px solid rgba(0,0,0,.08);text-align:left;vertical-align:top}
.quote{padding:22px;border-radius:18px;font-size:1.05rem;line-height:1.6}
.gallery{display:grid;grid-template-columns:1.3fr 1fr;gap:12px}
@media(max-width:900px){.gallery{grid-template-columns:1fr}}
.g-main,.g-side{border-radius:20px;min-height:180px;overflow:hidden}
.tool{padding:28px;border-radius:22px;text-align:center}
.tool .val{font-size:clamp(1.6rem,3vw,2.2rem);font-weight:700;margin:12px 0}
input[type=range]{width:min(100%,420px)}

.shot{margin:0;border-radius:20px;overflow:hidden}
.shot img{width:100%;height:100%;object-fit:cover;display:block}
.shot.tall img{min-height:280px}
.ba{display:grid;grid-template-columns:1fr 1fr;gap:14px}
@media(max-width:800px){.ba{grid-template-columns:1fr}}
.ba figure{margin:0;border-radius:18px;overflow:hidden;background:rgba(0,0,0,.03)}
.ba img{width:100%;height:260px;object-fit:cover;display:block}
.ba figcaption{padding:10px 12px;font-size:.85rem;font-weight:700}
.team-card{text-align:center}
.team-card .avatar{width:96px;height:96px;border-radius:50%;object-fit:cover;margin:0 auto 12px}
.team-card .role{font-size:.8rem;font-weight:700;letter-spacing:.04em;text-transform:uppercase;opacity:.7;margin-bottom:8px}
.bullets{margin:14px 0 0 1.1rem;line-height:1.8}
.subnav{display:flex;flex-wrap:wrap;gap:10px 14px;font-size:.86rem;align-items:center}
.subnav a{text-decoration:none;opacity:.85}
.subnav a:hover{opacity:1}
"""

    # ================================================================= MEDICAL
    def _medical(self, name: str, cat: str, city: str, phone: str) -> str:
        n, c, p = self._e(name), self._e(city), self._e(phone)
        is_vet = any(w in f"{cat} {name}".lower() for w in ["vet", "veterinary"])
        hero_h = "Care that feels calm, clear, and human" if not is_vet else "Compassionate care for the animals you love"
        svc = [
            ("Diagnostics", "Digital imaging, clear explanations, no rushed consults."),
            ("Restorative / treatment", "Plans built around comfort and long-term outcomes."),
            ("Prevention", "Recalls and maintenance that keep care simple."),
            ("Emergency desk", "Priority pathways when something can’t wait."),
            ("Family continuity", "Notes that follow the patient — not lost in chats."),
            ("Aftercare", "Written instructions you can actually follow at home."),
        ]
        if is_vet:
            svc[0] = ("Wellness exams", "Gentle exams with time for owner questions.")
            svc[3] = ("Urgent cases", "Same-day triage when pets need faster attention.")
        cards = "".join(f"<article class='card'><h3>{self._e(t)}</h3><p>{self._e(d)}</p></article>" for t, d in svc)
        faq = self._faq([
            ("Do you accept new patients?", f"Yes — {n} welcomes new patients in {c} most weeks. Request a slot and we’ll confirm availability."),
            ("How long is a first visit?", "Typically 30–45 minutes so we can listen, examine, and map options without rushing."),
            ("Is financing available?", "We can discuss phased treatment plans. Mention budget constraints during booking."),
            ("Where are you located?", f"Serving patients across {c}. Exact suite details are confirmed on booking."),
        ])
        steps = self._steps([
            ("Tell us what you need", "Share symptoms, goals, or a photo if relevant."),
            ("We confirm a slot", "You’ll get a clear time window and prep notes."),
            ("Visit + plan", "Exam, options, and pricing transparency before treatment."),
        ])
        art = """
<svg viewBox="0 0 640 420" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Clinical illustration">
  <defs>
    <linearGradient id="mg" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#E8F7F4"/><stop offset="1" stop-color="#D5EEEA"/></linearGradient>
  </defs>
  <rect width="640" height="420" rx="32" fill="url(#mg)"/>
  <circle cx="470" cy="120" r="70" fill="#B7E2DA"/>
  <rect x="70" y="80" width="280" height="240" rx="28" fill="#fff" stroke="#C9E5DF" stroke-width="2"/>
  <rect x="100" y="120" width="160" height="14" rx="7" fill="#2F6F68"/>
  <rect x="100" y="150" width="200" height="10" rx="5" fill="#D7E5E1"/>
  <rect x="100" y="175" width="180" height="10" rx="5" fill="#D7E5E1"/>
  <rect x="100" y="210" width="90" height="40" rx="20" fill="#2F6F68"/>
  <circle cx="480" cy="270" r="54" fill="#fff" stroke="#2F6F68" stroke-width="6"/>
  <path d="M455 270h50M480 245v50" stroke="#2F6F68" stroke-width="8" stroke-linecap="round"/>
</svg>"""
        return f"""<!DOCTYPE html>
<html lang="en"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{n} · {c}</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Fraunces:opsz,wght@9..144,500;9..144,700&display=swap');
{self._base_css_common()}
:root{{--bg:#F7FBFA;--ink:#16302B;--mute:#5B726C;--line:#D7E5E1;--sea:#0F766E;--soft:#E4F3F0;--sand:#FFF9F2}}
body{{font-family:'DM Sans',sans-serif;background:var(--bg);color:var(--ink);line-height:1.7}}
.nav{{background:rgba(247,251,250,.92);border-bottom:1px solid var(--line)}}
.logo{{font-family:'Fraunces',serif;font-size:1.35rem;color:var(--ink)}}
.btn.primary{{background:var(--sea);color:#fff}}
.btn.ghost{{border:1px solid var(--line);color:var(--sea);background:var(--soft)}}
.pill{{background:var(--soft);color:var(--sea)}}
h1,h2,h3,h4{{font-family:'Fraunces',serif;font-weight:700}}
.hero{{padding:56px 0 24px}}
.side{{background:linear-gradient(160deg,var(--sand),#fff);border:1px solid var(--line);border-radius:28px;padding:22px}}
.metric{{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:14px}}
.metric div{{background:#fff;border:1px solid var(--line);border-radius:16px;padding:14px}}
.metric strong{{display:block;font-family:'Fraunces',serif;font-size:1.5rem}}
.metric span{{color:var(--mute);font-size:.8rem}}
.card{{background:#fff;border:1px solid var(--line)}}
.quote{{background:#fff;border:1px solid var(--line)}}
.tool{{background:#fff;border:1px solid var(--line)}}
.tool .val{{color:var(--sea);font-family:'Fraunces',serif}}
.faq{{border-color:var(--line);background:#fff}}
.table th{{color:var(--mute);font-size:.8rem;text-transform:uppercase;letter-spacing:.04em}}
.footer{{background:#fff;border-top:1px solid var(--line);color:var(--mute)}}
.lead,.card p,.section .lead{{color:var(--mute)}}
input[type=range]{{accent-color:var(--sea)}}
</style></head><body>
<nav class="nav"><a class="logo" href="#">{n}</a><div class="actions subnav">
<a href="#about">About</a><a href="#services">Services</a><a href="#results">Results</a><a href="#team">Team</a><a href="#process">Visit</a>
<button class="btn primary" onclick="openM()">Book visit</button></div></nav>
<main class="wrap">
  <section class="hero grid-2">
    <div>
      <div class="pill">Healthcare · {c}</div>
      <h1 style="font-size:clamp(2.2rem,4.5vw,3.4rem);line-height:1.1;margin:12px 0 14px">{hero_h}</h1>
      <p class="lead">{n} combines modern clinical standards with a calmer patient experience — clear language, transparent options, and a booking path that doesn’t feel like a call center.</p>
      <div class="actions">
        <button class="btn primary" onclick="openM()">Request appointment</button>
        <a class="btn ghost" href="#process">How visits work</a>
      </div>
    </div>
    <aside class="side">
      {self._img("vet" if is_vet else "medical", n + " clinic", 1000, 780, 21, "shot")}
      <div class="metric">
        <div><strong>4.9</strong><span>avg. rating</span></div>
        <div><strong>15m</strong><span>on-time goal</span></div>
      </div>
      <p class="muted" style="margin-top:12px;font-size:.92rem">Direct line: <strong style="color:var(--ink)">{p}</strong></p>
    </aside>
  </section>

  <section class="section" id="services">
    <h2>Services designed around comfort</h2>
    <p class="lead">Healthcare UX: high readability, soft teal trust palette, obvious next step — patients scan under stress.</p>
    <div class="grid-3">{cards}</div>
  </section>

  {self._about(name, city, f"{name} is a modern practice in {city} focused on clear communication, gentle care, and transparent options before treatment.", "medical2" if not is_vet else "vet", 5)}
  {self._ba("medical", "medical2", "Before consult planning", "After restorative / whitening plan", 12 if not is_vet else 19)}
  {self._team([
    ("Dr. Maya Chen", "Lead clinician", "Treatment planning and complex restorative cases."),
    ("Jordan Lee", "Patient coordinator", "Booking, insurance questions, and visit prep."),
    ("Sam Ortiz", "Hygiene lead", "Prevention programs and recall systems."),
  ], "team")}
  <section class="section" id="process">
    <h2>Your first visit, simplified</h2>
    <p class="lead">A predictable path reduces anxiety more than any animation ever will.</p>
    <div class="card" style="background:#fff;border:1px solid var(--line)">{steps}</div>
  </section>

  <section class="section">
    <div class="tool">
      <div class="pill">Interactive preview</div>
      <h2 style="margin-top:10px">Treatment brightness planner</h2>
      <p class="lead" style="margin:8px auto 0">A conversation starter for whitening goals — not a medical claim.</p>
      <div class="val" id="v">70% brighter target</div>
      <input type="range" min="20" max="100" value="70" oninput="document.getElementById('v').textContent=this.value+'% brighter target'">
      <div style="margin-top:14px"><button class="btn primary" onclick="openM()">Discuss this plan</button></div>
    </div>
  </section>

  <section class="section grid-2">
    <div>
      <h2>What patients say</h2>
      <div class="quote" style="margin-top:14px">“They explained every option before I felt pushed into treatment. The room felt calm — not clinical-cold.”<br><strong style="display:block;margin-top:10px;color:var(--ink)">— M. R., {c}</strong></div>
      <div class="quote" style="margin-top:12px">“Booking was simple and the follow-up notes were actually useful.”<br><strong style="display:block;margin-top:10px;color:var(--ink)">— A. K., {c}</strong></div>
    </div>
    <div>
      <h2>Transparent fee examples</h2>
      <p class="lead">Illustrative ranges for planning conversations — confirmed after exam.</p>
      <table class="table">
        <tr><th>Service</th><th>From</th></tr>
        <tr><td>New patient exam</td><td>$89</td></tr>
        <tr><td>Hygiene / cleaning visit</td><td>$120</td></tr>
        <tr><td>Whitening package</td><td>$350</td></tr>
        <tr><td>Custom treatment plan</td><td>Quoted after consult</td></tr>
      </table>
    </div>
  </section>

  <section class="section">
    <h2>FAQ</h2>
    {faq}
  </section>
</main>
<footer class="footer"><strong style="color:var(--ink);font-family:'Fraunces',serif;font-size:1.2rem">{n}</strong><br>{c} · {p}</footer>
{self._modal(name, "Request a visit", ["Full name *", "Phone *", "Preferred time window", "Notes (optional)"], "Send request", studio="MEDICAL_DEMO")}
</body></html>"""

    # ================================================================= DINING
    def _dining(self, name: str, cat: str, city: str, phone: str) -> str:
        n, c, p = self._e(name), self._e(city), self._e(phone)
        menu = [
            ("01 · Raw", "Wagyu tartare", "Black garlic, cured yolk, crisp shallot."),
            ("02 · Fire", "Coal-grilled catch", "Citrus beurre, herb oil, charred lemon."),
            ("03 · Slow", "Short rib glaze", "Root vegetables, bone jus, pickled mustard."),
            ("04 · Green", "Market leaves", "Seasonal crunch, aged vinegar, seeds."),
            ("05 · Sweet", "Dark chocolate pave", "Olive oil, sea salt, cacao nib."),
            ("06 · Pour", "Sommelier pairing", "Three glasses matched to the kitchen."),
        ]
        menu_html = "".join(
            f"<article class='card'><div class='k'>{self._e(k)}</div><h3>{self._e(t)}</h3><p>{self._e(d)}</p></article>"
            for k, t, d in menu
        )
        faq = self._faq([
            ("Do you take walk-ins?", "Limited bar seats some nights. Reservations are recommended for the dining room."),
            ("Can you host private events?", f"Yes — {n} offers private dining for celebrations and client dinners."),
            ("Dietary needs?", "We accommodate vegetarian and most allergies with advance notice."),
        ])
        art = """
<svg viewBox="0 0 800 360" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
  <rect width="800" height="360" fill="#1C1816"/>
  <circle cx="160" cy="220" r="90" fill="#2A201C"/>
  <circle cx="160" cy="220" r="55" fill="#3A2A22"/>
  <circle cx="400" cy="150" r="8" fill="#C45C26" opacity=".9"/>
  <circle cx="460" cy="190" r="5" fill="#D8B56A" opacity=".7"/>
  <circle cx="520" cy="130" r="6" fill="#C45C26" opacity=".55"/>
  <circle cx="580" cy="210" r="7" fill="#D8B56A" opacity=".5"/>
  <path d="M300 280 C420 200, 520 320, 700 240" stroke="#C45C26" stroke-width="2" fill="none" opacity=".35"/>
  <text x="300" y="90" fill="#D8B56A" font-family="Georgia, serif" font-size="28">Evening service</text>
</svg>"""
        return f"""<!DOCTYPE html>
<html lang="en"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{n} · {c}</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500&family=Outfit:wght@300;400;500;600&display=swap');
{self._base_css_common()}
:root{{--bg:#14110F;--panel:#1C1816;--ink:#F4EFE6;--mute:#B7A99A;--line:rgba(244,239,230,.12);--ember:#C45C26;--gold:#D8B56A}}
body{{font-family:'Outfit',sans-serif;background:var(--bg);color:var(--ink);line-height:1.75;font-weight:300}}
.nav{{background:rgba(20,17,15,.9);border-bottom:1px solid var(--line)}}
.logo{{font-family:'Cormorant Garamond',serif;font-size:1.7rem;color:var(--ink);letter-spacing:.03em}}
.btn.primary{{background:var(--ember);color:#fff;border-radius:0;text-transform:uppercase;letter-spacing:.08em;font-size:.72rem}}
.btn.ghost{{border:1px solid var(--line);color:var(--ink);border-radius:0}}
.pill,.k{{color:var(--gold);letter-spacing:.22em;text-transform:uppercase;font-size:.7rem;font-weight:600}}
h1,h2,h3{{font-family:'Cormorant Garamond',serif;font-weight:500}}
.hero{{min-height:78vh;display:grid;place-items:center;text-align:center;padding:90px 4vw;background:radial-gradient(ellipse at 50% 0%,rgba(196,92,38,.22),transparent 55%),linear-gradient(180deg,#1a1512,#14110F 70%)}}
.card{{background:var(--panel);border:1px solid var(--line);border-radius:0}}
.card h3{{font-size:1.45rem;color:var(--gold)}}
.card p,.lead,.muted{{color:var(--mute)}}
.tool{{background:var(--panel);border:1px solid var(--line);border-radius:0}}
.tool .val{{color:var(--gold);font-family:'Cormorant Garamond',serif;font-weight:500}}
.faq{{border-color:var(--line)}}
.footer{{border-top:1px solid var(--line);color:var(--mute)}}
.quote{{background:var(--panel);border:1px solid var(--line);border-radius:0}}
.step{{border-bottom:1px solid var(--line)}}
input[type=range]{{accent-color:var(--ember)}}
.modal-card input{{background:#14110F;border-color:var(--line);color:var(--ink)}}
</style></head><body>
<nav class="nav"><a class="logo" href="#">{n}</a><div class="actions subnav">
<a href="#about">About</a><a href="#menu">Menu</a><a href="#team">Team</a><a href="#hours">Hours</a>
<button class="btn primary" onclick="openM()">Reserve</button></div></nav>
<section class="hero">
  <div class="wrap">
    <div class="k">Dining room · {c}</div>
    <h1 style="font-size:clamp(2.8rem,7vw,5rem);line-height:1.05;margin:14px 0 16px">An evening of <em style="color:var(--gold);font-style:italic">fire, craft & quiet luxury</em></h1>
    <p class="lead" style="margin:0 auto 26px">{n} is a warm nocturnal room — ember light, considered pacing, plates built for memory.</p>
    <div class="actions" style="justify-content:center">
      <button class="btn primary" onclick="openM()">Request a table</button>
      <a class="btn ghost" href="#menu">View tasting notes</a>
    </div>
  </div>
</section>
<main class="wrap">
  <section class="section" style="padding-top:40px">
    <div class="gallery">
      {self._img("dining", n + " dining room", 1200, 800, 31, "shot g-main")}
      <div>
        {self._img("dining2", "Kitchen craft", 800, 390, 32, "shot g-side")}
        <div style="height:12px"></div>
        {self._img("dining", "Plating detail", 800, 390, 33, "shot g-side")}
      </div>
    </div>
  </section>
  {self._about(name, city, f"{name} is a reservation-led dining room in {city} - paced service, seasonal plates, and a cellar that supports the kitchen.", "dining2", 8)}

  <section class="section" id="menu">
    <h2 style="text-align:center">Tasting notes</h2>
    <p class="lead" style="text-align:center;margin-left:auto;margin-right:auto">A kitchen-led sequence — not a laminated tourist menu.</p>
    <div class="grid-3">{menu_html}</div>
  </section>
  <section class="section grid-2">
    <div>
      <h2>Private dining</h2>
      <p class="lead">For birthdays, closings, and the dinners that need a quieter room.</p>
      <div class="quote">“The pacing was perfect — we never felt rushed, and the wine pairings actually supported the food.”<br><strong style="color:var(--ink)">— Guest review, {c}</strong></div>
    </div>
    <div class="tool">
      <div class="k">Estimator</div>
      <h2 style="font-size:1.8rem;margin:8px 0">Guest count</h2>
      <div class="val" id="v">12 guests · ~$4,560</div>
      <input type="range" min="2" max="40" value="12" oninput="document.getElementById('v').textContent=this.value+' guests · ~$'+(this.value*380).toLocaleString()">
      <div style="margin-top:14px"><button class="btn primary" onclick="openM()">Hold a private room</button></div>
    </div>
  </section>
  {self._team([
    ("Elena Moreau", "Executive chef", "Menu architecture and fire cooking."),
    ("Marco Bell", "Sommelier", "Pairings that support the plate."),
    ("Aya Nouri", "Front of house", "Reservations and private dining."),
  ], "team2")}
  <section class="section">
    <h2 id="hours">Hours & contact</h2>
    <table class="table" style="color:var(--ink)">
      <tr><td style="color:var(--mute)">Tue–Thu</td><td>17:30 – 22:30</td></tr>
      <tr><td style="color:var(--mute)">Fri–Sat</td><td>17:00 – 23:30</td></tr>
      <tr><td style="color:var(--mute)">Sunday</td><td>Chef’s table only</td></tr>
      <tr><td style="color:var(--mute)">Reservations</td><td>{p}</td></tr>
    </table>
  </section>
  <section class="section"><h2>FAQ</h2>{faq}</section>
</main>
<footer class="footer">{n} · {c} · {p}</footer>
{self._modal(name, "Table request", ["Name *", "Phone *", "Date / time preference", "Party size"], "Send", dark=True, studio="DINING_DEMO")}
</body></html>"""

    # ================================================================= LEGAL
    def _legal(self, name: str, cat: str, city: str, phone: str) -> str:
        n, c, p = self._e(name), self._e(city), self._e(phone)
        practices = [
            ("Corporate disputes", "Shareholder, partnership, and contract litigation with disciplined prep."),
            ("Commercial counsel", "Agreements and negotiations before conflict becomes expensive."),
            ("Intellectual property", "Brand, trade secret, and infringement matters."),
            ("Executive matters", "Sensitive issues handled with discretion."),
            ("Cross-border", "Multi-jurisdiction coordination when the file isn’t local-only."),
            ("Settlement strategy", "Leverage mapping — not performative aggression."),
        ]
        cards = "".join(f"<article class='card'><h3>{self._e(t)}</h3><p>{self._e(d)}</p></article>" for t, d in practices)
        steps = self._steps([
            ("Confidential intake", "We scope the matter and conflicts check."),
            ("Case architecture", "Facts, risks, leverage, and options in plain language."),
            ("Execution", "Negotiation or litigation with measured updates."),
        ])
        faq = self._faq([
            ("Is the first conversation privileged?", "We treat initial inquiries as confidential. Formal engagement terms are confirmed in writing."),
            ("Do you work on contingency?", "Depends on matter type. Fee structure is discussed after intake."),
            ("How fast can you start?", f"{n} typically responds within one business day in {c}."),
        ])
        return f"""<!DOCTYPE html>
<html lang="en"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{n} · Counsel · {c}</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Libre+Baskerville:ital,wght@0,400;0,700;1,400&family=Source+Sans+3:wght@400;600;700&display=swap');
{self._base_css_common()}
:root{{--bg:#F7F4EF;--ink:#1B1A17;--mute:#6B6560;--line:#E4DDD2;--navy:#1E3A8A;--brass:#B45309}}
body{{font-family:'Source Sans 3',sans-serif;background:var(--bg);color:var(--ink)}}
.nav{{background:#FFFEFB;border-bottom:1px solid var(--line)}}
.logo{{font-family:'Libre Baskerville',serif;font-size:1.05rem;letter-spacing:.12em;text-transform:uppercase;color:var(--navy)}}
.btn.primary{{background:var(--navy);color:#fff;border-radius:0}}
.btn.ghost{{border:1px solid var(--navy);color:var(--navy);border-radius:0;background:transparent}}
.pill{{background:transparent;color:var(--brass);border:0;padding:0;letter-spacing:.16em}}
h1,h2,h3,h4{{font-family:'Libre Baskerville',serif;color:var(--navy);font-weight:700}}
.hero{{padding:70px 0;background:#FFFEFB;border-bottom:1px solid var(--line)}}
.card{{background:#FFFEFB;border:1px solid var(--line);border-radius:0}}
.card p,.lead,.muted{{color:var(--mute)}}
.panel{{border:1px solid var(--line);background:var(--bg);padding:24px}}
.tool{{background:#FFFEFB;border:1px solid var(--line);border-radius:0}}
.tool .val{{color:var(--brass);font-family:'Libre Baskerville',serif}}
.faq{{border-color:var(--line);background:#FFFEFB;border-radius:0}}
.footer{{background:var(--navy);color:#C9C4B8}}
.quote{{background:#FFFEFB;border:1px solid var(--line);border-radius:0}}
input[type=range]{{accent-color:var(--navy)}}
.seal{{width:120px;height:120px;border:2px solid var(--brass);border-radius:50%;display:grid;place-items:center;margin:0 auto 12px;font-family:'Libre Baskerville',serif;color:var(--brass);text-align:center;font-size:.75rem;letter-spacing:.08em}}
</style></head><body>
<nav class="nav"><a class="logo" href="#">{n}</a><div class="actions subnav">
<a href="#about">About</a><a href="#practice">Practice</a><a href="#team">Team</a>
<button class="btn primary" onclick="openM()">Consultation</button></div></nav>
<main class="wrap">
  <section class="hero grid-2">
    <div>
      <div class="pill">Counsel · {c}</div>
      <h1 style="font-size:clamp(2rem,4vw,3.1rem);line-height:1.2;margin:12px 0 16px">Advocacy with composure. Strategy without theatrics.</h1>
      <p class="lead">{n} represents clients who value preparation, discretion, and direct communication — not billboard bravado.</p>
      <div class="actions">
        <button class="btn primary" onclick="openM()">Schedule evaluation</button>
        <a class="btn ghost" href="#practice">Practice areas</a>
      </div>
    </div>
    <aside class="panel">
      {self._img("legal", n + " counsel", 900, 700, 71, "shot")}
      <h3 style="margin:14px 0 8px">Privileged first conversation</h3>
      <p class="muted">Direct line: <strong style="color:var(--ink)">{p}</strong></p>
      <p class="muted" style="margin-top:10px;font-size:.92rem">Authority editorial - paper, brass, navy.</p>
    </aside>
  </section>

  {self._about(name, city, f"{name} advises and represents clients in {city} with disciplined preparation and discreet handling of complex commercial matters.", "legal2", 16)}
  <section class="section" id="practice">
    <h2>Practice focus</h2>
    <p class="lead">Structured for authority: long-form readability, serif headlines, zero gimmicks.</p>
    <div class="grid-3">{cards}</div>
  </section>
  {self._team([
    ("Helen Ward", "Managing partner", "Complex commercial disputes."),
    ("James Okonkwo", "Counsel", "Contracts and negotiations."),
    ("Priya Shah", "Associate", "Research, filings, case architecture."),
  ], "team")}

  <section class="section grid-2">
    <div>
      <h2>How engagement works</h2>
      <div class="card">{steps}</div>
    </div>
    <div class="tool">
      <div class="pill">Matter scale</div>
      <h2 style="font-size:1.45rem;margin:8px 0">Confidential range</h2>
      <div class="val" id="v">$1,500,000 matter scale</div>
      <input type="range" min="100000" max="10000000" step="100000" value="1500000" oninput="document.getElementById('v').textContent='$'+parseInt(this.value).toLocaleString()+' matter scale'">
      <div style="margin-top:14px"><button class="btn primary" onclick="openM()">Begin inquiry</button></div>
    </div>
  </section>

  <section class="section">
    <h2>Selected commentary</h2>
    <div class="quote">“They translated a messy commercial dispute into a clear decision tree. No theatrics — just leverage and timing.”<br><strong style="color:var(--navy)">— General Counsel, {c}</strong></div>
  </section>

  <section class="section"><h2>FAQ</h2>{faq}</section>
</main>
<footer class="footer">{n}<br>{c} · {p}</footer>
{self._modal(name, "Confidential inquiry", ["Name *", "Phone *", "Brief matter summary", "Company (optional)"], "Submit", studio="LEGAL_DEMO")}
</body></html>"""

    # ================================================================= REALTY
    def _realty(self, name: str, cat: str, city: str, phone: str) -> str:
        n, c, p = self._e(name), self._e(city), self._e(phone)
        listings = [
            ("Skyline residence", "$4.5M", "Stone kitchen, evening terrace, private lift lobby."),
            ("Waterfront house", "$7.2M", "Dock access, garden rooms, quiet morning light."),
            ("Courtyard loft", "$1.9M", "Double-height volume, raw timber, city quiet."),
        ]
        list_html = "".join(
            f"<article class='card listing'><div class='photo' style=\"background-image:url('{self._photo(pk, 900, 700, 60+i)}')\"></div><div class='meta'><h3>{self._e(t)}</h3><div class='price'>{self._e(pr)}</div><p>{self._e(d)}</p></div></article>"
            for i, ((t, pr, d), pk) in enumerate(zip(listings, ["realty", "realty2", "realty3"]), 1)
        )
        faq = self._faq([
            ("Do you handle off-market?", f"Yes. {n} maintains a private shortlist for qualified buyers."),
            ("Buyer or seller focused?", "Both — search advisory and discreet sale strategy."),
            ("International clients?", f"We regularly coordinate remote viewings for {c} inventory."),
        ])
        return f"""<!DOCTYPE html>
<html lang="en"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{n} · {c}</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Manrope:wght@400;500;600;700&display=swap');
{self._base_css_common()}
:root{{--bg:#F3EFE7;--ink:#1C1916;--mute:#6F675E;--line:#DDD4C6;--forest:#0F766E;--clay:#A56B45}}
body{{font-family:'Manrope',sans-serif;background:var(--bg);color:var(--ink)}}
.nav{{position:absolute;left:0;right:0;top:0;background:transparent;color:#fff;border:0}}
.nav .logo{{color:#fff;font-family:'Instrument Serif',serif;font-size:1.6rem;font-weight:400}}
.btn.primary{{background:#fff;color:var(--ink);border-radius:0}}
.btn.dark{{background:var(--forest);color:#fff;border-radius:0}}
.hero{{min-height:82vh;display:flex;align-items:flex-end;padding:0 6vw 70px;color:#fff;background:
 linear-gradient(180deg,rgba(28,25,22,.12),rgba(28,25,22,.78)),
 url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='1600' height='1000'><defs><linearGradient id='g' x1='0' y1='0' x2='1' y2='1'><stop stop-color='%233a4d3f'/><stop offset='1' stop-color='%237a5a3a'/></linearGradient></defs><rect width='100%25' height='100%25' fill='url(%23g)'/><rect x='10%25' y='42%25' width='36%25' height='30%25' fill='%2300000022'/><circle cx='72%25' cy='28%25' r='200' fill='%23ffffff10'/></svg>");
 background-size:cover}}
.hero h1{{font-family:'Instrument Serif',serif;font-weight:400;font-size:clamp(2.6rem,6vw,4.5rem);line-height:1.05;max-width:14ch;margin:10px 0 14px}}
.hero p{{max-width:34rem;opacity:.92;margin-bottom:18px}}
.k{{letter-spacing:.2em;text-transform:uppercase;font-size:.72rem;opacity:.85}}
h2,h3{{font-family:'Instrument Serif',serif;font-weight:400}}
.card{{background:#fff;border:1px solid var(--line);border-radius:0;padding:0;overflow:hidden}}
.listing .photo{{min-height:190px;background-size:cover;background-position:center}}
.listing .meta{{padding:18px}}
.price{{font-family:'Instrument Serif',serif;font-size:1.6rem;color:var(--forest);margin:6px 0}}
.card p,.lead,.muted{{color:var(--mute)}}
.tool{{background:#fff;border:1px solid var(--line);border-radius:0}}
.tool .val{{color:var(--clay);font-family:'Instrument Serif',serif;font-weight:400}}
.faq{{border-color:var(--line);background:#fff;border-radius:0}}
.footer{{border-top:1px solid var(--line);color:var(--mute)}}
input[type=range]{{accent-color:var(--forest)}}
</style></head><body>
<nav class="nav"><a class="logo" href="#">{n}</a><div class="actions subnav">
<a href="#about" style="color:#fff">About</a><a href="#listings" style="color:#fff">Listings</a><a href="#team" style="color:#fff">Team</a>
<button class="btn primary" onclick="openM()">Book showing</button></div></nav>
<section class="hero">
  <div>
    <div class="k">Property · {c}</div>
    <h1>Spaces with architecture, light, and long views</h1>
    <p>{n} curates residences and investments for buyers who care about proportion and materials — not listing spam.</p>
    <button class="btn dark" onclick="openM()">Request private shortlist</button>
  </div>
</section>
<main class="wrap">
  {self._about(name, city, f"{name} is a property desk in {city} for buyers who care about light, materials, and long-term livability - not spammy listing farms.", "realty2", 14)}
  <section class="section" id="listings">
    <h2>Selected inventory</h2>
    <p class="lead">Magazine layout with real photography fields - architecture first.</p>
    <div class="grid-3">{list_html}</div>
  </section>
  {self._team([
    ("Ava Brooks", "Principal advisor", "Buyer strategy and off-market access."),
    ("Noah Patel", "Listing specialist", "Presentation and discreet sale process."),
    ("Mia Costa", "Client ops", "Showings, logistics, paperwork."),
  ], "team2")}
  <section class="section grid-2">
    <div>
      <h2>Neighborhood intelligence</h2>
      <p class="lead">We brief on light, noise, school zones, and resale texture — not just square meters.</p>
      <div class="card" style="padding:18px">
        <h3>Desk</h3>
        <p>Advisory line: <strong style="color:var(--ink)">{p}</strong></p>
        <p style="margin-top:8px">Typical response window: same business day in {c}.</p>
      </div>
    </div>
    <div class="tool">
      <div class="k" style="color:var(--mute)">Yield sketch</div>
      <h2 style="font-size:1.8rem;margin:8px 0">Purchase → annual yield</h2>
      <div class="val" id="v">$2,500,000 · ~$212,500 / yr</div>
      <input type="range" min="500000" max="12000000" step="100000" value="2500000" oninput="const y=Math.round(this.value*0.085);document.getElementById('v').textContent='$'+parseInt(this.value).toLocaleString()+' · ~$'+y.toLocaleString()+' / yr'">
      <div style="margin-top:14px"><button class="btn dark" onclick="openM()">Talk to an advisor</button></div>
    </div>
  </section>
  <section class="section">
    <h2>Process</h2>
    {self._steps([
      ("Brief", "Lifestyle, budget, must-haves, deal-breakers."),
      ("Shortlist", "3–7 properties with honest tradeoffs."),
      ("Showing + offer", "Quiet logistics and negotiation support."),
    ])}
  </section>
  <section class="section"><h2>FAQ</h2>{faq}</section>
</main>
<footer class="footer">{n} · {c} · {p}</footer>
{self._modal(name, "Showing request", ["Name *", "Phone *", "Budget window", "Must-haves"], "Submit", studio="REALTY_DEMO")}
</body></html>"""

    # ================================================================= GYM
    def _gym(self, name: str, cat: str, city: str, phone: str) -> str:
        n, c, p = self._e(name), self._e(city), self._e(phone)
        cards = "".join(
            f"<article class='card'><h3>{self._e(t)}</h3><p>{self._e(d)}</p></article>"
            for t, d in [
                ("Strength blocks", "Progressive programming for real lifts."),
                ("Conditioning", "Engine work that respects joints."),
                ("Coaching desk", "Form checks and measurable PRs."),
                ("Open gym", "Serious floor, no mirror selfies culture."),
                ("Hyrox / hybrid", "Optional race prep tracks."),
                ("Recovery bay", "Mobility and down-regulation after hard days."),
            ]
        )
        schedule = [
            ("05:30", "Strength Engine"),
            ("07:00", "Hybrid Conditioning"),
            ("12:15", "Express Lift"),
            ("18:00", "Performance Class"),
            ("19:15", "Olympic Lifts"),
        ]
        rows = "".join(f"<tr><td>{t}</td><td>{s}</td></tr>" for t, s in schedule)
        return f"""<!DOCTYPE html>
<html lang="en"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{n} · {c}</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Archivo+Black&family=Space+Grotesk:wght@400;500;600;700&display=swap');
{self._base_css_common()}
:root{{--bg:#0B0B0C;--panel:#141416;--ink:#F5F5F5;--mute:#A1A1AA;--line:#27272A;--volt:#F97316}}
body{{font-family:'Space Grotesk',sans-serif;background:var(--bg);color:var(--ink)}}
.nav{{background:rgba(11,11,12,.92);border-bottom:1px solid var(--line)}}
.logo{{font-family:'Archivo Black',sans-serif;color:#fff;letter-spacing:.02em;text-transform:uppercase}}
.btn.primary{{background:var(--volt);color:#000;border-radius:0;text-transform:uppercase;letter-spacing:.06em;font-size:.75rem}}
.btn.ghost{{border:1px solid var(--line);color:#fff;border-radius:0}}
.pill{{background:transparent;color:var(--volt);padding:0;letter-spacing:.16em}}
h1,h2{{font-family:'Archivo Black',sans-serif;text-transform:uppercase;letter-spacing:.01em}}
.hero{{padding:70px 0 40px;border-bottom:1px solid var(--line)}}
.statbox{{background:var(--panel);border:1px solid var(--line);padding:22px}}
.statbox strong{{display:block;font-family:'Archivo Black',sans-serif;font-size:2.4rem;color:var(--volt)}}
.card{{background:var(--panel);border:1px solid var(--line);border-radius:0}}
.card p,.lead,.muted{{color:var(--mute)}}
.tool{{background:var(--panel);border:1px solid var(--line);border-radius:0}}
.tool .val{{color:var(--volt);font-family:'Archivo Black',sans-serif}}
.faq{{border-color:var(--line)}}
.footer{{border-top:1px solid var(--line);color:var(--mute)}}
.table td,.table th{{border-bottom:1px solid var(--line)}}
.stripe{{height:8px;background:linear-gradient(90deg,var(--volt),#FB923C 40%,transparent)}}
input[type=range]{{accent-color:var(--volt)}}
.modal-card input{{background:#0B0B0C;border-color:var(--line);color:#fff}}
</style></head><body>
<div class="stripe"></div>
<nav class="nav"><a class="logo" href="#">{n}</a><div class="actions subnav">
<a href="#about">About</a><a href="#schedule">Schedule</a><a href="#team">Team</a>
<button class="btn primary" onclick="openM()">Join / Trial</button></div></nav>
<main class="wrap">
  <section class="hero grid-2">
    <div>
      <div class="pill">Training floor · {c}</div>
      <h1 style="font-size:clamp(2.5rem,7vw,4.5rem);line-height:.95;margin:12px 0 16px">Train hard.<br>Recover smarter.</h1>
      <p class="lead">{n} is for people who want strength, sweat, and accountability — Fitness/Gym orange voltage on black, no pastel fluff.</p>
      <div class="actions">
        <button class="btn primary" onclick="openM()">Start trial week</button>
        <a class="btn ghost" href="#schedule">Today’s board</a>
      </div>
    </div>
    <div class="statbox">
      {self._img("gym", n + " training floor", 900, 560, 81, "shot")}
      <div class="pill" style="margin-top:12px">Floor metrics</div>
      <strong>240+</strong>
      <span class="muted">active members logging weekly PRs</span>
      <p class="muted" style="margin-top:14px">Coach line: <span style="color:#fff">{p}</span></p>
    </div>
  </section>
  {self._about(name, city, f"{name} is a serious training room in {city} for strength, conditioning, and accountability - not mirror-selfie culture.", "gym2", 18)}
  <section class="section">
    <h2>Programming pillars</h2>
    <p class="lead">Urgency + clarity. Conversion-first class layout.</p>
    <div class="grid-3">{cards}</div>
  </section>
  {self._team([
    ("Chris Vega", "Head coach", "Strength programming and PR tracking."),
    ("Riley Cho", "Conditioning coach", "Engine work and hybrid prep."),
    ("Dana Brooks", "Floor lead", "Onboarding and form standards."),
  ], "team2")}
  <section class="section grid-2" id="schedule">
    <div>
      <h2>Sample weekday board</h2>
      <table class="table">
        <tr><th>Time</th><th>Block</th></tr>
        {rows}
      </table>
    </div>
    <div class="tool">
      <div class="pill">Session builder</div>
      <h2 style="font-size:1.3rem;margin:8px 0">Days / week</h2>
      <div class="val" id="v">4 DAYS</div>
      <input type="range" min="2" max="6" value="4" oninput="document.getElementById('v').textContent=this.value+' DAYS'">
      <div style="margin-top:14px"><button class="btn primary" onclick="openM()">Lock my plan</button></div>
    </div>
  </section>
  <section class="section">
    <h2>Membership sketch</h2>
    <div class="grid-3">
      <article class="card"><h3>Drop-in</h3><p>From $35 / session</p></article>
      <article class="card"><h3>Unlimited</h3><p>From $189 / month</p></article>
      <article class="card"><h3>Coached 1:1</h3><p>Custom block pricing</p></article>
    </div>
  </section>
  <section class="section"><h2>FAQ</h2>{self._faq([
    ("Beginner friendly?", "Yes — coaches scale every block."),
    ("Do I need Olympic experience?", "No. We’ll meet you at your current skill."),
    ("Parking?", f"Details shared on signup for the {c} location."),
  ])}</section>
</main>
<footer class="footer">{n} · {c} · {p}</footer>
{self._modal(name, "Trial request", ["Name *", "Phone *", "Goal (strength / fat loss / hybrid)", "Preferred time"], "Send", dark=True, studio="GYM_DEMO")}
</body></html>"""

    # ================================================================= SPA
    def _spa(self, name: str, cat: str, city: str, phone: str) -> str:
        n, c, p = self._e(name), self._e(city), self._e(phone)
        rituals = [
            ("Facial ritual", "Skin-first protocols, unhurried pacing.", "75–90 min"),
            ("Body release", "Tension work in quiet rooms.", "60–90 min"),
            ("Glow add-on", "LED / mask finish for events.", "20 min"),
            ("Couples room", "Shared calm without noise.", "90 min"),
            ("Scalp therapy", "Reset for screen-heavy weeks.", "45 min"),
            ("Membership calm", "Recurring care, no hard sell theater.", "Monthly"),
        ]
        cards = "".join(
            f"<article class='card'><h3>{self._e(t)}</h3><p>{self._e(d)}</p><div class='time'>{self._e(tm)}</div></article>"
            for t, d, tm in rituals
        )
        art = """
<svg viewBox="0 0 640 360" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
  <rect width="640" height="360" rx="40" fill="#F3E0D6"/>
  <ellipse cx="320" cy="190" rx="170" ry="110" fill="#E7C4B8"/>
  <ellipse cx="250" cy="150" rx="70" ry="90" fill="#F8F1EC"/>
  <ellipse cx="390" cy="150" rx="70" ry="90" fill="#F8F1EC"/>
  <circle cx="320" cy="200" r="46" fill="#C9897B" opacity=".85"/>
  <path d="M200 280 C280 240, 360 300, 440 260" stroke="#C9897B" stroke-width="3" fill="none" opacity=".5"/>
</svg>"""
        return f"""<!DOCTYPE html>
<html lang="en"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{n} · {c}</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant:wght@400;500;600&family=Nunito+Sans:wght@300;400;600;700&display=swap');
{self._base_css_common()}
:root{{--bg:#F8F1EC;--ink:#3D2C29;--mute:#8A736C;--line:#E8D8D0;--rose:#EC4899;--cream:#FFFCF9;--dust:#C9897B}}
body{{font-family:'Nunito Sans',sans-serif;background:var(--bg);color:var(--ink);font-weight:300}}
.nav{{background:rgba(248,241,236,.92);border-bottom:1px solid var(--line)}}
.logo{{font-family:'Cormorant',serif;font-size:1.7rem;font-weight:500;color:var(--ink)}}
.btn.primary{{background:var(--dust);color:#fff}}
.btn.ghost{{background:var(--cream);color:var(--ink);border:1px solid var(--line)}}
.pill{{background:#F9D0E3;color:#9D174D}}
h1,h2,h3{{font-family:'Cormorant',serif;font-weight:500}}
.card{{background:var(--cream);border:1px solid var(--line)}}
.card .time{{margin-top:12px;font-size:.8rem;letter-spacing:.08em;text-transform:uppercase;color:var(--dust);font-weight:700}}
.card p,.lead,.muted{{color:var(--mute)}}
.tool{{background:var(--cream);border:1px solid var(--line)}}
.tool .val{{color:var(--dust);font-family:'Cormorant',serif}}
.faq{{border-color:var(--line);background:var(--cream)}}
.footer{{border-top:1px solid var(--line);color:var(--mute)}}
.quote{{background:var(--cream);border:1px solid var(--line)}}
input[type=range]{{accent-color:var(--dust)}}
</style></head><body>
<nav class="nav"><a class="logo" href="#">{n}</a><div class="actions subnav">
<a href="#about">About</a><a href="#rituals">Rituals</a><a href="#results">Results</a><a href="#team">Team</a>
<button class="btn primary" onclick="openM()">Book ritual</button></div></nav>
<main class="wrap">
  <section class="section grid-2" style="padding-top:40px">
    <div>
      <div class="pill">Sanctuary · {c}</div>
      <h1 style="font-size:clamp(2.4rem,5vw,3.6rem);line-height:1.12;margin:12px 0 14px">Soft rooms. Slow rituals. Skin that looks rested.</h1>
      <p class="lead">{n} is a wellness house for restoration without clinical coldness — Beauty/Spa palette, organic shapes, Nature Distilled calm.</p>
      <div class="actions">
        <button class="btn primary" onclick="openM()">Reserve a treatment</button>
        <a class="btn ghost" href="#rituals">View rituals</a>
      </div>
    </div>
    <div>{self._img("spa", n + " sanctuary", 1000, 900, 51, "shot tall")}</div>
  </section>
  {self._about(name, city, f"{name} is a calm wellness house in {city} - unhurried rituals, skin-first protocols, and rooms designed for the nervous system.", "spa2", 9)}
  {self._ba("spa", "spa2", "Before treatment cycle", "After a restorative series", 22)}
  <section class="section" id="rituals">
    <h2>Ritual menu</h2>
    <p class="lead">Each service includes consultation, treatment, and aftercare notes.</p>
    <div class="grid-3">{cards}</div>
  </section>
  <section class="section grid-2">
    <div class="quote">“I stopped dreading facials. The room is quiet, the pacing is human, and nobody upsold me into a 12-step cult.”<br><strong style="color:var(--ink)">— Guest, {c}</strong></div>
    <div class="tool">
      <div class="pill">Session length</div>
      <h2 style="font-size:1.7rem;margin:8px 0">How long to unplug?</h2>
      <div class="val" id="v">75 minutes</div>
      <input type="range" min="45" max="120" step="15" value="75" oninput="document.getElementById('v').textContent=this.value+' minutes'">
      <div style="margin-top:14px"><button class="btn primary" onclick="openM()">Book this length</button></div>
    </div>
  </section>
  {self._team([
    ("Nora Hale", "Lead aesthetician", "Facial architecture and skin plans."),
    ("Ivy Park", "Body therapist", "Release work and recovery."),
    ("Theo Quinn", "Guest host", "Booking, intake, aftercare."),
  ], "team")}
  <section class="section">
    <h2>House notes</h2>
    <table class="table">
      <tr><td>Arrive</td><td>10 minutes early for tea + intake</td></tr>
      <tr><td>Contraindications</td><td>Please share pregnancy/meds in advance</td></tr>
      <tr><td>Contact</td><td>{p}</td></tr>
    </table>
  </section>
  <section class="section"><h2>FAQ</h2>{self._faq([
    ("Gift cards?", "Yes — digital or printed."),
    ("Couples bookings?", "Available on selected evenings."),
    ("Parking?", f"Shared on confirmation for {c}."),
  ])}</section>
</main>
<footer class="footer">{n} · {c} · {p}</footer>
{self._modal(name, "Treatment request", ["Name *", "Phone *", "Treatment interest", "Preferred daypart"], "Send", studio="SPA_DEMO")}
</body></html>"""

    # ================================================================= JEWELRY
    def _jewelry(self, name: str, cat: str, city: str, phone: str) -> str:
        n, c, p = self._e(name), self._e(city), self._e(phone)
        pieces = [
            ("Solitaire study", "Quiet brilliance, precise proportions."),
            ("Eternity line", "Continuous light for everyday wear."),
            ("Atelier custom", "Stone-first commissions with sketches."),
            ("Heritage reset", "Modern settings for inherited stones."),
            ("Evening collar", "Statement geometry without noise."),
            ("Signet revival", "Personal seals, contemporary weight."),
        ]
        cards = "".join(f"<article class='card'><div class='gem'></div><h3>{self._e(t)}</h3><p>{self._e(d)}</p></article>" for t, d in pieces)
        return f"""<!DOCTYPE html>
<html lang="en"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{n} · Atelier · {c}</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Bodoni+Moda:opsz,wght@6..96,500;6..96,600&family=Inter:wght@300;400;500;600&display=swap');
{self._base_css_common()}
:root{{--bg:#0E0E0F;--ink:#F7F3EA;--mute:#A39E93;--line:rgba(247,243,234,.14);--gold:#C2A46B}}
body{{font-family:'Inter',sans-serif;background:var(--bg);color:var(--ink);font-weight:300}}
.nav{{border-bottom:1px solid var(--line);background:rgba(14,14,15,.92)}}
.logo{{font-family:'Bodoni Moda',serif;font-size:1.5rem;letter-spacing:.08em;color:var(--ink)}}
.btn.primary{{background:var(--gold);color:#111;border-radius:0;text-transform:uppercase;letter-spacing:.12em;font-size:.68rem}}
.btn.ghost{{border:1px solid var(--gold);color:var(--gold);border-radius:0;background:transparent}}
.pill{{color:var(--gold);letter-spacing:.28em;padding:0;background:transparent}}
h1,h2,h3{{font-family:'Bodoni Moda',serif;font-weight:500}}
.hero{{padding:90px 0;text-align:center;border-bottom:1px solid var(--line)}}
.ring{{width:min(260px,70vw);height:min(260px,70vw);margin:28px auto 18px;border-radius:50%;border:1px solid var(--gold);box-shadow:inset 0 0 0 18px rgba(194,164,107,.08);position:relative}}
.ring:after{{content:"";position:absolute;inset:28%;border-radius:50%;border:1px solid rgba(194,164,107,.35)}}
.card{{border:1px solid var(--line);border-radius:0;background:transparent;text-align:center}}
.card h3{{color:var(--gold);font-size:1.4rem}}
.card p,.lead,.muted{{color:var(--mute)}}
.gem{{width:54px;height:54px;margin:0 auto 12px;transform:rotate(45deg);border:1px solid var(--gold);background:radial-gradient(circle at 30% 30%,rgba(255,255,255,.25),transparent 45%),rgba(194,164,107,.08)}}
.tool{{border:1px solid var(--line);border-radius:0;background:transparent}}
.tool .val{{color:var(--gold);font-family:'Bodoni Moda',serif}}
.faq{{border-color:var(--line)}}
.footer{{border-top:1px solid var(--line);color:var(--mute)}}
input[type=range]{{accent-color:var(--gold)}}
.modal-card input{{background:#0E0E0F;border-color:var(--line);color:var(--ink)}}
</style></head><body>
<nav class="nav"><a class="logo" href="#">{n}</a><div class="actions subnav">
<a href="#about">About</a><a href="#collections">Collections</a><a href="#team">Team</a>
<button class="btn ghost" onclick="openM()">Private viewing</button></div></nav>
<section class="hero wrap">
  <div class="pill">High jewelry · {c}</div>
  <h1 style="font-size:clamp(2.6rem,6vw,4.3rem);line-height:1.08;margin:14px 0 12px">Quiet brilliance. Precise craft.</h1>
  <p class="lead" style="margin:0 auto">{n} presents jewels with atelier restraint — black field, ivory type, thin gold lines. Luxury that whispers.</p>
  <div class="ring" aria-hidden="true"></div>
  <button class="btn primary" onclick="openM()">Request a viewing</button>
</section>
<main class="wrap">
  {self._about(name, city, f"{name} is an appointment-only atelier in {city} for clients who want quiet brilliance and precise craft.", "jewelry2", 24)}
  <section class="section" id="collections">
    <h2 style="text-align:center">Collections</h2>
    <p class="lead" style="text-align:center;margin-left:auto;margin-right:auto">Space, proportion, almost no decoration - jewelry that whispers.</p>
    <div class="gallery" style="margin-bottom:18px">
      {self._img("jewelry", "Atelier piece", 1200, 800, 91, "shot g-main")}
      <div>
        {self._img("jewelry2", "Detail", 800, 390, 92, "shot g-side")}
        <div style="height:12px"></div>
        {self._img("jewelry", "Setting study", 800, 390, 93, "shot g-side")}
      </div>
    </div>
    <div class="grid-3">{cards}</div>
  </section>
  {self._team([
    ("Camille Laurent", "Creative director", "Stone-first design language."),
    ("Owen Park", "Master setter", "Precision settings and finishes."),
    ("Hana Ito", "Client advisor", "Private viewings and commissions."),
  ], "team")}
  <section class="section grid-2">
    <div>
      <h2>Atelier process</h2>
      {self._steps([
        ("Stone conversation", "Budget, shape, and lifestyle wear."),
        ("Sketch & model", "Proportion studies before metal."),
        ("Setting & reveal", "Final polish and private handover."),
      ])}
      <p class="muted" style="margin-top:12px">Desk: {p}</p>
    </div>
    <div class="tool">
      <div class="pill">Carat conversation</div>
      <h2 style="font-size:1.6rem;margin:8px 0">Center stone</h2>
      <div class="val" id="v">1.50 ct</div>
      <input type="range" min="50" max="500" value="150" oninput="document.getElementById('v').textContent=(this.value/100).toFixed(2)+' ct'">
      <div style="margin-top:14px"><button class="btn primary" onclick="openM()">Discuss this stone</button></div>
    </div>
  </section>
  <section class="section"><h2>FAQ</h2>{self._faq([
    ("Can I bring an heirloom stone?", "Yes — resets are a core atelier service."),
    ("Appointments only?", "Yes, for privacy and focus."),
    ("Certificates?", "Provided for eligible stones."),
  ])}</section>
</main>
<footer class="footer">{n} · {c} · {p}</footer>
{self._modal(name, "Private viewing", ["Name *", "Phone *", "Interest (bridal / custom / service)", "Budget window"], "Send", dark=True, studio="JEWELRY_DEMO")}
</body></html>"""

    # ================================================================= WEALTH
    def _wealth(self, name: str, cat: str, city: str, phone: str) -> str:
        n, c, p = self._e(name), self._e(city), self._e(phone)
        pillars = [
            ("Portfolio architecture", "Allocation matched to horizon and risk."),
            ("Family office liaison", "Multi-generational coordination."),
            ("Liquidity events", "Pre- and post-exit conversations."),
            ("Tax-aware planning", "Working alongside your counsel & CPA."),
            ("Private markets access", "Where suitable and understood."),
            ("Reporting cadence", "Clear packs, not dashboard theater."),
        ]
        cards = "".join(f"<article class='card'><h3>{self._e(t)}</h3><p>{self._e(d)}</p></article>" for t, d in pillars)
        return f"""<!DOCTYPE html>
<html lang="en"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{n} · {c}</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Newsreader:opsz,wght@6..72,500;6..72,600&family=IBM+Plex+Sans:wght@300;400;500;600&display=swap');
{self._base_css_common()}
:root{{--bg:#F2EFE8;--ink:#0F172A;--mute:#667084;--line:#D9D3C7;--navy:#0F172A;--gold:#A16207}}
body{{font-family:'IBM Plex Sans',sans-serif;background:var(--bg);color:var(--ink);font-weight:300}}
.nav{{background:rgba(242,239,232,.95);border-bottom:1px solid var(--line)}}
.logo{{font-family:'Newsreader',serif;font-size:1.35rem;color:var(--navy);font-weight:600}}
.btn.primary{{background:var(--navy);color:#fff;border-radius:0}}
.btn.ghost{{border:1px solid var(--navy);color:var(--navy);border-radius:0;background:transparent}}
.pill{{color:var(--gold);padding:0;background:transparent;letter-spacing:.16em}}
h1,h2,h3{{font-family:'Newsreader',serif;color:var(--navy);font-weight:600}}
.card{{background:#FFFEFA;border:1px solid var(--line);border-radius:0}}
.card p,.lead,.muted{{color:var(--mute)}}
.panel{{background:#FFFEFA;border:1px solid var(--line);padding:24px}}
.tool{{background:#FFFEFA;border:1px solid var(--line);border-radius:0}}
.tool .val{{color:var(--gold);font-family:'Newsreader',serif}}
.faq{{border-color:var(--line);background:#FFFEFA;border-radius:0}}
.footer{{background:var(--navy);color:#B7BFC9}}
.chart{{display:grid;grid-template-columns:repeat(5,1fr);gap:8px;align-items:end;height:140px;margin-top:12px}}
.chart span{{background:linear-gradient(180deg,#1E3A8A,#0F172A);border-radius:4px 4px 0 0}}
input[type=range]{{accent-color:var(--navy)}}
</style></head><body>
<nav class="nav"><a class="logo" href="#">{n}</a><div class="actions subnav">
<a href="#about">About</a><a href="#pillars">Pillars</a><a href="#team">Team</a>
<button class="btn primary" onclick="openM()">Private intro</button></div></nav>
<main class="wrap">
  <section class="section grid-2" style="padding-top:48px">
    <div>
      <div class="pill">Private advisory · {c}</div>
      <h1 style="font-size:clamp(2.1rem,4.2vw,3.2rem);line-height:1.15;margin:12px 0 14px">Stewardship for capital that must outlast the moment.</h1>
      <p class="lead">{n} works with families and principals who prefer measured process and plain language — Banking/Traditional Finance cues, not fintech billboard energy.</p>
      <div class="actions">
        <button class="btn primary" onclick="openM()">Request introduction</button>
        <a class="btn ghost" href="#pillars">Advisory pillars</a>
      </div>
    </div>
    <aside class="panel">
      {self._img("wealth", n + " private desk", 900, 700, 101, "shot")}
      <div class="pill" style="margin-top:12px">Desk</div>
      <h3 style="margin:8px 0">Confidential first meeting</h3>
      <p class="muted">Direct line: <strong style="color:var(--ink)">{p}</strong></p>
      <div class="chart" aria-hidden="true">
        <span style="height:40%"></span><span style="height:55%"></span><span style="height:48%"></span><span style="height:72%"></span><span style="height:63%"></span>
      </div>
      <p class="muted" style="margin-top:10px;font-size:.9rem">Illustrative allocation sketch - not performance data.</p>
    </aside>
  </section>
  {self._about(name, city, f"{name} works with families and principals in {city} who want measured process, plain language, and private-bank composure.", "wealth2", 26)}
  <section class="section" id="pillars">
    <h2>Advisory pillars</h2>
    <p class="lead">Trust density over visual excitement.</p>
    <div class="grid-3">{cards}</div>
  </section>
  {self._team([
    ("Margaret Shaw", "Managing partner", "Family architecture and governance."),
    ("Daniel Cho", "Portfolio strategist", "Allocation and liquidity events."),
    ("Elena Ruiz", "Client principal", "Reporting cadence and coordination."),
  ], "team")}
  <section class="section grid-2">
    <div>
      <h2>Engagement cadence</h2>
      {self._steps([
        ("Discovery", "Goals, constraints, existing structure."),
        ("Architecture", "Written plan with explicit tradeoffs."),
        ("Stewardship", "Quarterly reviews and event-driven updates."),
      ])}
    </div>
    <div class="tool">
      <div class="pill">Horizon</div>
      <h2 style="font-size:1.5rem;margin:8px 0">Years under consideration</h2>
      <div class="val" id="v">15-year horizon</div>
      <input type="range" min="3" max="40" value="15" oninput="document.getElementById('v').textContent=this.value+'-year horizon'">
      <div style="margin-top:14px"><button class="btn primary" onclick="openM()">Discuss this horizon</button></div>
    </div>
  </section>
  <section class="section"><h2>FAQ</h2>{self._faq([
    ("Minimums?", "Discussed privately after fit assessment."),
    ("Fiduciary?", "We clarify duty and fee model in writing before engagement."),
    ("Who is ideal?", "Principals and families who want process, not product pushing."),
  ])}</section>
</main>
<footer class="footer">{n}<br>{c} · {p}</footer>
{self._modal(name, "Private introduction", ["Name *", "Phone *", "Context (family / liquidity / portfolio)", "Approx. AUM range (optional)"], "Submit", studio="WEALTH_DEMO")}
</body></html>"""

    # ================================================================= UNIVERSAL
    def _universal(self, name: str, cat: str, city: str, phone: str) -> str:
        n, c, p = self._e(name), self._e(city), self._e(phone)
        cat_title = self._e((cat or "Professional Services").title())
        cards = "".join(
            f"<article class='card'><h3>{self._e(t)}</h3><p>{self._e(d)}</p></article>"
            for t, d in [
                (f"Core {cat_title}", f"Signature {cat_title.lower()} delivered with consistency."),
                ("Clear process", "Inquiry → consult → delivery without fog."),
                ("Local trust", f"Built for clients around {c}."),
                ("Proof pack", "Case notes and outcomes you can share."),
                ("Transparent scope", "What’s included — and what isn’t."),
                ("Fast response", "Human follow-up, not chatbot loops."),
            ]
        )
        return f"""<!DOCTYPE html>
<html lang="en"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{n} · {cat_title} · {c}</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Sora:wght@400;500;600;700&family=IBM+Plex+Sans:wght@300;400;600&display=swap');
{self._base_css_common()}
:root{{--bg:#F4F6FB;--ink:#12141C;--mute:#5C6478;--line:#D9DEEA;--ind:#3B4CCA;--soft:#E8EBFF}}
body{{font-family:'IBM Plex Sans',sans-serif;background:var(--bg);color:var(--ink)}}
.nav{{background:#fff;border-bottom:1px solid var(--line)}}
.logo{{font-family:'Sora',sans-serif;font-weight:700;color:var(--ink)}}
.btn.primary{{background:var(--ind);color:#fff;border-radius:12px}}
.btn.ghost{{background:var(--soft);color:var(--ind);border-radius:12px}}
.pill{{background:var(--soft);color:var(--ind)}}
h1,h2,h3{{font-family:'Sora',sans-serif}}
.card{{background:#fff;border:1px solid var(--line)}}
.card p,.lead,.muted{{color:var(--mute)}}
.panel{{background:#fff;border:1px solid var(--line);border-radius:20px;padding:22px}}
.tool{{background:#fff;border:1px solid var(--line)}}
.tool .val{{color:var(--ind);font-family:'Sora',sans-serif}}
.faq{{border-color:var(--line);background:#fff}}
.footer{{background:#fff;border-top:1px solid var(--line);color:var(--mute)}}
input[type=range]{{accent-color:var(--ind)}}
</style></head><body>
<nav class="nav"><a class="logo" href="#">{n}</a><div class="actions subnav">
<a href="#about">About</a><a href="#offer">Offer</a><a href="#team">Team</a>
<button class="btn primary" onclick="openM()">Contact</button></div></nav>
<main class="wrap">
  <section class="section grid-2" style="padding-top:40px">
    <div>
      <div class="pill">{cat_title} · {c}</div>
      <h1 style="font-size:clamp(2rem,4vw,2.9rem);line-height:1.15;margin:12px 0 14px">A sharper front door for {cat_title.lower()}</h1>
      <p class="lead">{n} helps clients understand the offer fast, trust the process, and take the next step — deliberately <em>not</em> a clone of the LeadFlow product UI.</p>
      <div class="actions">
        <button class="btn primary" onclick="openM()">Start a conversation</button>
        <a class="btn ghost" href="#offer">See offer</a>
      </div>
    </div>
    <aside class="panel">
      {self._img("universal", n + " studio", 900, 700, 111, "shot")}
      <div class="pill" style="margin-top:12px">Studio notes</div>
      <h3 style="margin:8px 0">Category-tuned layout</h3>
      <p class="muted">Indigo service studio - deliberately not a LeadFlow product UI clone.</p>
      <p class="muted" style="margin-top:12px">Line: <strong style="color:var(--ink)">{p}</strong></p>
    </aside>
  </section>
  {self._about(name, city, f"{name} helps clients in {city} understand the offer fast and take the next step without agency theater.", "universal", 28)}
  <section class="section" id="offer">
    <h2>What clients get</h2>
    <div class="grid-3">{cards}</div>
  </section>
  {self._team([
    ("Alex Rivera", "Principal", "Scope and delivery standards."),
    ("Kim Sato", "Producer", "Timeline and client communication."),
    ("Lee Morgan", "Specialist", "Hands-on execution."),
  ], "team2")}
  <section class="section grid-2">
    <div>
      <h2>How it works</h2>
      {self._steps([
        ("Brief", "Goals, constraints, timeline."),
        ("Proposal", "Scope, milestones, fee."),
        ("Delivery", "Work + weekly checkpoints."),
      ])}
    </div>
    <div class="tool">
      <div class="pill">Engagement size</div>
      <h2 style="font-size:1.3rem;margin:8px 0">Project scale</h2>
      <div class="val" id="v">Medium</div>
      <input type="range" min="1" max="5" value="3" oninput="const m={{1:'Starter',2:'Focused',3:'Medium',4:'Growth',5:'Enterprise'}};document.getElementById('v').textContent=m[this.value]">
      <div style="margin-top:14px"><button class="btn primary" onclick="openM()">Match me</button></div>
    </div>
  </section>
  <section class="section"><h2>FAQ</h2>{self._faq([
    ("Remote or on-site?", f"Both available depending on the work in {c}."),
    ("Typical timeline?", "Scoped after the first call."),
    ("Who is ideal?", f"Teams that need reliable {cat_title.lower()} without agency theater."),
  ])}</section>
</main>
<footer class="footer">{n} · {c} · {p}</footer>
{self._modal(name, "Contact", ["Name *", "Phone *", "What do you need?", "Timeline"], "Send", studio="UNIVERSAL_DEMO")}
</body></html>"""


if __name__ == "__main__":
    g = ShadowInfiltrator()
    samples = [
        ("Apex Dental Lounge", "Dental Clinic", "Toronto", "+1 416 555 0199"),
        ("Lumiere Fine Dining", "Restaurant", "Paris", "+33 1 42 68 55 00"),
        ("Vanguard Legal Counsel", "Law Firm", "New York", "+1 212 555 0100"),
        ("Skyline Real Estate", "Real Estate", "Dubai", "+971 4 318 8888"),
        ("Titan Elite Gym", "Gym", "London", "+44 20 5555 0100"),
        ("Aura Aesthetic Spa", "Spa", "Munich", "+49 89 555 0100"),
        ("Royal Crown Jewelry", "Jewelry", "Singapore", "+65 6555 0100"),
        ("Horizon Private Wealth", "Wealth", "Melbourne", "+61 3 5550 0100"),
    ]
    for s in samples:
        r = g.generate_luxury_site(*s)
        print(r["design_kind"], r["industry_paradigm_applied"])
