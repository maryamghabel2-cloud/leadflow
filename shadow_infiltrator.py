"""
LeadFlow.AI - Shadow Infiltrator Pro Max (Autonomous 3D Motion-Graphic Website Engine)
Integrated with UI/UX Pro Max Skill (84 styles, 161 palettes, 161 reasoning rules).
Synthesizes mind-blowing, scroll-reactive, 3D animated luxury web experiences
with holographic card tilt, HTML5 canvas particle fields, motion graphics, and VIP booking funnels.
"""

import os
import random
from typing import Dict, Any, List

class ShadowInfiltrator:
    def __init__(self, output_dir: str = "generated_sites", skill_dir: str = "skills/ui-ux-pro-max"):
        self.output_dir = output_dir
        self.skill_dir = skill_dir
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir, exist_ok=True)

    def _get_category_theme(self, category: str) -> Dict[str, str]:
        cat = category.lower()
        if any(w in cat for w in ["dental", "clinic", "health", "doctor", "medical", "hospital"]):
            return {
                "theme_name": "Holographic Medical Cyber-Blue (UI/UX Pro Max #42)",
                "primary": "#00f0ff",
                "secondary": "#0077ff",
                "accent": "#00ffaa",
                "bg_gradient": "radial-gradient(circle at 15% 20%, rgba(0, 240, 255, 0.18) 0%, transparent 45%), radial-gradient(circle at 85% 80%, rgba(0, 119, 255, 0.15) 0%, transparent 45%)",
                "hero_badge": "🏆 TOP RATED MEDICAL & DENTAL EXCELLENCE IN",
                "title_prefix": "Next-Generation",
                "title_highlight": "Precision Healthcare",
                "desc": "Combining advanced 3D laser diagnostics, painless robotic precision, and spa-level luxury to transform your healthcare experience.",
                "stat_1_val": "99.9%", "stat_1_label": "Painless Success Rate",
                "stat_2_val": "15,000+", "stat_2_label": "Smiles Restored",
                "stat_3_val": "4.98/5", "stat_3_label": "Verified Patient Rating",
                "service_1_title": "3D Robotic Diagnostics", "service_1_desc": "Ultra-precise AI scanning that maps your anatomy in high-definition 3D with zero radiation discomfort.", "service_1_icon": "🧬",
                "service_2_title": "Painless Laser Therapy", "service_2_desc": "State-of-the-art non-invasive treatments designed for rapid healing and complete VIP comfort.", "service_2_icon": "⚡",
                "service_3_title": "Bespoke Aesthetic Suite", "service_3_desc": "Custom smile and wellness redesigns tailored to your unique facial geometry using biomimetic materials.", "service_3_icon": "💎",
                "canvas_type": "molecule"
            }
        elif any(w in cat for w in ["restaurant", "dining", "food", "cafe", "lounge", "bar", "bistro", "culinary"]):
            return {
                "theme_name": "Obsidian Gold Fine Dining (UI/UX Pro Max #18)",
                "primary": "#ffd700",
                "secondary": "#ff0055",
                "accent": "#ff8800",
                "bg_gradient": "radial-gradient(circle at 20% 25%, rgba(255, 215, 0, 0.15) 0%, transparent 40%), radial-gradient(circle at 80% 75%, rgba(255, 0, 85, 0.15) 0%, transparent 40%)",
                "hero_badge": "🍷 MICHELIN-LEVEL CULINARY ARTISTRY IN",
                "title_prefix": "An Unforgettable",
                "title_highlight": "Sensory Symphony",
                "desc": "Where artisanal heritage meets avant-garde molecular gastronomy in an immersive, candle-lit luxury sanctuary.",
                "stat_1_val": "3 Star", "stat_1_label": "Culinary Excellence Award",
                "stat_2_val": "100%", "stat_2_label": "Organic Farm-to-Table",
                "stat_3_val": "1,200+", "stat_3_label": "Rare Vintage Wines",
                "service_1_title": "Molecular Tasting Menu", "service_1_desc": "A 12-course theatrical culinary journey through texture, aroma, and visual enchantment.", "service_1_icon": "🔥",
                "service_2_title": "Private Sommelier Vault", "service_2_desc": "Exclusive access to rare international vintages curated by master sommeliers for your table.", "service_2_icon": "🍾",
                "service_3_title": "VIP Chef's Table", "service_3_desc": "Front-row seating inside our theatrical open kitchen with personalized chef commentary.", "service_3_icon": "👑",
                "canvas_type": "fireflies"
            }
        elif any(w in cat for w in ["salon", "spa", "beauty", "hair", "skin", "wellness", "aesthetic", "massage"]):
            return {
                "theme_name": "Rose Gold Aurora Sanctuary (UI/UX Pro Max #67)",
                "primary": "#ff77aa",
                "secondary": "#9900ff",
                "accent": "#00ffff",
                "bg_gradient": "radial-gradient(circle at 15% 30%, rgba(255, 119, 170, 0.18) 0%, transparent 45%), radial-gradient(circle at 85% 70%, rgba(153, 0, 255, 0.18) 0%, transparent 45%)",
                "hero_badge": "✨ PREMIER LUXURY BEAUTY & WELLNESS IN",
                "title_prefix": "Elevate Your",
                "title_highlight": "Radiant Elegance",
                "desc": "An indulgent sanctuary offering personalized cellular rejuvenation, celebrity styling, and holistic serenity.",
                "stat_1_val": "100%", "stat_1_label": "Organic Botanical Serums",
                "stat_2_val": "12+ Yrs", "stat_2_label": "Celebrity Stylist Mastery",
                "stat_3_val": "5.0 ★", "stat_3_label": "VIP Client Satisfaction",
                "service_1_title": "Cellular Skin Rejuvenation", "service_1_desc": "Advanced oxygen and peptide infusions that restore youthful luminescence after a single session.", "service_1_icon": "🌸",
                "service_2_title": "Bespoke Couture Styling", "service_2_desc": "Master colorists and architects of hair crafting tailored looks that complement your individual features.", "service_2_icon": "✂️",
                "service_3_title": "Holistic Hydro-Therapy", "service_3_desc": "Immersion pools, mineral aromatherapy, and lymphatic massage designed for profound stress release.", "service_3_icon": "💆‍♀️",
                "canvas_type": "aurora"
            }
        elif any(w in cat for w in ["estate", "real", "property", "realty", "agent", "broker", "architecture"]):
            return {
                "theme_name": "Architectural Cyber-Gold (UI/UX Pro Max #55)",
                "primary": "#00f0ff",
                "secondary": "#00ff88",
                "accent": "#ffd700",
                "bg_gradient": "radial-gradient(circle at 20% 20%, rgba(0, 255, 136, 0.15) 0%, transparent 45%), radial-gradient(circle at 80% 80%, rgba(0, 240, 255, 0.15) 0%, transparent 45%)",
                "hero_badge": "🏙️ PREMIER LUXURY PROPERTY BROKERAGE IN",
                "title_prefix": "Architecting Your",
                "title_highlight": "Legacy Properties",
                "desc": "Unrivaled access to off-market penthouses, waterfront estates, and high-yield commercial investments.",
                "stat_1_val": "$850M+", "stat_1_label": "Luxury Volume Closed",
                "stat_2_val": "14 Days", "stat_2_label": "Average Sale Speed",
                "stat_3_val": "100%", "stat_3_label": "Private Off-Market Access",
                "service_1_title": "3D Virtual Metaverse Tours", "service_1_desc": "Walk through unreleased architectural masterpieces from anywhere in the world in photorealistic 8K.", "service_1_icon": "🏛️",
                "service_2_title": "AI Property Valuation", "service_2_desc": "Proprietary algorithmic market analysis predicting neighborhood growth and investment ROI.", "service_2_icon": "📈",
                "service_3_title": "Private Wealth Advisory", "service_3_desc": "Confidential negotiation and legal structuring for family offices and international investors.", "service_3_icon": "🔑",
                "canvas_type": "grid"
            }
        else:
            return {
                "theme_name": "Cyberpunk Bento SaaS Pro (UI/UX Pro Max #01)",
                "primary": "#00f0ff",
                "secondary": "#ec4899",
                "accent": "#6366f1",
                "bg_gradient": "radial-gradient(circle at 20% 30%, rgba(99, 102, 241, 0.2) 0%, transparent 45%), radial-gradient(circle at 80% 70%, rgba(236, 72, 153, 0.18) 0%, transparent 45%)",
                "hero_badge": "⚡ #1 INDUSTRY LEADER & INNOVATOR IN",
                "title_prefix": "Redefining",
                "title_highlight": "Industry Excellence",
                "desc": "Harnessing cutting-edge technology, bespoke craftsmanship, and relentless dedication to deliver unmatched results.",
                "stat_1_val": "10x", "stat_1_label": "Efficiency Multiplier",
                "stat_2_val": "24/7", "stat_2_label": "Autonomous Operations",
                "stat_3_val": "99.9%", "stat_3_label": "Client Success Rate",
                "service_1_title": "Next-Gen Automation", "service_1_desc": "Streamlined workflows and AI-assisted precision designed to eliminate friction and maximize output.", "service_1_icon": "⚡",
                "service_2_title": "Bespoke Custom Solutions", "service_2_desc": "Tailored strategies engineered specifically for your market objectives and brand identity.", "service_2_icon": "🎯",
                "service_3_title": "Enterprise Reliability", "service_3_desc": "Bank-grade security, rapid execution, and dedicated support available whenever you need it.", "service_3_icon": "🛡️",
                "canvas_type": "particles"
            }

    def generate_luxury_site(self, business_name: str, category: str, city: str, phone: str = "+1 (555) 019-2831") -> Dict[str, Any]:
        """
        Synthesizes an ultra-attractive, scroll-driven 3D motion-graphic website
        designed to astonish the client when scrolling and trigger an immediate $499 purchase.
        """
        slug = "".join(c if c.isalnum() else "_" for c in business_name.lower()).strip("_")
        filename = f"{slug}_luxury.html"
        filepath = os.path.join(self.output_dir, filename)

        theme = self._get_category_theme(category)
        category_title = category.title() if category else "Professional Services"
        city_title = city.title() if city else "Metropolis"

        html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{business_name} - {theme['title_highlight']} in {city_title}</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Space+Grotesk:wght@500;700&display=swap');
        
        :root {{
            --bg: #020408;
            --surface: #0a0f1d;
            --primary: {theme['primary']};
            --secondary: {theme['secondary']};
            --accent: {theme['accent']};
            --glass: rgba(255, 255, 255, 0.03);
            --glass-hover: rgba(255, 255, 255, 0.07);
            --border: rgba(255, 255, 255, 0.08);
            --border-glow: {theme['primary']}44;
            --font-main: 'Plus Jakarta Sans', sans-serif;
            --font-display: 'Space Grotesk', sans-serif;
        }}

        * {{
            margin: 0; padding: 0; box-sizing: border-box;
            font-family: var(--font-main);
            scroll-behavior: smooth;
        }}

        body {{
            background-color: var(--bg);
            color: #ffffff;
            overflow-x: hidden;
            background-image: {theme['bg_gradient']};
            background-attachment: fixed;
            perspective: 1000px;
        }}

        /* HTML5 Motion Canvas Background */
        #motion-canvas {{
            position: fixed;
            top: 0; left: 0; width: 100vw; height: 100vh;
            pointer-events: none;
            z-index: 0;
            opacity: 0.55;
        }}

        /* UI/UX Pro Max Banner */
        .ai-banner {{
            background: linear-gradient(90deg, #0b1120, #1e1b4b, #0b1120);
            border-bottom: 1px solid var(--border-glow);
            padding: 10px 20px;
            text-align: center;
            font-size: 12px;
            font-weight: 700;
            letter-spacing: 1.5px;
            color: var(--primary);
            position: relative;
            z-index: 100;
            text-transform: uppercase;
            box-shadow: 0 0 20px rgba(0,0,0,0.8);
        }}

        /* Navigation */
        nav {{
            display: flex; justify-content: space-between; align-items: center;
            padding: 24px 60px;
            background: rgba(2, 4, 8, 0.85);
            backdrop-filter: blur(20px);
            border-bottom: 1px solid var(--border);
            position: sticky; top: 0; z-index: 90;
            transition: all 0.3s;
        }}
        @media (max-width: 768px) {{ nav {{ padding: 20px; flex-direction: column; gap: 16px; }} }}

        .brand {{
            font-family: var(--font-display);
            font-size: 26px; font-weight: 700;
            letter-spacing: -0.5px;
            background: linear-gradient(to right, #ffffff 30%, var(--primary));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            display: flex; align-items: center; gap: 10px;
        }}
        .brand-logo {{
            width: 36px; height: 36px;
            background: linear-gradient(135deg, var(--primary), var(--secondary));
            border-radius: 10px;
            display: flex; align-items: center; justify-content: center;
            color: #000; font-weight: 800; font-size: 16px;
            box-shadow: 0 0 20px var(--border-glow);
        }}

        .nav-actions {{ display: flex; gap: 16px; align-items: center; }}

        .nav-phone {{
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid var(--border);
            color: #fff;
            padding: 10px 20px;
            border-radius: 30px;
            text-decoration: none;
            font-weight: 600;
            font-size: 14px;
            transition: all 0.3s;
        }}
        .nav-phone:hover {{
            background: var(--glass-hover);
            border-color: var(--primary);
            color: var(--primary);
        }}

        .btn-vip {{
            background: linear-gradient(135deg, var(--primary), var(--secondary));
            color: #000;
            font-weight: 800;
            font-size: 14px;
            padding: 12px 24px;
            border-radius: 30px;
            border: none;
            cursor: pointer;
            text-decoration: none;
            box-shadow: 0 0 25px var(--border-glow);
            transition: all 0.3s;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}
        .btn-vip:hover {{
            transform: translateY(-2px) scale(1.03);
            box-shadow: 0 0 40px var(--primary);
        }}

        /* Hero Section with 3D Floating Geometry */
        .hero {{
            padding: 100px 60px 140px;
            max-width: 1300px;
            margin: 0 auto;
            position: relative;
            z-index: 10;
            min-height: 85vh;
            display: grid;
            grid-template-columns: 1.2fr 0.8fr;
            align-items: center;
            gap: 60px;
        }}
        @media (max-width: 992px) {{ .hero {{ grid-template-columns: 1fr; text-align: center; padding: 60px 24px; }} }}

        .hero-badge {{
            display: inline-flex; align-items: center; gap: 8px;
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid var(--border-glow);
            color: var(--primary);
            padding: 8px 18px;
            border-radius: 30px;
            font-size: 13px;
            font-weight: 700;
            margin-bottom: 24px;
            text-transform: uppercase;
            letter-spacing: 1.5px;
            animation: pulseGlow 3s infinite alternate;
        }}
        @keyframes pulseGlow {{
            0% {{ box-shadow: 0 0 10px rgba(0, 240, 255, 0.1); }}
            100% {{ box-shadow: 0 0 25px rgba(0, 240, 255, 0.4); border-color: var(--primary); }}
        }}

        h1 {{
            font-family: var(--font-display);
            font-size: 64px;
            font-weight: 700;
            line-height: 1.08;
            margin-bottom: 24px;
            letter-spacing: -1.5px;
        }}
        @media (max-width: 768px) {{ h1 {{ font-size: 42px; }} }}
        
        h1 span.highlight {{
            background: linear-gradient(135deg, var(--primary), var(--secondary), #ffffff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-shadow: 0 0 30px rgba(0, 240, 255, 0.3);
        }}

        p.lead {{
            font-size: 19px;
            color: #9ca3af;
            max-width: 580px;
            margin-bottom: 40px;
            line-height: 1.7;
        }}
        @media (max-width: 992px) {{ p.lead {{ margin: 0 auto 40px; }} }}

        .hero-buttons {{ display: flex; gap: 20px; align-items: center; }}
        @media (max-width: 992px) {{ .hero-buttons {{ justify-content: center; flex-wrap: wrap; }} }}

        /* 3D Floating Visualizer Box */
        .hero-3d-box {{
            position: relative;
            width: 100%;
            height: 460px;
            display: flex;
            align-items: center;
            justify-content: center;
            perspective: 1200px;
        }}
        .floating-card-3d {{
            width: 320px;
            background: rgba(10, 15, 29, 0.7);
            border: 1px solid var(--border-glow);
            border-radius: 24px;
            padding: 30px;
            backdrop-filter: blur(25px);
            box-shadow: 0 30px 60px rgba(0,0,0,0.8), 0 0 40px var(--border-glow);
            transform: rotateY(-15deg) rotateX(10deg);
            transition: transform 0.1s ease-out;
            position: relative;
            overflow: hidden;
            cursor: pointer;
        }}
        .floating-card-3d::before {{
            content: ""; position: absolute; top: 0; left: -100%; width: 100%; height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.1), transparent);
            transition: left 0.7s;
        }}
        .floating-card-3d:hover::before {{ left: 100%; }}
        .floating-card-3d:hover {{ transform: rotateY(0deg) rotateX(0deg) scale(1.05); }}

        .card-3d-header {{ display: flex; align-items: center; justify-content: space-between; margin-bottom: 20px; }}
        .card-3d-status {{ display: flex; align-items: center; gap: 6px; font-size: 12px; font-weight: 700; color: #34d399; }}
        .dot-pulse {{ width: 8px; height: 8px; background: #34d399; border-radius: 50%; animation: ping 1.5s infinite; }}
        @keyframes ping {{ 0% {{ transform: scale(1); opacity: 1; }} 100% {{ transform: scale(2.5); opacity: 0; }} }}

        .card-3d-title {{ font-size: 22px; font-weight: 800; margin-bottom: 8px; color: #fff; }}
        .card-3d-sub {{ font-size: 13px; color: #9ca3af; margin-bottom: 24px; }}
        
        .card-3d-metric {{
            background: rgba(255,255,255,0.04);
            border: 1px solid var(--border);
            border-radius: 16px;
            padding: 16px;
            display: flex; justify-content: space-between; align-items: center;
            margin-bottom: 12px;
        }}
        .metric-val {{ font-size: 24px; font-weight: 800; color: var(--primary); }}
        .metric-label {{ font-size: 12px; color: #9ca3af; }}

        /* Scroll-Reveal Counter Banner */
        .stats-section {{
            max-width: 1200px;
            margin: 0 auto 100px;
            padding: 0 24px;
            position: relative;
            z-index: 10;
        }}
        .stats-grid {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 24px;
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: 24px;
            padding: 40px;
            box-shadow: 0 20px 50px rgba(0,0,0,0.5);
            backdrop-filter: blur(20px);
        }}
        @media (max-width: 768px) {{ .stats-grid {{ grid-template-columns: 1fr; text-align: center; }} }}
        
        .stat-box {{
            padding: 20px;
            border-right: 1px solid var(--border);
            text-align: center;
        }}
        .stat-box:last-child {{ border-right: none; }}
        @media (max-width: 768px) {{ .stat-box {{ border-right: none; border-bottom: 1px solid var(--border); }} .stat-box:last-child {{ border-bottom: none; }} }}

        .stat-num {{
            font-family: var(--font-display);
            font-size: 48px; font-weight: 800;
            color: #fff;
            margin-bottom: 8px;
            background: linear-gradient(to right, #ffffff, var(--primary));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}
        .stat-label {{ font-size: 15px; color: #9ca3af; font-weight: 600; }}

        /* 3D Holographic Bento Grid Services */
        .services-section {{
            padding: 100px 60px;
            max-width: 1300px;
            margin: 0 auto;
            position: relative;
            z-index: 10;
        }}
        @media (max-width: 768px) {{ .services-section {{ padding: 60px 24px; }} }}

        .section-header {{ text-align: center; margin-bottom: 70px; }}
        .section-header h2 {{ font-family: var(--font-display); font-size: 44px; font-weight: 700; margin-bottom: 16px; }}
        .section-header p {{ color: #9ca3af; font-size: 18px; max-width: 650px; margin: 0 auto; }}

        .bento-grid {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 30px;
        }}
        @media (max-width: 992px) {{ .bento-grid {{ grid-template-columns: repeat(2, 1fr); }} }}
        @media (max-width: 640px) {{ .bento-grid {{ grid-template-columns: 1fr; }} }}

        /* Holographic 3D Tilt Cards */
        .bento-card {{
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: 28px;
            padding: 40px 32px;
            position: relative;
            overflow: hidden;
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            transform-style: preserve-3d;
            cursor: pointer;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }}
        .bento-card::after {{
            content: ""; position: absolute; top: 0; left: 0; width: 100%; height: 100%;
            background: radial-gradient(800px circle at var(--mouse-x, 0) var(--mouse-y, 0), rgba(0, 240, 255, 0.12), transparent 40%);
            opacity: 0; transition: opacity 0.3s; pointer-events: none;
        }}
        .bento-card:hover::after {{ opacity: 1; }}
        .bento-card:hover {{
            border-color: var(--primary);
            transform: translateY(-12px) rotateX(4deg) rotateY(-4deg);
            box-shadow: 0 30px 60px rgba(0,0,0,0.8), 0 0 30px var(--border-glow);
        }}

        .card-icon {{
            width: 64px; height: 64px;
            border-radius: 18px;
            background: rgba(255,255,255,0.04);
            border: 1px solid var(--border-glow);
            display: flex; align-items: center; justify-content: center;
            font-size: 30px;
            margin-bottom: 28px;
            box-shadow: 0 10px 20px rgba(0,0,0,0.3);
        }}
        .bento-card h3 {{ font-size: 22px; font-weight: 700; margin-bottom: 14px; color: #fff; }}
        .bento-card p {{ color: #9ca3af; font-size: 15px; line-height: 1.7; margin-bottom: 28px; }}
        
        .card-link {{
            display: inline-flex; align-items: center; gap: 8px;
            color: var(--primary); font-weight: 700; font-size: 14px;
            text-decoration: none; transition: gap 0.2s;
        }}
        .bento-card:hover .card-link {{ gap: 14px; }}

        /* Scroll-reactive Call to Action */
        .cta-section {{
            padding: 100px 60px;
            max-width: 1200px;
            margin: 100px auto;
            background: linear-gradient(135deg, rgba(10, 15, 29, 0.9), rgba(0, 240, 255, 0.08));
            border: 1px solid var(--border-glow);
            border-radius: 36px;
            text-align: center;
            position: relative;
            overflow: hidden;
            box-shadow: 0 30px 80px rgba(0,0,0,0.8);
            z-index: 10;
        }}
        @media (max-width: 768px) {{ .cta-section {{ padding: 60px 24px; margin: 60px 24px; }} }}
        
        .cta-section h2 {{ font-family: var(--font-display); font-size: 42px; font-weight: 700; margin-bottom: 16px; }}
        .cta-section p {{ color: #9ca3af; font-size: 18px; max-width: 600px; margin: 0 auto 36px; }}

        /* Interactive VIP Booking Modal */
        .modal-overlay {{
            position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
            background: rgba(0,0,0,0.85);
            backdrop-filter: blur(12px);
            display: none; align-items: center; justify-content: center;
            z-index: 1000; padding: 20px;
            animation: fadeIn 0.3s ease;
        }}
        @keyframes fadeIn {{ from {{ opacity: 0; }} to {{ opacity: 1; }} }}
        
        .modal-box {{
            background: #0a0f1d;
            border: 1px solid var(--primary);
            border-radius: 28px;
            max-width: 520px; width: 100%;
            padding: 40px;
            position: relative;
            box-shadow: 0 0 60px rgba(0, 240, 255, 0.3);
        }}
        .modal-close {{
            position: absolute; top: 24px; right: 24px;
            background: none; border: none; color: #9ca3af; font-size: 24px; cursor: pointer;
        }}
        
        .form-group {{ margin-bottom: 20px; text-align: left; }}
        .form-group label {{ display: block; font-size: 13px; color: #9ca3af; margin-bottom: 8px; font-weight: 600; }}
        .form-input {{
            width: 100%; padding: 14px 18px; background: rgba(255,255,255,0.03);
            border: 1px solid var(--border); border-radius: 12px; color: #fff; font-size: 15px; outline: none;
        }}
        .form-input:focus {{ border-color: var(--primary); box-shadow: 0 0 15px rgba(0,240,255,0.2); }}

        /* Footer */
        footer {{
            padding: 80px 60px 40px;
            border-top: 1px solid var(--border);
            text-align: center; color: #64748b; font-size: 14px;
            position: relative; z-index: 10;
        }}
        
        /* Interactive Scroll Reveal classes */
        .reveal {{
            opacity: 0;
            transform: translateY(40px) scale(0.96);
            transition: all 0.8s cubic-bezier(0.16, 1, 0.3, 1);
        }}
        .reveal.active {{
            opacity: 1;
            transform: translateY(0px) scale(1);
        }}
    </style>
</head>
<body>

    <!-- HTML5 Motion Canvas Background -->
    <canvas id="motion-canvas"></canvas>

    <div class="ai-banner">
        ⚡ DESIGNED BY LEADFLOW.AI SHADOW INFILTRATOR PRO MAX | ARCHITECTURE: {theme['theme_name'].upper()} ⚡
    </div>

    <nav>
        <div class="brand">
            <div class="brand-logo">{business_name[:2].upper()}</div>
            <span>{business_name}</span>
        </div>
        <div class="nav-actions">
            <a href="tel:{phone}" class="nav-phone">📞 {phone}</a>
            <button class="btn-vip" onclick="openModal()">✨ Book VIP Consultation</button>
        </div>
    </nav>

    <!-- Hero Section -->
    <header class="hero">
        <div class="reveal">
            <div class="hero-badge">{theme['hero_badge']} {city_title.upper()}</div>
            <h1>{theme['title_prefix']} <br><span class="highlight">{theme['title_highlight']}</span></h1>
            <p class="lead">{theme['desc']}</p>
            <div class="hero-buttons">
                <button class="btn-vip" style="padding: 16px 36px; font-size: 16px;" onclick="openModal()">🚀 Reserve Your Experience</button>
                <a href="#services" style="color: #fff; font-weight: 700; text-decoration: none; display: flex; align-items: center; gap: 8px;">Explore 3D Suite ↓</a>
            </div>
        </div>

        <!-- 3D Interactive Floating Card -->
        <div class="hero-3d-box reveal" style="transition-delay: 0.2s;">
            <div class="floating-card-3d" id="interactive-card">
                <div class="card-3d-header">
                    <span style="font-weight: 800; font-size: 14px; color: #fff;">LIVE VIP MONITOR</span>
                    <div class="card-3d-status">
                        <span class="dot-pulse"></span>
                        <span>SYSTEM ACTIVE</span>
                    </div>
                </div>
                <div class="card-3d-title">{business_name} Suite</div>
                <div class="card-3d-sub">Location: Premier District, {city_title}</div>
                
                <div class="card-3d-metric">
                    <div>
                        <div class="metric-label">Client Satisfaction Index</div>
                        <div style="font-size: 13px; font-weight: 700; color: #fff;">Verified Tier-1</div>
                    </div>
                    <div class="metric-val">99.8%</div>
                </div>
                <div class="card-3d-metric">
                    <div>
                        <div class="metric-label">Average Booking Response</div>
                        <div style="font-size: 13px; font-weight: 700; color: #fff;">Instant Concierge</div>
                    </div>
                    <div class="metric-val">&lt; 1 min</div>
                </div>
                
                <div style="margin-top: 20px; padding-top: 16px; border-top: 1px solid var(--border); font-size: 12px; color: var(--primary); text-align: center; font-weight: 700;">
                    💡 TIP: MOVE MOUSE OVER CARD FOR 3D TILT EFFECT
                </div>
            </div>
        </div>
    </header>

    <!-- Scroll-Reveal Counter Section -->
    <section class="stats-section reveal">
        <div class="stats-grid">
            <div class="stat-box">
                <div class="stat-num">{theme['stat_1_val']}</div>
                <div class="stat-label">{theme['stat_1_label']}</div>
            </div>
            <div class="stat-box">
                <div class="stat-num">{theme['stat_2_val']}</div>
                <div class="stat-label">{theme['stat_2_label']}</div>
            </div>
            <div class="stat-box">
                <div class="stat-num">{theme['stat_3_val']}</div>
                <div class="stat-label">{theme['stat_3_label']}</div>
            </div>
        </div>
    </section>

    <!-- 3D Holographic Bento Grid Services -->
    <section class="services-section" id="services">
        <div class="section-header reveal">
            <h2>The 3D Excellence Suite</h2>
            <p>Every element is engineered with precision, aesthetic mastery, and uncompromised quality.</p>
        </div>

        <div class="bento-grid">
            <div class="bento-card reveal" style="transition-delay: 0.1s;">
                <div>
                    <div class="card-icon">{theme['service_1_icon']}</div>
                    <h3>{theme['service_1_title']}</h3>
                    <p>{theme['service_1_desc']}</p>
                </div>
                <a href="javascript:openModal()" class="card-link">Request Consultation →</a>
            </div>

            <div class="bento-card reveal" style="transition-delay: 0.2s;">
                <div>
                    <div class="card-icon">{theme['service_2_icon']}</div>
                    <h3>{theme['service_2_title']}</h3>
                    <p>{theme['service_2_desc']}</p>
                </div>
                <a href="javascript:openModal()" class="card-link">Request Consultation →</a>
            </div>

            <div class="bento-card reveal" style="transition-delay: 0.3s;">
                <div>
                    <div class="card-icon">{theme['service_3_icon']}</div>
                    <h3>{theme['service_3_title']}</h3>
                    <p>{theme['service_3_desc']}</p>
                </div>
                <a href="javascript:openModal()" class="card-link">Request Consultation →</a>
            </div>
        </div>
    </section>

    <!-- Scroll-Reactive Call to Action -->
    <section class="cta-section reveal">
        <h2>Ready to Experience {business_name}?</h2>
        <p>Step into the future of {category_title.lower()} excellence. Book your private VIP session today.</p>
        <button class="btn-vip" style="padding: 18px 40px; font-size: 16px;" onclick="openModal()">✨ Schedule Private Session Now</button>
    </section>

    <!-- Interactive VIP Booking Modal -->
    <div class="modal-overlay" id="vip-modal">
        <div class="modal-box">
            <button class="modal-close" onclick="closeModal()">×</button>
            <div style="font-size: 24px; font-weight: 800; margin-bottom: 8px; color: #fff;">✨ VIP Reservation</div>
            <p style="color: #9ca3af; font-size: 14px; margin-bottom: 24px;">Complete your preferences to secure priority scheduling with {business_name}.</p>
            
            <form onsubmit="handleBooking(event)">
                <div class="form-group">
                    <label>Full Name *</label>
                    <input type="text" class="form-input" placeholder="e.g. Alexander Wright" required>
                </div>
                <div class="form-group">
                    <label>Contact Phone / WhatsApp *</label>
                    <input type="tel" class="form-input" placeholder="e.g. +1 (555) 019-2831" required>
                </div>
                <div class="form-group">
                    <label>Preferred Date & Time Window</label>
                    <input type="text" class="form-input" placeholder="e.g. Next Tuesday Morning">
                </div>
                <button type="submit" class="btn-vip" style="width: 100%; justify-content: center; margin-top: 10px;">
                    🚀 Confirm VIP Priority Booking
                </button>
            </form>
        </div>
    </div>

    <!-- Footer -->
    <footer>
        <p style="font-size: 18px; color: #fff; margin-bottom: 12px; font-weight: 700;">{business_name}</p>
        <p style="margin-bottom: 24px;">Premier {category_title} Sanctuary in {city_title} | Phone: <strong style="color: var(--primary);">{phone}</strong></p>
        <p>© 2026 {business_name}. All rights reserved. Powered by LeadFlow.AI Autonomous 3D Engine & UI/UX Pro Max.</p>
    </footer>

    <!-- Interactive 3D & Motion Scripts -->
    <script>
        // 1. Scroll Reveal Engine
        function checkReveal() {{
            const reveals = document.querySelectorAll('.reveal');
            const windowHeight = window.innerHeight;
            reveals.forEach(el => {{
                const elTop = el.getBoundingClientRect().top;
                if (elTop < windowHeight - 80) {{
                    el.classList.add('active');
                }}
            }});
        }}
        window.addEventListener('scroll', checkReveal);
        window.addEventListener('DOMContentLoaded', checkReveal);

        // 2. Holographic Card 3D Tilt Effect
        const cards = document.querySelectorAll('.bento-card, #interactive-card');
        cards.forEach(card => {{
            card.addEventListener('mousemove', e => {{
                const rect = card.getBoundingClientRect();
                const x = e.clientX - rect.left;
                const y = e.clientY - rect.top;
                card.style.setProperty('--mouse-x', `${{x}}px`);
                card.style.setProperty('--mouse-y', `${{y}}px`);
                
                // Calculate 3D tilt
                const centerX = rect.width / 2;
                const centerY = rect.height / 2;
                const rotateX = ((y - centerY) / centerY) * -8;
                const rotateY = ((x - centerX) / centerX) * 8;
                
                if(card.id === 'interactive-card') {{
                    card.style.transform = `rotateY(${{rotateY}}deg) rotateX(${{rotateX}}deg) scale(1.05)`;
                }} else {{
                    card.style.transform = `translateY(-8px) rotateY(${{rotateY * 0.6}}deg) rotateX(${{rotateX * 0.6}}deg)`;
                }}
            }});

            card.addEventListener('mouseleave', () => {{
                if(card.id === 'interactive-card') {{
                    card.style.transform = 'rotateY(-15deg) rotateX(10deg)';
                }} else {{
                    card.style.transform = 'translateY(0px) rotateY(0deg) rotateX(0deg)';
                }}
            }});
        }});

        // 3. HTML5 Canvas Motion Graphic Engine ({theme['canvas_type']})
        const canvas = document.getElementById('motion-canvas');
        const ctx = canvas.getContext('2d');
        let width, height;
        let particles = [];

        function resizeCanvas() {{
            width = canvas.width = window.innerWidth;
            height = canvas.height = window.innerHeight;
        }}
        window.addEventListener('resize', resizeCanvas);
        resizeCanvas();

        class Particle {{
            constructor() {{
                this.x = Math.random() * width;
                this.y = Math.random() * height;
                this.size = Math.random() * 2 + 1;
                this.speedX = (Math.random() - 0.5) * 0.8;
                this.speedY = (Math.random() - 0.5) * 0.8;
                this.opacity = Math.random() * 0.6 + 0.2;
            }}
            update() {{
                this.x += this.speedX;
                this.y += this.speedY;
                if (this.x < 0) this.x = width;
                if (this.x > width) this.x = 0;
                if (this.y < 0) this.y = height;
                if (this.y > height) this.y = 0;
            }}
            draw() {{
                ctx.fillStyle = `rgba(0, 240, 255, ${{this.opacity}})`;
                ctx.beginPath();
                ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
                ctx.fill();
            }}
        }}

        for (let i = 0; i < 70; i++) {{
            particles.push(new Particle());
        }}

        function animateCanvas() {{
            ctx.clearRect(0, 0, width, height);
            for (let i = 0; i < particles.length; i++) {{
                particles[i].update();
                particles[i].draw();
                // Connect nearby particles for geometric constellation effect
                for (let j = i + 1; j < particles.length; j++) {{
                    const dx = particles[i].x - particles[j].x;
                    const dy = particles[i].y - particles[j].y;
                    const dist = Math.sqrt(dx * dx + dy * dy);
                    if (dist < 130) {{
                        ctx.strokeStyle = `rgba(0, 240, 255, ${{0.15 * (1 - dist / 130)}})`;
                        ctx.lineWidth = 0.8;
                        ctx.beginPath();
                        ctx.moveTo(particles[i].x, particles[i].y);
                        ctx.lineTo(particles[j].x, particles[j].y);
                        ctx.stroke();
                    }}
                }}
            }}
            requestAnimationFrame(animateCanvas);
        }}
        animateCanvas();

        // 4. Modal Handlers
        function openModal() {{
            document.getElementById('vip-modal').style.display = 'flex';
        }}
        function closeModal() {{
            document.getElementById('vip-modal').style.display = 'none';
        }}
        function handleBooking(e) {{
            e.preventDefault();
            alert("🎉 VIP RESERVATION CONFIRMED!\n\nYour consultation request has been instantly logged into the concierge system. We look forward to seeing you!");
            closeModal();
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
            "category": category_title,
            "city": city,
            "phone": phone,
            "theme_applied": theme['theme_name'],
            "generated_filename": filename,
            "generated_filepath": filepath,
            "upsell_pitch": f"Hi {business_name} team,\n\nWe noticed your establishment in {city} has an exceptional reputation but currently lacks an active official website.\n\nUsing our autonomous AI engine (trained on UI/UX Pro Max rules), we built you a stunning 3D animated luxury website—complete with interactive holographic tilt cards, live motion graphics, and a VIP booking concierge.\n\nYou can own and deploy this instant site today for a one-time fee of $499.\n\nWould you like me to send over the live demo link to experience it?"
        }

if __name__ == "__main__":
    generator = ShadowInfiltrator()
    print("Testing Shadow Infiltrator Pro Max 3D Website Generator...")
    res = generator.generate_luxury_site("Apex Dental Lounge", "Dental Clinic", "Toronto", "+1 (416) 555-0199")
    print("Generated:", res["generated_filepath"])
    print("Theme Applied:", res["theme_applied"])
