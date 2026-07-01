"""
LeadFlow.AI - Shadow Infiltrator Pro Max (GSAP + Three.js + Lenis 3D Engine)
Synthesizes Awwwards-winning 3D motion-graphic websites with 8 rich interactive sections,
Three.js 3D geometric interactive sculptures, GSAP ScrollTrigger parallax,
infinite marquee tickers, live ROI calculators, Before/After comparison sliders,
floating AI chat widgets, and confetti-triggering VIP booking funnels.
Includes offline fallback engines for iframe sandboxes without CDN access.
"""

import os
from typing import Dict, Any

class ShadowInfiltrator:
    def __init__(self, output_dir: str = "generated_sites"):
        self.output_dir = output_dir
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir, exist_ok=True)

    def _get_theme(self, category: str) -> Dict[str, str]:
        cat = category.lower()
        if any(w in cat for w in ["dental", "clinic", "health", "doctor", "medical"]):
            return {
                "name": "Holographic Medical Cyber-Blue",
                "primary": "#00f0ff", "secondary": "#0077ff", "accent": "#00ffaa",
                "badge": "🧬 TOP RATED 3D BIOMIMETIC HEALTHCARE IN",
                "hero_title": "Next-Generation", "hero_sub": "Precision Healthcare",
                "desc": "Combining advanced 3D AI diagnostics, painless robotic precision, and spa-level luxury to transform your healthcare experience.",
                "calc_title": "Interactive Health & Time Savings Calculator",
                "calc_label": "Estimated Monthly Patients / Treatments",
                "calc_unit": "Patients", "calc_val": "120",
                "calc_result_label": "Estimated Annual Revenue Increase:",
                "calc_mult": 1450,
                "service_1": "3D Robotic Scanning", "desc_1": "High-definition anatomical 3D mapping with zero discomfort or radiation.", "icon_1": "🧬",
                "service_2": "Painless Laser Therapy", "desc_2": "Non-invasive rapid healing technology designed for complete VIP comfort.", "icon_2": "⚡",
                "service_3": "Biomimetic Restoration", "desc_3": "Custom aesthetic smile redesigns tailored to your exact facial symmetry.", "icon_3": "💎",
                "service_4": "AI Concierge Monitoring", "desc_4": "24/7 proactive recovery tracking and instant virtual physician connection.", "icon_4": "🛡️",
                "before_label": "Traditional Painful Procedures", "after_label": "LeadFlow 3D Painless Luxury Suite"
            }
        elif any(w in cat for w in ["restaurant", "dining", "food", "lounge", "cafe", "bistro"]):
            return {
                "name": "Obsidian Gold Fine Dining",
                "primary": "#ffd700", "secondary": "#ff0055", "accent": "#ff8800",
                "badge": "🍷 MICHELIN-LEVEL CULINARY ARTISTRY IN",
                "hero_title": "An Unforgettable", "hero_sub": "Sensory Symphony",
                "desc": "Where artisanal culinary heritage meets avant-garde molecular gastronomy in an immersive, candle-lit luxury sanctuary.",
                "calc_title": "VIP Private Dining & Event Value Calculator",
                "calc_label": "Expected Guests / Group Size",
                "calc_unit": "Guests", "calc_val": "24",
                "calc_result_label": "Estimated Tasting Package Value:",
                "calc_mult": 380,
                "service_1": "Molecular Tasting Menu", "desc_1": "A 12-course theatrical culinary journey through texture, aroma, and visual enchantment.", "icon_1": "🔥",
                "service_2": "Private Sommelier Vault", "desc_2": "Exclusive access to rare international vintages curated by master sommeliers.", "icon_2": "🍾",
                "service_3": "Theatrical Chef's Table", "desc_3": "Front-row seating inside our open kitchen with personalized chef commentary.", "icon_3": "👑",
                "service_4": "Bespoke Event Catering", "desc_4": "Custom luxury menus engineered specifically for your high-profile private gatherings.", "icon_4": "🥂",
                "before_label": "Standard Crowded Restaurants", "after_label": "LeadFlow VIP Private Gastronomy",
                "extra_btn": '<a href="lumiere_3d_dish_experience.html" class="btn-vip" style="background: linear-gradient(135deg, #ffd700, #ff8800); color: #000; padding: 16px 28px; text-decoration: none; font-size: 15px; box-shadow: 0 0 30px rgba(255, 215, 0, 0.5);">🍔 Launch 3D Interactive Dish →</a>'
            }
        elif any(w in cat for w in ["salon", "spa", "beauty", "hair", "skin", "wellness"]):
            return {
                "name": "Rose Gold Aurora Sanctuary",
                "primary": "#ff77aa", "secondary": "#9900ff", "accent": "#00ffff",
                "badge": "✨ PREMIER LUXURY BEAUTY & WELLNESS IN",
                "hero_title": "Elevate Your", "hero_sub": "Radiant Elegance",
                "desc": "An indulgent sanctuary offering cellular skin rejuvenation, celebrity styling, and holistic stress-release therapies.",
                "calc_title": "Holistic Rejuvenation Value Calculator",
                "calc_label": "Desired Monthly Treatment Sessions",
                "calc_unit": "Sessions", "calc_val": "4",
                "calc_result_label": "Estimated VIP Membership Value:",
                "calc_mult": 650,
                "service_1": "Cellular Skin Infusion", "desc_1": "Oxygen and peptide serums restoring youthful luminescence after one session.", "icon_1": "🌸",
                "service_2": "Couture Hair Architecture", "desc_2": "Master colorists and stylists crafting tailored looks for your facial structure.", "icon_2": "✂️",
                "service_3": "Mineral Hydro-Therapy", "desc_3": "Aromatherapy immersion and lymphatic drainage designed for profound relaxation.", "icon_3": "💆‍♀️",
                "service_4": "AI Skin Diagnostics", "desc_4": "Precision dermatological mapping predicting cellular renewal rates.", "icon_4": "🔬",
                "before_label": "Generic Salons & Harsh Chemicals", "after_label": "LeadFlow Organic VIP Serenity"
            }
        else:
            return {
                "name": "Cyberpunk Bento SaaS Pro",
                "primary": "#00f0ff", "secondary": "#ec4899", "accent": "#6366f1",
                "badge": "⚡ #1 INDUSTRY LEADER & INNOVATOR IN",
                "hero_title": "Redefining", "hero_sub": "Industry Excellence",
                "desc": "Harnessing cutting-edge 3D technology, bespoke craftsmanship, and autonomous precision to deliver unmatched results.",
                "calc_title": "Interactive ROI & Growth Multiplier Calculator",
                "calc_label": "Monthly Business Transaction Volume",
                "calc_unit": "Transactions", "calc_val": "500",
                "calc_result_label": "Estimated Annual Revenue Impact:",
                "calc_mult": 499,
                "service_1": "Next-Gen Automation", "desc_1": "Streamlined workflows and AI precision eliminating friction and maximizing output.", "icon_1": "⚡",
                "service_2": "3D Visual Experiences", "desc_2": "Immersive interactive design keeping clients engaged 10x longer on your platform.", "icon_2": "🌐",
                "service_3": "Enterprise Security", "desc_3": "Bank-grade encryption, rapid execution, and 24/7 dedicated system reliability.", "icon_3": "🛡️",
                "service_4": "Autonomous Scaling", "desc_4": "Self-optimizing pipelines designed to grow seamlessly with your customer demand.", "icon_4": "📈",
                "before_label": "Outdated Static Web Interfaces", "after_label": "LeadFlow 3D Interactive Metaverse"
            }

    def generate_luxury_site(self, business_name: str, category: str, city: str, phone: str = "+1 (555) 019-2831") -> Dict[str, Any]:
        slug = "".join(c if c.isalnum() else "_" for c in business_name.lower()).strip("_")
        filename = f"{slug}_luxury.html"
        filepath = os.path.join(self.output_dir, filename)

        t = self._get_theme(category)
        city_title = city.title() if city else "Metropolis"

        html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{business_name} - {t['hero_sub']} in {city_title}</title>
    <!-- External CDNs with offline fallbacks -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.9.3/dist/confetti.browser.min.js"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Space+Grotesk:wght@500;700;800&display=swap');
        
        :root {{
            --bg: #03060d;
            --surface: #0a1020;
            --primary: {t['primary']};
            --secondary: {t['secondary']};
            --accent: {t['accent']};
            --glass: rgba(255, 255, 255, 0.04);
            --border: rgba(255, 255, 255, 0.1);
            --border-glow: {t['primary']}55;
            --font-main: 'Plus Jakarta Sans', sans-serif;
            --font-display: 'Space Grotesk', sans-serif;
        }}

        * {{ margin: 0; padding: 0; box-sizing: border-box; font-family: var(--font-main); }}
        
        body {{
            background-color: var(--bg);
            color: #ffffff;
            overflow-x: hidden;
            perspective: 1000px;
        }}

        /* 3D Canvas Container */
        #three-canvas-container {{
            position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
            pointer-events: none; z-index: 0; opacity: 0.65;
        }}

        /* Top Banner */
        .ai-banner {{
            background: linear-gradient(90deg, #0a1020, #1e1b4b, #0a1020);
            border-bottom: 1px solid var(--border-glow);
            padding: 10px 20px; text-align: center; font-size: 12px; font-weight: 800;
            letter-spacing: 2px; color: var(--primary); position: relative; z-index: 100;
            text-transform: uppercase;
        }}

        /* Navbar */
        nav {{
            display: flex; justify-content: space-between; align-items: center;
            padding: 24px 60px; background: rgba(3, 6, 13, 0.85);
            backdrop-filter: blur(20px); border-bottom: 1px solid var(--border);
            position: sticky; top: 0; z-index: 90;
        }}
        @media (max-width: 768px) {{ nav {{ padding: 18px 24px; flex-direction: column; gap: 14px; }} }}

        .brand {{
            font-family: var(--font-display); font-size: 26px; font-weight: 800;
            background: linear-gradient(to right, #ffffff, var(--primary));
            -webkit-background-clip: text; -webkit-text-fill-color: transparent;
            display: flex; align-items: center; gap: 12px;
        }}
        .brand-logo {{
            width: 40px; height: 40px; background: linear-gradient(135deg, var(--primary), var(--secondary));
            border-radius: 12px; display: flex; align-items: center; justify-content: center;
            color: #000; font-weight: 800; font-size: 18px; box-shadow: 0 0 25px var(--border-glow);
        }}

        .btn-vip {{
            background: linear-gradient(135deg, var(--primary), var(--secondary));
            color: #000; font-weight: 800; font-size: 14px; padding: 14px 28px;
            border-radius: 30px; border: none; cursor: pointer; text-decoration: none;
            box-shadow: 0 0 30px var(--border-glow); transition: all 0.3s;
            text-transform: uppercase; letter-spacing: 1px; display: inline-flex; align-items: center; gap: 8px;
        }}
        .btn-vip:hover {{ transform: translateY(-3px) scale(1.03); box-shadow: 0 0 45px var(--primary); }}

        /* SECTION 1: HERO */
        .hero {{
            padding: 100px 60px 120px; max-width: 1300px; margin: 0 auto;
            position: relative; z-index: 10; min-height: 85vh;
            display: grid; grid-template-columns: 1.2fr 0.8fr; align-items: center; gap: 60px;
        }}
        @media (max-width: 992px) {{ .hero {{ grid-template-columns: 1fr; text-align: center; padding: 60px 24px; }} }}

        .hero-badge {{
            display: inline-flex; align-items: center; gap: 8px;
            background: rgba(255, 255, 255, 0.05); border: 1px solid var(--border-glow);
            color: var(--primary); padding: 8px 18px; border-radius: 30px;
            font-size: 13px; font-weight: 700; margin-bottom: 24px; text-transform: uppercase;
        }}
        h1 {{ font-family: var(--font-display); font-size: 66px; font-weight: 800; line-height: 1.05; margin-bottom: 24px; }}
        @media (max-width: 768px) {{ h1 {{ font-size: 42px; }} }}
        h1 span.highlight {{
            background: linear-gradient(135deg, var(--primary), var(--secondary), #fff);
            -webkit-background-clip: text; -webkit-text-fill-color: transparent;
            text-shadow: 0 0 30px rgba(0,240,255,0.3);
        }}
        p.lead {{ font-size: 19px; color: #9ca3af; max-width: 580px; margin-bottom: 40px; line-height: 1.7; }}
        @media (max-width: 992px) {{ p.lead {{ margin: 0 auto 40px; }} }}

        .floating-card-3d {{
            background: rgba(10, 16, 32, 0.75); border: 1px solid var(--border-glow);
            border-radius: 28px; padding: 36px; backdrop-filter: blur(25px);
            box-shadow: 0 30px 60px rgba(0,0,0,0.8), 0 0 40px var(--border-glow);
            transform: rotateY(-12deg) rotateX(8deg); transition: transform 0.2s ease-out;
            position: relative; overflow: hidden; cursor: pointer;
        }}
        .floating-card-3d:hover {{ transform: rotateY(0deg) rotateX(0deg) scale(1.04); }}
        .dot-pulse {{ width: 10px; height: 10px; background: #34d399; border-radius: 50%; display: inline-block; box-shadow: 0 0 10px #34d399; }}

        /* SECTION 2: INFINITE MARQUEE TICKER */
        .marquee-section {{
            background: rgba(10, 16, 32, 0.9); border-top: 1px solid var(--border); border-bottom: 1px solid var(--border);
            padding: 20px 0; overflow: hidden; position: relative; z-index: 10; margin-bottom: 100px;
        }}
        .marquee-track {{ display: flex; gap: 60px; width: max-content; animation: scrollMarquee 25s linear infinite; }}
        @keyframes scrollMarquee {{ 0% {{ transform: translateX(0); }} 100% {{ transform: translateX(-50%); }} }}
        .marquee-item {{ font-family: var(--font-display); font-size: 18px; font-weight: 700; color: #fff; display: flex; align-items: center; gap: 12px; white-space: nowrap; }}
        .marquee-item span {{ color: var(--primary); }}

        /* SECTION 3: BENTO GRID SERVICES */
        .section-box {{ padding: 80px 60px; max-width: 1300px; margin: 0 auto; position: relative; z-index: 10; }}
        @media (max-width: 768px) {{ .section-box {{ padding: 60px 24px; }} }}
        .section-header {{ text-align: center; margin-bottom: 70px; }}
        .section-header h2 {{ font-family: var(--font-display); font-size: 44px; font-weight: 800; margin-bottom: 16px; }}
        .section-header p {{ color: #9ca3af; font-size: 18px; max-width: 650px; margin: 0 auto; }}

        .bento-grid {{ display: grid; grid-template-columns: repeat(2, 1fr); gap: 30px; }}
        @media (max-width: 768px) {{ .bento-grid {{ grid-template-columns: 1fr; }} }}
        .bento-card {{
            background: var(--surface); border: 1px solid var(--border); border-radius: 28px;
            padding: 40px; position: relative; overflow: hidden; transition: all 0.3s;
        }}
        .bento-card:hover {{ border-color: var(--primary); transform: translateY(-8px); box-shadow: 0 20px 40px rgba(0,0,0,0.6), 0 0 30px var(--border-glow); }}
        .card-icon {{ width: 64px; height: 64px; border-radius: 18px; background: rgba(255,255,255,0.04); border: 1px solid var(--border-glow); display: flex; align-items: center; justify-content: center; font-size: 32px; margin-bottom: 24px; }}
        .bento-card h3 {{ font-size: 24px; font-weight: 700; margin-bottom: 12px; color: #fff; }}
        .bento-card p {{ color: #9ca3af; font-size: 16px; line-height: 1.7; }}

        /* SECTION 4: INTERACTIVE ROI CALCULATOR */
        .calc-box {{
            background: linear-gradient(135deg, rgba(10,16,32,0.9), rgba(0,240,255,0.08));
            border: 1px solid var(--border-glow); border-radius: 36px; padding: 60px;
            box-shadow: 0 30px 80px rgba(0,0,0,0.8); margin: 60px 0; text-align: center;
        }}
        @media (max-width: 768px) {{ .calc-box {{ padding: 36px 20px; }} }}
        .calc-slider {{ width: 100%; max-width: 600px; height: 10px; background: #1e293b; border-radius: 10px; outline: none; margin: 30px 0; accent-color: var(--primary); cursor: pointer; }}
        .calc-output {{ font-family: var(--font-display); font-size: 64px; font-weight: 800; color: var(--primary); text-shadow: 0 0 30px var(--border-glow); margin: 20px 0; }}

        /* SECTION 5: BEFORE & AFTER COMPARISON SLIDER */
        .comp-container {{
            position: relative; width: 100%; max-width: 900px; height: 400px; margin: 40px auto;
            border-radius: 28px; overflow: hidden; border: 1px solid var(--border-glow);
            box-shadow: 0 30px 60px rgba(0,0,0,0.8); user-select: none;
        }}
        @media (max-width: 768px) {{ .comp-container {{ height: 300px; }} }}
        .comp-layer {{
            position: absolute; top: 0; left: 0; width: 100%; height: 100%;
            display: flex; align-items: center; justify-content: center; font-size: 24px; font-weight: 800; padding: 40px; text-align: center;
        }}
        .comp-before {{ background: #111827; color: #9ca3af; width: 100%; }}
        .comp-after {{ background: linear-gradient(135deg, #0f172a, #1e1b4b); color: var(--primary); width: 50%; overflow: hidden; border-right: 3px solid var(--primary); box-shadow: 5px 0 25px var(--border-glow); }}
        .comp-slider-input {{
            position: absolute; top: 0; left: 0; width: 100%; height: 100%;
            opacity: 0; cursor: ew-resize; z-index: 20;
        }}

        /* SECTION 6: 3D FAQ ACCORDION */
        .faq-item {{
            background: var(--surface); border: 1px solid var(--border); border-radius: 20px;
            margin-bottom: 16px; overflow: hidden; transition: all 0.3s;
        }}
        .faq-header {{ padding: 24px 30px; font-size: 18px; font-weight: 700; cursor: pointer; display: flex; justify-content: space-between; align-items: center; }}
        .faq-body {{ padding: 0 30px; max-height: 0; overflow: hidden; color: #9ca3af; line-height: 1.7; transition: max-height 0.4s ease, padding 0.4s ease; }}
        .faq-item.active {{ border-color: var(--primary); box-shadow: 0 0 25px rgba(0,240,255,0.15); }}
        .faq-item.active .faq-body {{ padding-bottom: 24px; max-height: 200px; }}

        /* SECTION 7: FLOATING AI CHAT WIDGET */
        .ai-chat-btn {{
            position: fixed; bottom: 30px; right: 30px; width: 64px; height: 64px;
            background: linear-gradient(135deg, var(--primary), var(--secondary));
            border-radius: 50%; display: flex; align-items: center; justify-content: center;
            font-size: 28px; cursor: pointer; box-shadow: 0 0 30px var(--primary);
            z-index: 500; transition: transform 0.3s;
        }}
        .ai-chat-btn:hover {{ transform: scale(1.1) rotate(10deg); }}
        .ai-chat-window {{
            position: fixed; bottom: 110px; right: 30px; width: 340px; background: #0a1020;
            border: 1px solid var(--primary); border-radius: 24px; padding: 24px;
            box-shadow: 0 20px 50px rgba(0,0,0,0.8); z-index: 500; display: none;
            flex-direction: column; gap: 16px;
        }}

        /* SECTION 8: VIP BOOKING MODAL */
        .modal-overlay {{
            position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
            background: rgba(0,0,0,0.85); backdrop-filter: blur(15px);
            display: none; align-items: center; justify-content: center; z-index: 1000; padding: 20px;
        }}
        .modal-box {{
            background: #0a1020; border: 1px solid var(--primary); border-radius: 32px;
            max-width: 520px; width: 100%; padding: 40px; position: relative;
            box-shadow: 0 0 60px rgba(0,240,255,0.4);
        }}
        .form-input {{ width: 100%; padding: 14px 18px; background: rgba(255,255,255,0.03); border: 1px solid var(--border); border-radius: 12px; color: #fff; font-size: 15px; outline: none; margin-bottom: 16px; }}
        .form-input:focus {{ border-color: var(--primary); }}

        /* Scroll Reveal Animation Classes */
        .gsap-reveal {{ opacity: 0; transform: translateY(40px); transition: all 0.8s ease; }}
        .gsap-reveal.active {{ opacity: 1; transform: translateY(0); }}
    </style>
</head>
<body>

    <!-- Three.js / WebGL 3D Canvas -->
    <div id="three-canvas-container"></div>

    <div class="ai-banner">
        ⚡ PRO MAX 3D INTERACTIVE MASTERPIECE | {t['name'].upper()} | ADVANCED GSAP & THREE.JS ENGINE ⚡
    </div>

    <nav>
        <div class="brand">
            <div class="brand-logo">{business_name[:2].upper()}</div>
            <span>{business_name}</span>
        </div>
        <button class="btn-vip" onclick="openModal()">✨ Book VIP Consultation</button>
    </nav>

    <!-- SECTION 1: HERO -->
    <header class="hero">
        <div class="gsap-reveal">
            <div class="hero-badge">{t['badge']} {city_title.upper()}</div>
            <h1>{t['hero_title']} <br><span class="highlight">{t['hero_sub']}</span></h1>
            <p class="lead">{t['desc']}</p>
            <div style="display: flex; gap: 16px; flex-wrap: wrap;">
                <button class="btn-vip" style="padding: 16px 36px; font-size: 16px;" onclick="openModal()">🚀 Reserve Your Experience</button>
                {t.get('extra_btn', '')}
                <a href="#calculator" style="color: #fff; font-weight: 700; text-decoration: none; display: flex; align-items: center; gap: 8px; padding: 16px;">Calculate Savings ↓</a>
            </div>
        </div>

        <div class="floating-card-3d gsap-reveal">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
                <span style="font-weight: 800; font-size: 14px; color: #fff;">LIVE 3D SUITE MONITOR</span>
                <span style="font-size: 12px; font-weight: 700; color: #34d399;"><span class="dot-pulse"></span> ONLINE</span>
            </div>
            <div style="font-size: 24px; font-weight: 800; margin-bottom: 6px; color: #fff;">{business_name}</div>
            <div style="font-size: 14px; color: #9ca3af; margin-bottom: 24px;">Location: Premier District, {city_title}</div>
            <div style="background: rgba(255,255,255,0.04); border: 1px solid var(--border); border-radius: 16px; padding: 16px; display: flex; justify-content: space-between; margin-bottom: 12px;">
                <span style="font-size: 13px; color: #9ca3af;">Client Satisfaction Rating</span>
                <span style="font-size: 22px; font-weight: 800; color: var(--primary);">99.9% ★</span>
            </div>
            <div style="background: rgba(255,255,255,0.04); border: 1px solid var(--border); border-radius: 16px; padding: 16px; display: flex; justify-content: space-between;">
                <span style="font-size: 13px; color: #9ca3af;">VIP Priority Access</span>
                <span style="font-size: 22px; font-weight: 800; color: var(--primary);">Instant</span>
            </div>
        </div>
    </header>

    <!-- SECTION 2: INFINITE MARQUEE TICKER -->
    <div class="marquee-section">
        <div class="marquee-track">
            <div class="marquee-item"><span>★</span> 100% VERIFIED VIP EXCELLENCE <span>★</span> FEATURED IN LUXURY DIGEST <span>★</span> STATE-OF-THE-ART 3D TECHNOLOGY <span>★</span> ZERO DISCOMFORT GUARANTEED <span>★</span> 24/7 CONCIERGE SERVICE <span>★</span></div>
            <div class="marquee-item"><span>★</span> 100% VERIFIED VIP EXCELLENCE <span>★</span> FEATURED IN LUXURY DIGEST <span>★</span> STATE-OF-THE-ART 3D TECHNOLOGY <span>★</span> ZERO DISCOMFORT GUARANTEED <span>★</span> 24/7 CONCIERGE SERVICE <span>★</span></div>
        </div>
    </div>

    <!-- SECTION 3: BENTO GRID SERVICES -->
    <section class="section-box" id="services">
        <div class="section-header gsap-reveal">
            <h2>The 3D Excellence Suite</h2>
            <p>Every service is meticulously tailored using award-winning techniques and ultra-premium craftsmanship.</p>
        </div>
        <div class="bento-grid">
            <div class="bento-card gsap-reveal">
                <div class="card-icon">{t['icon_1']}</div>
                <h3>{t['service_1']}</h3>
                <p>{t['desc_1']}</p>
            </div>
            <div class="bento-card gsap-reveal">
                <div class="card-icon">{t['icon_2']}</div>
                <h3>{t['service_2']}</h3>
                <p>{t['desc_2']}</p>
            </div>
            <div class="bento-card gsap-reveal">
                <div class="card-icon">{t['icon_3']}</div>
                <h3>{t['service_3']}</h3>
                <p>{t['desc_3']}</p>
            </div>
            <div class="bento-card gsap-reveal">
                <div class="card-icon">{t['icon_4']}</div>
                <h3>{t['service_4']}</h3>
                <p>{t['desc_4']}</p>
            </div>
        </div>
    </section>

    <!-- SECTION 4: INTERACTIVE ROI CALCULATOR -->
    <section class="section-box" id="calculator">
        <div class="calc-box gsap-reveal">
            <h2 style="font-family: var(--font-display); font-size: 38px; font-weight: 800; margin-bottom: 12px;">{t['calc_title']}</h2>
            <p style="color: #9ca3af; font-size: 16px; margin-bottom: 30px;">Drag the slider below to calculate your estimated growth and time savings with {business_name}:</p>
            
            <div style="font-size: 18px; font-weight: 700; color: #fff;">{t['calc_label']}: <span id="calc-val-text" style="color: var(--primary);">{t['calc_val']}</span> {t['calc_unit']}</div>
            <input type="range" class="calc-slider" id="roi-slider" min="10" max="500" value="{t['calc_val']}" step="10" oninput="updateCalc()">
            
            <div style="font-size: 16px; color: #9ca3af; margin-top: 20px;">{t['calc_result_label']}</div>
            <div class="calc-output" id="calc-result-text">$174,000 / yr</div>
            <button class="btn-vip" style="margin-top: 20px;" onclick="openModal()">🚀 Lock In This Value Now</button>
        </div>
    </section>

    <!-- SECTION 5: BEFORE & AFTER COMPARISON SLIDER -->
    <section class="section-box">
        <div class="section-header gsap-reveal">
            <h2>Interactive Transformation Comparison</h2>
            <p>Drag the slider divider left and right to see the immense difference in quality and luxury.</p>
        </div>
        <div class="comp-container gsap-reveal">
            <div class="comp-layer comp-before">❌ {t['before_label']}</div>
            <div class="comp-layer comp-after" id="comp-after-layer">✨ {t['after_label']}</div>
            <input type="range" class="comp-slider-input" min="0" max="100" value="50" oninput="updateComparison(this.value)">
        </div>
    </section>

    <!-- SECTION 6: 3D FAQ ACCORDION -->
    <section class="section-box">
        <div class="section-header gsap-reveal">
            <h2>Frequently Asked Questions</h2>
            <p>Everything you need to know about our VIP consultation process and 3D suite.</p>
        </div>
        <div style="max-width: 800px; margin: 0 auto;">
            <div class="faq-item gsap-reveal" onclick="this.classList.toggle('active')">
                <div class="faq-header"><span>How fast can I book a VIP session with {business_name}?</span><span>+</span></div>
                <div class="faq-body">Our concierge system schedules priority appointments immediately. Once you submit the VIP form, our team connects with you in under 1 minute.</div>
            </div>
            <div class="faq-item gsap-reveal" onclick="this.classList.toggle('active')">
                <div class="faq-header"><span>What makes the 3D luxury suite different from standard establishments?</span><span>+</span></div>
                <div class="faq-body">We utilize award-winning biomimetic techniques, state-of-the-art non-invasive technology, and organic premium materials to ensure zero discomfort and 100% satisfaction.</div>
            </div>
            <div class="faq-item gsap-reveal" onclick="this.classList.toggle('active')">
                <div class="faq-header"><span>Is private off-market consultation available?</span><span>+</span></div>
                <div class="faq-body">Yes. For high-profile individuals and executives requiring complete confidentiality, we offer exclusive after-hours private suite reservations upon request.</div>
            </div>
        </div>
    </section>

    <!-- SECTION 7: FLOATING AI CHAT WIDGET -->
    <div class="ai-chat-btn" onclick="toggleChat()">🤖</div>
    <div class="ai-chat-window" id="ai-chat">
        <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid var(--border); padding-bottom: 12px;">
            <span style="font-weight: 800; color: #fff;">Elena AI Concierge</span>
            <span style="cursor: pointer; color: #9ca3af;" onclick="toggleChat()">×</span>
        </div>
        <div id="chat-messages" style="max-height: 200px; overflow-y: auto; font-size: 13px; color: #9ca3af; display: flex; flex-direction: column; gap: 8px;">
            <div style="background: rgba(255,255,255,0.05); padding: 10px; border-radius: 12px;">👋 Hello! I am Elena, the AI Concierge for {business_name}. Would you like to book a priority VIP consultation?</div>
        </div>
        <div style="display: flex; gap: 8px;">
            <input type="text" id="chat-input" placeholder="Ask a question..." style="flex: 1; background: rgba(255,255,255,0.05); border: 1px solid var(--border); border-radius: 8px; padding: 8px; color: #fff; font-size: 12px; outline: none;" onkeypress="if(event.key==='Enter') sendChat()">
            <button onclick="sendChat()" style="background: var(--primary); border: none; padding: 8px 12px; border-radius: 8px; font-weight: 700; cursor: pointer;">Send</button>
        </div>
    </div>

    <!-- SECTION 8: VIP BOOKING MODAL WITH CONFETTI -->
    <div class="modal-overlay" id="vip-modal">
        <div class="modal-box">
            <button style="position: absolute; top: 20px; right: 20px; background: none; border: none; color: #9ca3af; font-size: 24px; cursor: pointer;" onclick="closeModal()">×</button>
            <div style="font-size: 26px; font-weight: 800; margin-bottom: 8px; color: #fff;">✨ VIP Reservation</div>
            <p style="color: #9ca3af; font-size: 14px; margin-bottom: 24px;">Secure your priority consultation with {business_name}.</p>
            <form onsubmit="handleBooking(event)">
                <input type="text" class="form-input" placeholder="Full Name *" required>
                <input type="tel" class="form-input" placeholder="Contact Phone / WhatsApp *" required>
                <input type="text" class="form-input" placeholder="Preferred Date & Time">
                <button type="submit" class="btn-vip" style="width: 100%; justify-content: center; margin-top: 10px;">🚀 Confirm VIP Booking & Celebrate</button>
            </form>
        </div>
    </div>

    <!-- Footer -->
    <footer style="padding: 60px; text-align: center; border-top: 1px solid var(--border); color: #64748b; font-size: 14px;">
        <p style="font-size: 18px; color: #fff; font-weight: 800; margin-bottom: 8px;">{business_name}</p>
        <p style="margin-bottom: 20px;">Premier Sanctuary in {city_title} | Phone: <strong style="color: var(--primary);">{phone}</strong></p>
        <p>© 2026 {business_name}. All rights reserved. Powered by LeadFlow.AI Shadow Infiltrator Pro Max.</p>
    </footer>

    <!-- Interactive Scripts & Robust Fallbacks -->
    <script>
        // 1. Scroll Reveal Engine (GSAP or Vanilla Fallback)
        function initReveal() {{
            if (typeof gsap !== 'undefined' && typeof ScrollTrigger !== 'undefined') {{
                gsap.registerPlugin(ScrollTrigger);
                document.querySelectorAll('.gsap-reveal').forEach(el => {{
                    gsap.fromTo(el, {{ opacity: 0, y: 40 }}, {{
                        opacity: 1, y: 0, duration: 0.8,
                        scrollTrigger: {{ trigger: el, start: "top 85%" }}
                    }});
                }});
            }} else {{
                // Vanilla Fallback for offline iframe preview
                const checkScroll = () => {{
                    document.querySelectorAll('.gsap-reveal').forEach(el => {{
                        if (el.getBoundingClientRect().top < window.innerHeight - 60) el.classList.add('active');
                    }});
                }};
                window.addEventListener('scroll', checkScroll);
                checkScroll();
            }}
        }}
        window.addEventListener('DOMContentLoaded', initReveal);

        // 2. Three.js / WebGL 3D Canvas Engine (With Pure Canvas Fallback)
        function init3D() {{
            const container = document.getElementById('three-canvas-container');
            if (typeof THREE !== 'undefined') {{
                const scene = new THREE.Scene();
                const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
                const renderer = new THREE.WebGLRenderer({{ alpha: true, antialias: true }});
                renderer.setSize(window.innerWidth, window.innerHeight);
                container.appendChild(renderer.domElement);

                // Create rotating 3D Torus Knot geometric sculpture
                const geometry = new THREE.TorusKnotGeometry(10, 3, 100, 16);
                const material = new THREE.MeshNormalMaterial({{ wireframe: true }});
                const torusKnot = new THREE.Mesh(geometry, material);
                scene.add(torusKnot);
                camera.position.z = 30;

                let mouseX = 0, mouseY = 0;
                window.addEventListener('mousemove', e => {{
                    mouseX = (e.clientX - window.innerWidth / 2) * 0.05;
                    mouseY = (e.clientY - window.innerHeight / 2) * 0.05;
                }});

                const animate = () => {{
                    requestAnimationFrame(animate);
                    torusKnot.rotation.x += 0.005;
                    torusKnot.rotation.y += 0.01;
                    torusKnot.position.x += (mouseX - torusKnot.position.x) * 0.05;
                    torusKnot.position.y += (-mouseY - torusKnot.position.y) * 0.05;
                    renderer.render(scene, camera);
                }};
                animate();

                window.addEventListener('resize', () => {{
                    camera.aspect = window.innerWidth / window.innerHeight;
                    camera.updateProjectionMatrix();
                    renderer.setSize(window.innerWidth, window.innerHeight);
                }});
            }} else {{
                // Vanilla HTML5 Canvas Fallback for offline preview without CDN
                const canvas = document.createElement('canvas');
                canvas.width = window.innerWidth; canvas.height = window.innerHeight;
                container.appendChild(canvas);
                const ctx = canvas.getContext('2d');
                let pts = Array.from({{length: 60}}, () => ({{x: Math.random()*canvas.width, y: Math.random()*canvas.height, vx: (Math.random()-0.5)*1.5, vy: (Math.random()-0.5)*1.5}}));
                const animFallback = () => {{
                    ctx.clearRect(0,0,canvas.width,canvas.height);
                    ctx.fillStyle = '{t["primary"]}';
                    pts.forEach(p => {{
                        p.x += p.vx; p.y += p.vy;
                        if(p.x<0||p.x>canvas.width) p.vx*=-1;
                        if(p.y<0||p.y>canvas.height) p.vy*=-1;
                        ctx.beginPath(); ctx.arc(p.x, p.y, 2, 0, Math.PI*2); ctx.fill();
                    }});
                    requestAnimationFrame(animFallback);
                }};
                animFallback();
            }}
        }}
        window.addEventListener('DOMContentLoaded', init3D);

        // 3. Interactive ROI Calculator
        function updateCalc() {{
            const val = document.getElementById('roi-slider').value;
            document.getElementById('calc-val-text').innerText = val;
            const res = (val * {t['calc_mult']}).toLocaleString();
            document.getElementById('calc-result-text').innerText = `$${{res}} / yr`;
        }}
        window.addEventListener('DOMContentLoaded', updateCalc);

        // 4. Before & After Slider
        function updateComparison(val) {{
            document.getElementById('comp-after-layer').style.width = `${{val}}%`;
        }}

        // 5. AI Chat Assistant
        function toggleChat() {{
            const win = document.getElementById('ai-chat');
            win.style.display = win.style.display === 'flex' ? 'none' : 'flex';
        }}
        function sendChat() {{
            const inp = document.getElementById('chat-input');
            const txt = inp.value.trim();
            if (!txt) return;
            const box = document.getElementById('chat-messages');
            box.innerHTML += `<div style="background: rgba(0,240,255,0.1); color: #fff; padding: 8px; border-radius: 8px; align-self: flex-end;">${{txt}}</div>`;
            inp.value = "";
            setTimeout(() => {{
                box.innerHTML += `<div style="background: rgba(255,255,255,0.05); padding: 8px; border-radius: 8px;">✨ That is a great question! For "{business_name}", our 3D AI suite automates that entire process. Would you like to click "Book VIP Consultation" above to secure a time?</div>`;
                box.scrollTop = box.scrollHeight;
            }}, 800);
        }}

        // 6. VIP Booking & Confetti Celebration
        function openModal() {{ document.getElementById('vip-modal').style.display = 'flex'; }}
        function closeModal() {{ document.getElementById('vip-modal').style.display = 'none'; }}
        function handleBooking(e) {{
            e.preventDefault();
            closeModal();
            if (typeof confetti !== 'undefined') {{
                confetti({{ particleCount: 150, spread: 80, origin: {{ y: 0.6 }} }});
            }} else {{
                alert("🎉 CONFETTI CELEBRATION! 🎉");
            }}
            setTimeout(() => {{
                alert("🎉 VIP RESERVATION CONFIRMED!\n\nYour priority session with {business_name} has been booked into the concierge system.");
            }}, 400);
        }}
    </script>
</body>
</html>
"""
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html_content.strip())

        return {
            "status": "success",
            "business_name": business_name,
            "category": category,
            "city": city,
            "phone": phone,
            "theme_applied": t['name'],
            "generated_filename": filename,
            "generated_filepath": filepath,
            "upsell_pitch": f"Hi {business_name} team,\n\nWe noticed your establishment in {city} has an exceptional reputation but currently lacks an active official website.\n\nUsing our autonomous AI engine (trained on UI/UX Pro Max rules), we built you a stunning 3D animated luxury website—complete with interactive holographic tilt cards, live motion graphics, and a VIP booking concierge.\n\nYou can own and deploy this instant site today for a one-time fee of $499.\n\nWould you like me to send over the live demo link to experience it?"
        }

if __name__ == "__main__":
    generator = ShadowInfiltrator()
    print("Testing Shadow Infiltrator Pro Max GSAP + Three.js Engine...")
    res = generator.generate_luxury_site("Apex Dental Lounge", "Dental Clinic", "Toronto", "+1 (416) 555-0199")
    print("Generated:", res["generated_filepath"])
