"""
LeadFlow.AI - Website Prompt Engineer Specialist (Prompt Pro Max v5.0)
Actively integrates the Master AI Web Engineering Super Stack:
- /impeccable & taste skill (Zero AI slop, organic palettes, immaculate visual hierarchy)
- 21st.dev registry (AI-agent component intelligence)
- /motion.dev & Framer Motion (60-FPS spring physics & gesture recognition)
- Higgsfield MCP (Cinematic 360° video generation)
- GSD, Superpowers, Context mode, Cloud mem, and /ultra-review inspection gates.
"""

import json
from typing import Dict, Any, List

class WebsitePromptSpecialist:
    def __init__(self, skill_version: str = "5.0.0 (Master Web Super Stack /impeccable + 21st.dev + motion.dev)"):
        self.skill_version = skill_version

    def generate_master_prompt(self, project_name: str, industry: str, target_audience: str, key_features: List[str] = None) -> Dict[str, Any]:
        """
        Synthesizes a specialized system prompt that injects active skill rules (/impeccable, 21st.dev, motion.dev,
        Higgsfield MCP, and /ultra-review) directly into AI coding assistants to build flawless web applications.
        """
        if not key_features:
            key_features = [
                "21st.dev Awwwards-ready Bento Grid & interactive component architecture",
                "motion.dev / GSAP 60-FPS spring physics & scroll-scrub animations",
                "Higgsfield MCP cinematic video background loops & 360° object showcases",
                "Impeccable visual hierarchy with zero 'AI Slop' (organic palettes, asymmetrical grids)",
                "Interactive industry-specific conversion widget (calculator, diagnostic hub, or custom slider)",
                "Pre-flight /ultra-review quality gate for WCAG AA accessibility and responsive polish"
            ]

        features_formatted = "\n".join(f"  - [x] {feat}" for feat in key_features)

        system_prompt = f"""# SYSTEM INSTRUCTIONS: /IMPECCABLE CREATIVE TECHNOLOGIST & UI/UX PRO MAX ARCHITECT

You are an elite Creative Technologist operating under the **GSD (Get Shit Done)** and **Superpowers** autonomous execution protocols. Your mission is to architect and code an Awwwards-winning, interactive web application for **"{project_name}"** ({industry}) targeting {target_audience}.

## 1. /IMPECCABLE & TASTE SKILL ENFORCEMENT (ZERO AI SLOP)
- **CRITICAL ANTI-SLOP RULE:** You must completely avoid generic "AI Slop". Do NOT use excessive centered text layouts, repetitive purple/cyan neon gradients, uniform bubbly rounded corners (e.g. `border-radius: 32px` everywhere), or Inter font defaults.
- **Aesthetic Judgment (Taste):** Curate organic, sophisticated color palettes matching the industry paradigm (e.g., Sunlit Travertine & Linen for luxury fashion, Obsidian Gold for fine dining, Deep Gunmetal Titanium for industrial engineering).
- **Spatial Hierarchy:** Use container queries, asymmetrical editorial grids, subtle 1px hairline borders (`rgba(255,255,255,0.08)` or `#E5DCCB`), and intentional whitespace to establish breathing room.

## 2. COMPONENT INTELLIGENCE & MOTION PHYSICS (/motion.dev & 21st.dev)
- **21st.dev Component Registry:** Do not build basic Bootstrap or standard Tailwind cards from scratch. Model all UI structures after modern 21st.dev components (interactive floating HUDs, glassmorphism badges, and dynamic accordions).
- **motion.dev / Framer Motion Physics:** Every interactive element must animate at 60 FPS using natural spring physics (`mass: 1, damping: 15, stiffness: 120`). Enforce smooth gesture recognition (`whileHover`, `whileTap`) and scroll-linked scrub transitions.
- **Higgsfield MCP Media Integration:** When showcasing products or luxury environments, structure image/video wrappers to support Higgsfield AI cinematic 360° video loops and macro camera motion.

## 3. MANDATORY INDUSTRY-SPECIFIC INTERACTIVE CONVERSION ENGINE
You must invent and embed at least ONE deep functional interactive tool tailored specifically to {industry}:
- If Medical/Dental: Interactive anatomical visualizer & instant patient consultation scheduler.
- If Dining/Hospitality: Interactive course tasting grid & sommelier wine pairing selector.
- If E-Commerce/Parts: Smart model/chassis compatibility filter & instant live Toman/Currency cart.
- If Legal/Finance: Interactive case valuation / settlement calculator with PDF report generation.

## 4. DELIVERABLE CHECKLIST FOR "{project_name.upper()}"
{features_formatted}
  - [x] Embedded offline canvas/SVG vector fallbacks for sandboxed preview iframe reliability
  - [x] Execution through /ultra-review quality inspection gate before final code output

## 5. /ULTRA-REVIEW PRE-FLIGHT QUALITY GATE
Before generating the final output, execute an internal `/ultra-review` reflection pass:
1. Verify contrast ratios meet WCAG AA standards across all breakpoints.
2. Check that no section is hidden by default with `opacity: 0` without fallback triggers.
3. Ensure all image URLs use verified, authenticated CDN sources or high-fidelity inline SVG illustrations.

Output a single, self-contained, production-ready HTML5/CSS3/JS file that compiles instantly."""

        cursor_rules = f"""---
description: /impeccable & 21st.dev Web Engineering Rules for {project_name}
globs: *.html, *.tsx, *.jsx, *.js, *.ts, *.css
---
# CURSOR & WINDSURF SPECIALIZED RULES: /IMPECCABLE & MOTION.DEV
When modifying or creating web components for {project_name}, enforce the following:
1. ALWAYS apply `/impeccable` and `taste skill` rules: zero AI slop, no repetitive purple gradients, no uniform rounded corners. Use organic, sophisticated palettes.
2. ALWAYS design UI structures inspired by `21st.dev` component patterns (asymmetrical Bento grids, subtle hairline borders, floating HUDs).
3. ALWAYS implement `motion.dev` / GSAP spring physics (`mass: 1, damping: 15, stiffness: 120`) for hover tilts and scroll transitions.
4. ALWAYS integrate offline Canvas/SVG fallbacks to ensure 100% display reliability in sandboxed preview environments.
5. ALWAYS run code through `/ultra-review` quality inspection (accessibility, responsive polish, contrast) before committing."""

        return {
            "status": "success",
            "project_name": project_name,
            "industry": industry,
            "target_audience": target_audience,
            "active_skills_injected": ["/impeccable", "taste skill", "21st.dev", "/motion.dev", "Higgsfield MCP", "GSD", "Superpowers", "/ultra-review"],
            "skill_benchmark": self.skill_version,
            "master_system_prompt": system_prompt.strip(),
            "cursor_rules_format": cursor_rules.strip(),
            "agency_integration": "Directly injected into LeadFlow.AI copywriter and website synthesizer agents."
        }

if __name__ == "__main__":
    specialist = WebsitePromptSpecialist()
    print("🚀 Testing Website Prompt Specialist with Active Skill Injection...")
    result = specialist.generate_master_prompt("Apex Dental Suite", "Medical Clinic", "VIP Healthcare Patients")
    print("Active Skills Injected:", result["active_skills_injected"])
    print("\nPrompt Preview:\n", result["master_system_prompt"][:500] + "...")
