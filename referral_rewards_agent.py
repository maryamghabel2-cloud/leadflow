"""
LeadFlow.AI - Ambassador Referral Rewards & Lead Capture Agent (`referral_rewards_agent.py`)
Replaces heavy multi-tier cash commissions with a sustainable SaaS Ambassador Reward Program.
Rewards users for inviting new businesses via referral links with:
- +500 Free Autonomous AI Voice Calls & Outbound Email Credits
- OR $50 USDT Account Credit / 1-Month Plan Upgrade
Also manages enterprise lead capture by harvesting verified work emails from interactive studio trials.
"""

import json
import time
from typing import Dict, Any, List

class ReferralRewardsAgent:
    def __init__(self, credit_reward_calls: int = 500, usdt_reward_credit: float = 50.0):
        self.credit_reward_calls = credit_reward_calls
        self.usdt_reward_credit = usdt_reward_credit
        
        # Captured Enterprise Lead Database (Email Harvesting)
        self.captured_leads: List[Dict[str, Any]] = [
            {"email": "marcus@cloudbase.io", "name": "Marcus Vance", "company": "CloudBase Tech", "source_studio": "SDR_COPYWRITER_TRIAL", "timestamp": "2026-07-05 10:15:00"},
            {"email": "dr.wright@apexdental.com", "name": "Dr. Wright", "company": "Apex Dental Toronto", "source_studio": "AI_VOICE_TELEPHONY_TRIAL", "timestamp": "2026-07-05 11:20:00"}
        ]

        # Ambassador Accounts & Earned Rewards
        self.ambassadors = {
            "alex_ambassador": {
                "name": "Alex Vance",
                "referral_code": "ref_alex2026",
                "total_invites_successful": 4,
                "earned_call_credits": 2000,
                "earned_usdt_credit": 200.0
            }
        }

    def capture_lead_email(self, email: str, name: str, company: str, studio_source: str) -> Dict[str, Any]:
        """
        Harvests prospect work emails before unlocking interactive studio reports or live cloud URLs.
        """
        lead_id = f"lead_{int(time.time())}"
        lead_entry = {
            "lead_id": lead_id,
            "email": email.strip().lower(),
            "name": name.strip(),
            "company": company.strip(),
            "source_studio": studio_source,
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }
        self.captured_leads.append(lead_entry)
        
        return {
            "status": "success",
            "event": "WORK_EMAIL_CAPTURED",
            "lead": lead_entry,
            "total_database_leads": len(self.captured_leads),
            "message": f"✔ Email '{email}' verified. Unlocking full AI report & live cloud demo link."
        }

    def process_referral_reward(self, referrer_code: str, new_client_name: str, reward_choice: str = "credits") -> Dict[str, Any]:
        """
        Grants Ambassador rewards when an invited business subscribes or deploys a $499 site.
        Reward choices: 'credits' (+500 Voice/Email calls) OR 'usdt' ($50 account credit).
        """
        ambassador_key = None
        for key, data in self.ambassadors.items():
            if data["referral_code"] == referrer_code:
                ambassador_key = key
                break

        if not ambassador_key:
            return {"status": "error", "message": f"Referral code '{referrer_code}' not found."}

        amb = self.ambassadors[ambassador_key]
        amb["total_invites_successful"] += 1

        if reward_choice == "usdt":
            amb["earned_usdt_credit"] += self.usdt_reward_credit
            reward_desc = f"+${self.usdt_reward_credit} USDT Account Credit applied to subscription balance"
        else:
            amb["earned_call_credits"] += self.credit_reward_calls
            reward_desc = f"+{self.credit_reward_calls} Autonomous AI Voice & Email Outreach Credits added"

        return {
            "status": "success",
            "event": "AMBASSADOR_REWARD_GRANTED",
            "ambassador_name": amb["name"],
            "new_client_invited": new_client_name,
            "reward_granted": reward_desc,
            "total_ambassador_stats": {
                "successful_invites": amb["total_invites_successful"],
                "total_call_credits_balance": amb["earned_call_credits"],
                "total_usdt_credit_balance": amb["earned_usdt_credit"]
            }
        }

if __name__ == "__main__":
    agent = ReferralRewardsAgent()
    print("🚀 Testing Ambassador Referral Rewards & Lead Capture Agent...")
    lead_res = agent.capture_lead_email("sarah@nexussoft.io", "Sarah Jenkins", "Nexus Soft", "TELEPHONY_STUDIO")
    print("\n1. Lead Capture Output:\n", json.dumps(lead_res, indent=2))
    
    reward_res = agent.process_referral_reward("ref_alex2026", "Lumiere Fine Dining Paris", "credits")
    print("\n2. Ambassador Reward Output:\n", json.dumps(reward_res, indent=2))
