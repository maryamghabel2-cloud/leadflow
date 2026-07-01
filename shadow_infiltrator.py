"""
LeadFlow.AI - Shadow Infiltrator (Instant 3D Neon Website Generator)
Automatically generates Awwwards-style luxury 3D neon websites for local businesses
discovered without online presence, enabling instant $499 upsell pitches.
"""

import os
from typing import Dict, Any

class ShadowInfiltrator:
    def __init__(self, output_dir: str = "generated_sites"):
        self.output_dir = output_dir
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir, exist_ok=True)

    def generate_luxury_site(self, business_name: str, category: str, city: str, phone: str = "+1 (555) 019-2831") -> Dict[str, Any]:
        """
        Synthesizes a full HTML5 3D Neon Luxury Website tailored to the target local business.
        """
        slug = "".join(c if c.isalnum() else "_" for c in business_name.lower()).strip("_")
        filename = f"{slug}_luxury.html"
        filepath = os.path.join(self.output_dir, filename)

        category_title = category.title() if category else "Premium Services"
        
        html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{business_name} - Luxury {category_title} in {city}</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;600;700&display=swap');
        
        :root {{
            --bg: #030508;
            --neon-primary: #00f0ff;
            --neon-secondary: #ff007b;
            --neon-gold: #ffd700;
            --glass: rgba(255, 255, 255, 0.04);
            --border: rgba(0, 240, 255, 0.2);
        }}

        * {{
            margin: 0; padding: 0; box-sizing: border-box;
            font-family: 'Space Grotesk', sans-serif;
            scroll-behavior: smooth;
        }}

        body {{
            background-color: var(--bg);
            color: #ffffff;
            overflow-x: hidden;
            background-image: 
                radial-gradient(circle at 20% 30%, rgba(0, 240, 255, 0.12) 0%, transparent 40%),
                radial-gradient(circle at 80% 70%, rgba(255, 0, 123, 0.12) 0%, transparent 40%);
        }}

        /* 3D Floating Neon Sphere effect */
        .sphere-container {{
            position: absolute;
            top: 15%; right: 10%;
            width: 380px; height: 380px;
            pointer-events: none;
            z-index: 0;
            opacity: 0.6;
        }}
        .sphere {{
            width: 100%; height: 100%;
            border-radius: 50%;
            background: linear-gradient(135deg, var(--neon-primary), var(--neon-secondary));
            filter: blur(40px);
            animation: float3D 8s ease-in-out infinite alternate;
        }}
        @keyframes float3D {{
            0% {{ transform: translateY(0px) scale(1) rotate(0deg); }}
            100% {{ transform: translateY(-30px) scale(1.1) rotate(20deg); }}
        }}

        nav {{
            display: flex; justify-content: space-between; align-items: center;
            padding: 24px 60px;
            background: rgba(3, 5, 8, 0.8);
            backdrop-filter: blur(15px);
            border-bottom: 1px solid var(--border);
            position: sticky; top: 0; z-index: 100;
        }}

        .brand {{
            font-size: 24px; font-weight: 700;
            letter-spacing: -0.5px;
            background: linear-gradient(to right, #fff, var(--neon-primary));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-shadow: 0 0 20px rgba(0, 240, 255, 0.5);
        }}

        .nav-phone {{
            background: rgba(0, 240, 255, 0.1);
            border: 1px solid var(--neon-primary);
            color: var(--neon-primary);
            padding: 10px 20px;
            border-radius: 30px;
            text-decoration: none;
            font-weight: 600;
            font-size: 14px;
            box-shadow: 0 0 15px rgba(0, 240, 255, 0.3);
            transition: all 0.3s;
        }}
        .nav-phone:hover {{
            background: var(--neon-primary);
            color: #000;
            box-shadow: 0 0 25px var(--neon-primary);
        }}

        .hero {{
            padding: 120px 60px;
            max-width: 1200px;
            margin: 0 auto;
            position: relative;
            z-index: 10;
            min-height: 80vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
        }}

        .badge {{
            display: inline-block;
            background: rgba(255, 0, 123, 0.15);
            border: 1px solid var(--neon-secondary);
            color: var(--neon-secondary);
            padding: 6px 16px;
            border-radius: 20px;
            font-size: 13px;
            font-weight: 600;
            margin-bottom: 24px;
            text-transform: uppercase;
            letter-spacing: 2px;
        }}

        h1 {{
            font-size: 64px;
            font-weight: 700;
            line-height: 1.1;
            margin-bottom: 24px;
            max-width: 800px;
        }}
        h1 span {{
            color: var(--neon-primary);
            text-shadow: 0 0 30px rgba(0, 240, 255, 0.4);
        }}

        p.lead {{
            font-size: 20px;
            color: #94a3b8;
            max-width: 600px;
            margin-bottom: 40px;
            line-height: 1.6;
        }}

        .btn-group {{ display: flex; gap: 20px; }}

        .btn-neon {{
            padding: 16px 36px;
            background: linear-gradient(90deg, var(--neon-primary), #0088ff);
            color: #000;
            font-weight: 700;
            font-size: 16px;
            border: none;
            border-radius: 12px;
            cursor: pointer;
            box-shadow: 0 0 30px rgba(0, 240, 255, 0.5);
            transition: all 0.3s;
            text-decoration: none;
        }}
        .btn-neon:hover {{
            transform: translateY(-3px);
            box-shadow: 0 0 45px rgba(0, 240, 255, 0.8);
        }}

        /* 3D Glass Cards */
        .features {{
            padding: 80px 60px;
            max-width: 1200px;
            margin: 0 auto;
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
            gap: 30px;
            position: relative;
            z-index: 10;
        }}

        .card {{
            background: var(--glass);
            border: 1px solid var(--border);
            border-radius: 20px;
            padding: 40px;
            backdrop-filter: blur(20px);
            transition: all 0.4s;
            position: relative;
            overflow: hidden;
        }}
        .card:hover {{
            transform: translateY(-10px) rotateX(2deg) rotateY(2deg);
            border-color: var(--neon-primary);
            box-shadow: 0 20px 40px rgba(0, 240, 255, 0.15);
        }}
        .card h3 {{
            font-size: 22px;
            margin-bottom: 12px;
            color: #fff;
        }}
        .card p {{
            color: #94a3b8;
            font-size: 15px;
            line-height: 1.6;
        }}
        .icon-glow {{
            width: 50px; height: 50px;
            border-radius: 12px;
            background: rgba(0, 240, 255, 0.1);
            border: 1px solid var(--neon-primary);
            display: flex; align-items: center; justify-content: center;
            font-size: 24px;
            margin-bottom: 24px;
            box-shadow: 0 0 15px rgba(0, 240, 255, 0.3);
        }}

        /* Footer */
        footer {{
            margin-top: 100px;
            padding: 60px;
            text-align: center;
            border-top: 1px solid var(--border);
            color: #64748b;
            font-size: 14px;
        }}
        .demo-banner {{
            background: linear-gradient(90deg, #1e1b4b, #311042);
            border: 1px solid var(--neon-secondary);
            padding: 12px;
            text-align: center;
            font-size: 13px;
            color: #fff;
            font-weight: 600;
            letter-spacing: 1px;
        }}
    </style>
</head>
<body>

    <div class="demo-banner">
        ⚡ INSTANT LUXURY 3D DEMO CREATED BY LEADFLOW.AI AUTONOMOUS ENGINE FOR {business_name.upper()} ⚡
    </div>

    <nav>
        <div class="brand">{business_name}</div>
        <a href="tel:{phone}" class="nav-phone">📞 {phone}</a>
    </nav>

    <div class="sphere-container">
        <div class="sphere"></div>
    </div>

    <section class="hero">
        <span class="badge">#1 PREMIER {category_title.upper()} IN {city.upper()}</span>
        <h1>The Next Generation of <span>{category_title}</span> Excellence</h1>
        <p class="lead">We combine state-of-the-art precision, bespoke customer care, and luxury comfort to deliver an unforgettable experience in the heart of {city}.</p>
        <div class="btn-group">
            <a href="#book" class="btn-neon">Book Your VIP Consultation</a>
        </div>
    </section>

    <section class="features">
        <div class="card">
            <div class="icon-glow">✨</div>
            <h3>Bespoke {category_title} Quality</h3>
            <p>Every service is meticulously tailored to your exacting standards using award-winning techniques and ultra-premium materials.</p>
        </div>
        <div class="card">
            <div class="icon-glow">🏛️</div>
            <h3>Prime {city} Sanctuary</h3>
            <p>Conveniently located in central {city}, our facility is designed from the ground up to provide a relaxing, high-end environment.</p>
        </div>
        <div class="card">
            <div class="icon-glow">💎</div>
            <h3>Guaranteed Satisfaction</h3>
            <p>Our commitment to perfection has earned us the trust of discerning clients across the region. Experience the difference today.</p>
        </div>
    </section>

    <footer id="book">
        <p style="font-size: 18px; color: #fff; margin-bottom: 12px; font-weight: 600;">Ready to elevate your experience with {business_name}?</p>
        <p style="margin-bottom: 24px;">Call us directly at <strong style="color: var(--neon-primary);">{phone}</strong> or visit our studio in {city}.</p>
        <p>© 2026 {business_name}. All rights reserved. Designed & powered by LeadFlow.AI Shadow Infiltrator.</p>
    </footer>

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
            "generated_filename": filename,
            "generated_filepath": filepath,
            "html_preview_snippet": html_content[:400] + "...",
            "upsell_pitch": f"Hi {business_name} team, we noticed your business in {city} has fantastic reviews but no active website. We went ahead and built a luxury 3D neon website tailored for you. You can own and deploy this instant site today for just $499."
        }

if __name__ == "__main__":
    generator = ShadowInfiltrator()
    print("Testing Shadow Infiltrator 3D Website Generator...")
    res = generator.generate_luxury_site("Apex Dental Lounge", "Dental Clinic", "Toronto", "+1 (416) 555-0199")
    print("Generated:", res["generated_filepath"])
    print("Pitch:", res["upsell_pitch"])
