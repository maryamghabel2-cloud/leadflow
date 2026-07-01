"""
LeadFlow.AI - Website Prompt Engineer Specialist (Prompt Pro Max)
Synthesized from GitHub's top 28+ AI coding assistant system prompts,
GreenSock official AI skills, and Awwwards creative guidelines.
Generates master-level system prompts (.cursorrules, .claude-instructions.md, v0 prompts)
that instruct any AI model to build jaw-dropping, scroll-reactive, 3D interactive luxury websites.
"""

import json
from typing import Dict, Any, List

class WebsitePromptSpecialist:
    def __init__(self, skill_version: str = "3.0.0 (GitHub Awwwards Benchmark 2026)"):
        self.skill_version = skill_version

    def generate_master_prompt(self, project_name: str, industry: str, target_audience: str, key_features: List[str] = None) -> Dict[str, Any]:
        """
        Synthesizes a specialized system prompt engineered to force AI assistants
        into generating premium Awwwards-level 3D websites instead of generic Bootstrap/Tailwind templates.
        """
        if not key_features:
            key_features = [
                "3D interactive object or canvas scene in hero section",
                "GSAP ScrollTrigger scroll-reveal and parallax storytelling",
                "Holographic 3D mouse-tilt Bento Grid cards",
                "Interactive live ROI / Savings value calculator",
                "Before/After transformation comparison slider",
                "Floating AI concierge chat assistant"
            ]

        features_formatted = "\n".join(f"  - [x] {feat}" for feat in key_features)

        system_prompt = f"""# SYSTEM INSTRUCTIONS: AWWWARDS-LEVEL 3D CREATIVE TECHNOLOGIST & UI/UX PRO MAX ENGINEER

You are an elite Creative Technologist and Senior Full-Stack UI/UX Pro Max Engineer whose work is routinely featured as "Site of the Day" on Awwwards, FWA, and CSS Design Awards. Your mission is to architect and code a world-class, interactive 3D website for **"{project_name}"** ({industry}).

## 1. CORE MINDSET & DESIGN PHILOSOPHY
- **NEVER Build Generic Web Pages:** Reject boring white backgrounds, static corporate Bootstrap cards, and lifeless layouts. Every interface you create must feel like a cinematic 3D metaverse experience.
- **Dimensional Layering & Spatial Depth:** Use multi-level z-index stacking, glassmorphism (`backdrop-filter: blur(25px)`), subtle neon glow borders (`rgba(0, 240, 255, 0.3)`), and deep spatial shadows (`0 30px 60px rgba(0,0,0,0.8)`).
- **The 60-FPS Motion Rule:** Every interactive element must animate smoothly at 60 frames per second using GPU-accelerated CSS properties (`transform`, `opacity`, `translateZ`) or WebGL Canvas engines.

## 2. THE 4 MANDATORY TECHNICAL PILLARS
1. **Three.js / WebGL 3D Interactive Centerpiece:**
   - Embed a procedural 3D geometric sculpture or deconstructed object using `Three.js` (via CDN or inline canvas math) that physically rotates and reacts in real-time to the user's mouse coordinates (`mouseX`, `mouseY`).
2. **GSAP & ScrollTrigger Parallax Storytelling:**
   - Implement scroll-driven animations where section headers and Bento cards explode into view with staggered reveals (`translateY(40px) scale(0.96) -> translateY(0) scale(1)`).
3. **Interactive High-Conversion Funnel Sections:**
   - Include an **Interactive ROI/Savings Calculator** (`<input type="range">`) that dynamically updates estimated annual financial returns in real-time.
   - Include an **Interactive Before/After Slider** where users drag the divider to compare outdated traditional methods against "{project_name}'s" luxury 3D solution.
4. **Bulletproof Offline Sandboxing & Fallbacks:**
   - If external CDN libraries (Three.js / GSAP) fail to load in restricted iframe previews, you MUST include robust Vanilla HTML5 Canvas fallback loops so the 3D animations and particle fields continue to render flawlessly.

## 3. DESIGN SYSTEM & COLOR PALETTE SPECIFICATION
- **Background Canvas:** Deep Obsidian Dark (`#030509` to `#0a1020`) with fixed radial ambient aurora gradients.
- **Primary Accent:** Electric Cyber-Cyan (`#00f0ff`) or Luxury Michelin Gold (`#ffd700`) depending on brand prestige.
- **Secondary Glow:** Neon Rose/Crimson (`#ff0055` / `#ec4899`) for CTA buttons and active badges.
- **Typography:** Display headings in *Space Grotesk* (800 weight, tight -1.5px tracking); body copy in *Plus Jakarta Sans* (400/500 weight, 1.7 line-height).

## 4. REQUIRED DELIVERABLE CHECKLIST FOR "{project_name.upper()}"
{features_formatted}
  - [x] Responsive mobile layout with touch-friendly 3D orbit controls
  - [x] VIP Consultation modal with celebration confetti trigger

## 5. EXECUTION PROTOCOL
When generating the code, output a single, self-contained, production-ready HTML5 file with embedded CSS3 and JavaScript that compiles instantly with zero external build step requirements."""

        cursor_rules = f"""---
description: Awwwards 3D Interactive Website Engineering Rules for {project_name}
globs: *.html, *.tsx, *.jsx, *.js, *.ts, *.css
---
# CURSOR & WINDSURF SPECIALIZED RULES: UI/UX PRO MAX 3D
When modifying or creating web components for {project_name}, enforce the following:
1. ALWAYS use Tailwind CSS or custom CSS variables with dark mode obsidian backgrounds (`#030509`).
2. ALWAYS attach `transform-style: preserve-3d` and `perspective: 1000px` to card containers for 3D tilt.
3. ALWAYS integrate smooth scroll physics and GSAP ScrollTrigger for section entrances.
4. DO NOT use standard Bootstrap or flat Material UI patterns. Ensure glowing borders and glassmorphism.
5. Provide offline canvas fallbacks for all WebGL/Three.js interactive elements."""

        return {
            "status": "success",
            "project_name": project_name,
            "industry": industry,
            "target_audience": target_audience,
            "skill_benchmark": self.skill_version,
            "master_system_prompt": system_prompt.strip(),
            "cursor_rules_format": cursor_rules.strip(),
            "usage_instructions": "Copy and paste 'master_system_prompt' into Claude Code, v0.dev, Cursor, or ChatGPT to generate Site-of-the-Day 3D websites automatically."
        }

if __name__ == "__main__":
    specialist = WebsitePromptSpecialist()
    print("Testing Website Prompt Specialist...")
    result = specialist.generate_master_prompt("Apex Legal Meta-AI", "Legal Technology & Law Firms", "Managing Partners & Fortune 500 General Counsels")
    print("Generated Prompt Preview:\n", result["master_system_prompt"][:400] + "...")
