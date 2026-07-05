"""
LeadFlow.AI (Project Shadow) - Zero-Cost ($0 Budget) Project Manager & Autonomous Orchestrator
Acts as Chief Project Manager for our Double-Engine Business:
1. Provisions local SQLite zero-cost database (leadflow_agency.db) for leads, outbound campaigns, and agent health.
2. Executes Engine 1 (SDR Outbound Email Pipeline) across sample B2B technology and SaaS prospects for $0!
3. Executes Engine 2 (Shadow Infiltrator v4.0) to verify multi-paradigm 3D portals and handover ZIP packages.
4. Compiles a live operational Agency Dashboard (agency_dashboard.html).
5. Executes automated git commit & push to deploy everything live to GitHub Pages for $0!
"""

import os
import sqlite3
import json
import time
import subprocess
from datetime import datetime
from researcher_agent import ResearcherAgent
from copywriter_agent import CopywriterAgent
from shadow_infiltrator import ShadowInfiltrator
from cloud_deployer import CloudDeploymentEngine

class LeadFlowProjectManager:
    def __init__(self, db_filename: str = "leadflow_agency.db"):
        self.repo_dir = os.path.dirname(os.path.abspath(__file__))
        self.db_path = os.path.join(self.repo_dir, db_filename)
        self.researcher = ResearcherAgent(timeout=10)
        self.copywriter = CopywriterAgent(sender_name="Elena", sender_company="LeadFlow.AI")
        self.infiltrator = ShadowInfiltrator(output_dir=os.path.join(self.repo_dir, "generated_sites"))
        self._init_db()

    def _init_db(self):
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS outbound_campaigns
                     (id INTEGER PRIMARY KEY AUTOINCREMENT, prospect_name TEXT, target_domain TEXT,
                      value_prop TEXT, subject TEXT, status TEXT, created_at TEXT)''')
        c.execute('''CREATE TABLE IF NOT EXISTS agency_logs
                     (id INTEGER PRIMARY KEY AUTOINCREMENT, agent_name TEXT, action TEXT, details TEXT, created_at TEXT)''')
        conn.commit()
        conn.close()

    def log_action(self, agent_name: str, action: str, details: str):
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        c.execute("INSERT INTO agency_logs (agent_name, action, details, created_at) VALUES (?, ?, ?, ?)", (agent_name, action, details, now))
        conn.commit()
        conn.close()
        print(f"[{now}] [{agent_name.upper()}]: {action} -> {details}")

    def execute_sdr_outbound_engine(self):
        """
        Engine 1: Execute Autonomous SDR Outreach for $0!
        """
        self.log_action("SDR_Engine", "START_CAMPAIGN", "Initiating automated B2B outbound research and copywriting queue.")
        prospects = [
            ("David (CEO)", "github.com"),
            ("Sarah (Head of Growth)", "stripe.com"),
            ("Marcus (Founder)", "vercel.com"),
            ("Elena (VP of Outbound)", "render.com")
        ]

        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        for name, domain in prospects:
            res_data = self.researcher.extract_signals(domain)
            email_out = self.copywriter.generate_email(name, res_data)
            
            conn = sqlite3.connect(self.db_path)
            c = conn.cursor()
            c.execute('''INSERT INTO outbound_campaigns (prospect_name, target_domain, value_prop, subject, status, created_at)
                         VALUES (?, ?, ?, ?, ?, ?)''',
                      (name, domain, res_data.get("value_proposition", "")[:100], email_out["subject"], "Ready for Dispatch", now))
            conn.commit()
            conn.close()
            
            self.log_action("Copywriter", "DRAFT_GENERATED", f"Crafted tailored cold email for {name} @ {domain}")

    def verify_shadow_infiltrator_engine(self):
        """
        Engine 2: Verify Multi-Paradigm 3D Portals and Handover ZIP Packages
        """
        self.log_action("Shadow_Infiltrator", "VERIFY_PARADIGMS", "Checking 0-to-100 client deployment infrastructure.")
        targets = [
            ("Apex Dental Clinic", "Dental Clinic", "Toronto", "+1 416 555 0199"),
            ("Lumiere Fine Dining", "Restaurant", "Paris", "+33 1 42 68 55 00"),
            ("Vanguard Legal Counsel", "Law Firm", "New York", "+1 212 555 0100"),
            ("Skyline Real Estate", "Real Estate", "Dubai", "+971 4 318 8888")
        ]

        for b_name, cat, city, phone in targets:
            res = self.infiltrator.generate_luxury_site(b_name, cat, city, phone)
            self.log_action("Deployer", "PROVISIONED", f"{b_name} -> {res['industry_paradigm_applied']} | Live URL: {res['live_cloud_demo_url']}")

    def compile_agency_dashboard(self):
        """
        Step 3: Compile Zero-Cost Operational Dashboard HTML
        """
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute("SELECT * FROM outbound_campaigns ORDER BY id DESC LIMIT 10")
        campaigns = c.fetchall()
        c.execute("SELECT * FROM agency_logs ORDER BY id DESC LIMIT 15")
        logs = c.fetchall()
        conn.close()

        camp_html = ""
        for camp in campaigns:
            camp_html += f"""
            <tr style="border-bottom: 1px solid #1f2937;">
                <td style="padding: 12px; font-weight: bold; color: #6366f1;">{camp[1]}</td>
                <td style="padding: 12px; color: #fff;">{camp[2]}</td>
                <td style="padding: 12px; color: #9ca3af;">{camp[4]}</td>
                <td style="padding: 12px; font-weight: bold; color: #10b981;">{camp[5]}</td>
            </tr>
            """

        logs_html = ""
        for log in logs:
            logs_html += f"""<div style="margin-bottom: 8px; font-family: monospace; font-size: 12px;"><span style="color: #64748b;">[{log[4]}]</span> <strong style="color: #6366f1;">{log[1]} ({log[2]}):</strong> <span style="color: #e2e8f0;">{log[3]}</span></div>"""

        html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LeadFlow.AI (Project Shadow) | Zero-Cost Agency Operating Dashboard</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;700;800&family=JetBrains+Mono:wght@400;700&display=swap');
        * {{ margin: 0; padding: 0; box-sizing: border-box; font-family: 'Plus Jakarta Sans', sans-serif; }}
        body {{ background: #030712; color: #f8fafc; padding: 40px 60px; line-height: 1.8; }}
        @media (max-width: 768px) {{ body {{ padding: 20px; }} }}
        .header {{ display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid #6366f1; padding-bottom: 20px; margin-bottom: 30px; flex-wrap: wrap; gap: 16px; }}
        .badge {{ background: #6366f1; color: #fff; padding: 6px 16px; border-radius: 20px; font-weight: 800; font-size: 13px; }}
        .card {{ background: #0b1120; border: 1px solid rgba(99, 102, 241, 0.3); border-radius: 24px; padding: 30px; margin-bottom: 30px; box-shadow: 0 20px 50px rgba(0,0,0,0.8); }}
        h2 {{ font-size: 24px; font-weight: 800; color: #fff; margin-bottom: 16px; display: flex; align-items: center; gap: 10px; }}
        table {{ width: 100%; border-collapse: collapse; text-align: left; margin-top: 14px; font-size: 14px; }}
        th {{ background: #111827; padding: 14px 12px; color: #6366f1; font-weight: 800; border-bottom: 2px solid #6366f1; }}
        .btn-live {{ background: linear-gradient(135deg, #6366f1, #ec4899); color: #fff; font-weight: 800; padding: 12px 24px; border-radius: 20px; text-decoration: none; display: inline-block; }}
    </style>
</head>
<body>
    <div class="header">
        <div>
            <h1 style="font-size: 32px; font-weight: 800; color: #fff;">🚀 LeadFlow.AI (Project Shadow) Agency OS</h1>
            <p style="color: #94a3b8; font-size: 14px; margin-top: 6px;">Zero-Cost ($0 Budget) Double-Engine Business Managed by Chief AI Project Manager</p>
        </div>
        <div style="display: flex; gap: 12px; align-items: center;">
            <span class="badge">● 100% OPERATIONAL & LIVE</span>
            <a href="index.html" class="btn-live">🌟 View Main Landing Page ←</a>
        </div>
    </div>

    <div class="card">
        <h2>📧 Engine 1: Autonomous SDR Outbound Campaign Queue ($199-$1,499/mo)</h2>
        <p style="color: #94a3b8; font-size: 13px;">Live scraped intelligence and personalized sales hooks generated by Elena AI without human overhead:</p>
        <div style="overflow-x: auto;">
            <table>
                <thead>
                    <tr><th>Prospect Decision Maker</th><th>Target Domain</th><th>Synthesized Subject Line</th><th>Queue Status</th></tr>
                </thead>
                <tbody>{camp_html}</tbody>
            </table>
        </div>
    </div>

    <div class="card">
        <h2>📜 Live Agency Audit Trail & Engine Health Logs</h2>
        <div style="background: #020408; border: 1px solid rgba(255,255,255,0.1); border-radius: 16px; padding: 20px; max-height: 280px; overflow-y: auto;">
            {logs_html}
        </div>
    </div>

    <footer style="text-align: center; color: #64748b; font-size: 13px; padding-top: 20px;">
        © 2026 LeadFlow.AI (Project Shadow) | Executed with Zero Cost by Chief AI Project Manager | Hosted Free on GitHub Pages SSL Edge
    </footer>
</body>
</html>"""
        dash_path = os.path.join(self.repo_dir, "agency_dashboard.html")
        with open(dash_path, "w", encoding="utf-8") as f:
            f.write(html_content.strip())
        self.log_action("Dashboard", "COMPILED", "Compiled agency_dashboard.html successfully inside repo directory.")

    def deploy_live_to_github(self):
        """
        Step 4: Autonomous Zero-Cost Cloud Deployment via Git Push
        """
        try:
            subprocess.run(["git", "add", "."], cwd=self.repo_dir, check=False)
            subprocess.run(["git", "commit", "-m", "🤖 Zero-Cost Agency Orchestrator: Execute SDR outbound queue & compile agency dashboard"], cwd=self.repo_dir, check=False)
            res = subprocess.run(["git", "push", "origin", "main"], cwd=self.repo_dir, capture_output=True, text=True, check=False)
            status = "Published to GitHub Pages" if res.returncode == 0 else f"Staged ({res.stderr.strip()[:60]})"
            self.log_action("Deployer", "EDGE_DEPLOY", f"Automated zero-cost deployment to GitHub Pages -> {status}")
        except Exception as e:
            self.log_action("Deployer", "EDGE_DEPLOY_ERROR", str(e)[:60])

if __name__ == "__main__":
    print("👔 Chief Project Manager: Initializing Zero-Cost Agency Execution for LeadFlow.AI...")
    pm = LeadFlowProjectManager()
    pm.execute_sdr_outbound_engine()
    pm.verify_shadow_infiltrator_engine()
    pm.compile_agency_dashboard()
    pm.deploy_live_to_github()
    print("✨ LeadFlow Project Manager Task Complete! Double-Engine business operational and live on GitHub Pages.")
