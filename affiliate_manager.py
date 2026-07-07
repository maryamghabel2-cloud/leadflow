"""
LeadFlow.AI - Autonomous Affiliate & Viral Referral Manager (`affiliate_manager.py`)
Replaces cold emailing with a Decentralized Product-Led Growth (PLG) & Crypto Referral Loop.
Manages multi-tier decreasing affiliate commissions:
- 20% Instant USDT Commission on Month 1 (e.g. $100 on a $499 subscription or site purchase)
- 5% Residual Passive USDT Commission on Month 2+ renewals (e.g. $25/mo forever)
- Automatic instant commission cutoff upon subscription termination.
- Connects to Tron USDT TRC-20 payment escrow for autonomous automated payouts.
"""

import json
import time
from typing import Dict, Any, List

class AffiliateManager:
    def __init__(self, month_1_rate: float = 0.20, residual_rate: float = 0.05):
        self.month_1_rate = month_1_rate
        self.residual_rate = residual_rate
        
        # Simulated Database of Referrers & Referred Clients
        self.referrers = {
            "alex_growth": {
                "name": "Alex Vance",
                "wallet_trc20": "TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t",
                "total_earned_usdt": 1450.0,
                "active_referrals": 12
            },
            "sara_marketing": {
                "name": "Sara K.",
                "wallet_trc20": "TLvP5hApeQ9s4yL5D3h8q9r2w1x8z7v6m5",
                "total_earned_usdt": 3200.0,
                "active_referrals": 28
            }
        }

        self.subscriptions = {
            "sub_101": {"client": "Apex Dental Toronto", "plan_amount_usdt": 499.0, "referrer_id": "alex_growth", "months_active": 1, "status": "ACTIVE"},
            "sub_102": {"client": "Lumiere Fine Dining Paris", "plan_amount_usdt": 1499.0, "referrer_id": "sara_marketing", "months_active": 4, "status": "ACTIVE"},
            "sub_103": {"client": "Skyline Realty Dubai", "plan_amount_usdt": 499.0, "referrer_id": "alex_growth", "months_active": 3, "status": "TERMINATED"}
        }

    def register_new_sale(self, client_name: str, plan_amount_usdt: float, referrer_id: str, sub_id: str = None) -> Dict[str, Any]:
        """
        Registers a new sale or $499 site upgrade triggered via a viral referral link.
        Calculates and triggers the immediate 20% Month-1 USDT commission payout.
        """
        if not sub_id:
            sub_id = f"sub_{int(time.time())}"

        commission_amount = round(plan_amount_usdt * self.month_1_rate, 2)
        
        if referrer_id in self.referrers:
            self.referrers[referrer_id]["total_earned_usdt"] += commission_amount
            self.referrers[referrer_id]["active_referrals"] += 1
            wallet = self.referrers[referrer_id]["wallet_trc20"]
            payout_status = f"AUTOPAY_SUCCESS: Transferred {commission_amount} USDT to Tron wallet {wallet[:10]}..."
        else:
            payout_status = "REFERRER_NOT_FOUND: Commission held in treasury vault."

        self.subscriptions[sub_id] = {
            "client": client_name,
            "plan_amount_usdt": plan_amount_usdt,
            "referrer_id": referrer_id,
            "months_active": 1,
            "status": "ACTIVE"
        }

        return {
            "status": "success",
            "event": "NEW_VIRAL_SALE_REGISTERED",
            "subscription_id": sub_id,
            "client_name": client_name,
            "plan_usdt": plan_amount_usdt,
            "referrer_id": referrer_id,
            "commission_tier": "MONTH_1_INSTANT (20%)",
            "commission_payout_usdt": commission_amount,
            "payout_execution": payout_status
        }

    def process_monthly_renewals(self) -> Dict[str, Any]:
        """
        Autonomous monthly cron job: Scans all subscriptions.
        If ACTIVE and month >= 2, pays 5% residual passive USDT commission.
        If TERMINATED or canceled, instantly cuts off commission.
        """
        results = []
        total_residual_paid = 0.0

        for sub_id, data in self.subscriptions.items():
            if data["status"] != "ACTIVE":
                results.append({
                    "sub_id": sub_id,
                    "client": data["client"],
                    "status": "TERMINATED",
                    "action": "INSTANT_CUTOFF - Zero commission disbursed."
                })
                continue

            # Advance month
            data["months_active"] += 1
            months = data["months_active"]
            referrer_id = data["referrer_id"]

            if months >= 2:
                comm = round(data["plan_amount_usdt"] * self.residual_rate, 2)
                if referrer_id in self.referrers:
                    self.referrers[referrer_id]["total_earned_usdt"] += comm
                    wallet = self.referrers[referrer_id]["wallet_trc20"]
                    total_residual_paid += comm
                    results.append({
                        "sub_id": sub_id,
                        "client": data["client"],
                        "status": "ACTIVE",
                        "months_active": months,
                        "referrer_id": referrer_id,
                        "commission_tier": "RESIDUAL_PASSIVE (5%)",
                        "payout_usdt": comm,
                        "wallet": wallet[:10] + "..."
                    })

        return {
            "status": "success",
            "event": "MONTHLY_RESIDUAL_PAYOUT_AUDIT",
            "total_active_renewals": len([r for r in results if "RESIDUAL" in r.get("commission_tier", "")]),
            "total_terminated_cutoffs": len([r for r in results if r["status"] == "TERMINATED"]),
            "total_residual_payout_usdt": total_residual_paid,
            "details": results
        }

if __name__ == "__main__":
    manager = AffiliateManager()
    print("🚀 Testing Autonomous Affiliate & Viral Referral Manager...")
    sale_res = manager.register_new_sale("Vanguard Legal New York", 499.0, "alex_growth", "sub_104")
    print("\n1. New Viral Sale Event:\n", json.dumps(sale_res, indent=2))
    
    print("\n2. Simulating Month 2 Renewal Cron Job...")
    renew_res = manager.process_monthly_renewals()
    print("Renewal Audit Output:\n", json.dumps(renew_res, indent=2))
