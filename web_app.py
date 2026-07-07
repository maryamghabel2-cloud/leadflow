"""
LeadFlow.AI - Central Cloud Engine (Full-Stack Backend)
Powered by FastAPI & Uvicorn.
Orchestrates Autonomous AI Agents (Researcher, Copywriter, Blockchain Verifier,
No-Website Miner, and Shadow Infiltrator 3D Website Generator).
"""

import uvicorn
from fastapi import FastAPI, HTTPException, Body
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any, List
import os

from researcher_agent import ResearcherAgent
from copywriter_agent import CopywriterAgent
from blockchain_verifier import BlockchainVerifier
from no_website_miner import NoWebsiteMiner
from shadow_infiltrator import ShadowInfiltrator
from affiliate_manager import AffiliateManager
from voice_outbound_agent import VoiceOutboundAgent
from referral_rewards_agent import ReferralRewardsAgent

app = FastAPI(
    title="LeadFlow.AI Autonomous SDR & Shadow Infiltrator Engine",
    description="Backend AI API powering live web scraping, personalized email copywriting, blockchain auditing, and instant 3D neon website generation.",
    version="3.0.0"
)

# Enable CORS for frontend flexibility
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize Agents & Generators
researcher = ResearcherAgent(timeout=12)
copywriter = CopywriterAgent(sender_name="Elena", sender_company="LeadFlow.AI")
verifier = BlockchainVerifier(timeout=10)
miner = NoWebsiteMiner(timeout=12)
infiltrator = ShadowInfiltrator(output_dir="generated_sites")
affiliate_mgr = AffiliateManager()
voice_agent = VoiceOutboundAgent()
referral_agent = ReferralRewardsAgent()

# Request Models
class LeadCaptureRequest(BaseModel):
    email: str = Field(..., example="marcus@cloudbase.io")
    name: str = Field(..., example="Marcus Vance")
    company: str = Field(..., example="CloudBase Tech")
    studio_source: str = Field(default="SDR_STUDIO", example="TELEPHONY_STUDIO")

class ReferralRewardRequest(BaseModel):
    referrer_code: str = Field(..., example="ref_alex2026")
    new_client_name: str = Field(..., example="Lumiere Fine Dining Paris")
    reward_choice: str = Field(default="credits", example="credits")

class VoiceCallRequest(BaseModel):
    business_name: str = Field(..., example="Apex Dental Lounge")
    phone: str = Field(..., example="+1 (416) 555-0199")
    city: str = Field(..., example="Toronto")
    live_cloud_url: str = Field(..., example="https://maryamghabel2-cloud.github.io/leadflow/live_demos/apex_dental_live.html")
    contact_name: str = Field(default="Decision Maker", example="Dr. Wright")

class AnalyzeRequest(BaseModel):
    url: str = Field(..., example="github.com", description="Target company website URL")
    prospect_name: str = Field(default="Decision Maker", example="David (CEO)", description="Name and role of the prospect")

class VerifyPaymentRequest(BaseModel):
    tx_hash: str = Field(..., description="Tron (TRC-20) USDT Transaction Hash")
    plan_amount: Optional[float] = Field(default=None, description="Expected USDT plan price (e.g. 199 or 499)")
    client_name: Optional[str] = Field(default="New Enterprise Client", description="Client or company name")
    plan_name: Optional[str] = Field(default="0-to-100 Cloud Web Agency Package", description="Purchased service tier")
    referrer_id: Optional[str] = Field(default=None, description="Affiliate referrer code for PLG commissions")

class RegisterSaleRequest(BaseModel):
    client_name: str = Field(..., example="Vanguard Legal New York")
    plan_amount_usdt: float = Field(..., example=499.0)
    referrer_id: str = Field(default="alex_growth", example="alex_growth")

class MineRequest(BaseModel):
    city: str = Field(default="Toronto", example="London", description="Target geographic city")
    category: str = Field(default="clinic", example="restaurant", description="Business category/niche")
    limit: int = Field(default=6, ge=1, le=20, description="Number of businesses to discover")

class GenerateSiteRequest(BaseModel):
    business_name: str = Field(..., example="Apex Dental Clinic", description="Name of the business")
    category: str = Field(default="Clinic", description="Business category")
    city: str = Field(default="Toronto", description="City location")
    phone: str = Field(default="+1 (555) 019-2831", description="Contact phone number")
    custom_domain: Optional[str] = Field(default=None, description="Custom domain for 0-to-100 client handover")

@app.get("/")
async def serve_index():
    if os.path.exists("index.html"):
        return FileResponse("index.html")
    return {"message": "LeadFlow.AI API Engine is Running. Frontend index.html not found in current directory."}

@app.get("/onboard")
async def serve_onboard():
    if os.path.exists("onboard.html"):
        return FileResponse("onboard.html")
    return {"message": "Onboard interface not found. Please create onboard.html."}

@app.get("/miner")
async def serve_miner():
    if os.path.exists("miner.html"):
        return FileResponse("miner.html")
    return {"message": "Miner interface not found. Please create miner.html."}

@app.get("/generated/{filename}")
async def serve_generated_site(filename: str):
    filepath = os.path.join("generated_sites", filename)
    if os.path.exists(filepath):
        return FileResponse(filepath)
    raise HTTPException(status_code=404, detail="Generated luxury website file not found.")

@app.get("/live_demos/{filename}")
async def serve_live_demo(filename: str):
    filepath = os.path.join("generated_sites", "live_demos", filename)
    if os.path.exists(filepath):
        return FileResponse(filepath)
    raise HTTPException(status_code=404, detail="Live demo file not found.")

@app.get("/handover_packages/{filename}")
async def serve_handover_package(filename: str):
    filepath = os.path.join("generated_sites", "handover_packages", filename)
    if os.path.exists(filepath):
        return FileResponse(filepath, media_type="application/zip", filename=filename)
    raise HTTPException(status_code=404, detail="Handover ZIP package not found.")

@app.post("/api/analyze")
async def analyze_prospect(request: AnalyzeRequest):
    """
    Triggers the autonomous pipeline:
    1. Researcher Agent crawls the live website.
    2. Copywriter Agent synthesizes pain points & crafts personalized email.
    """
    try:
        research_data = researcher.extract_signals(request.url)
        email_output = copywriter.generate_email(request.prospect_name, research_data)
        return {
            "status": "success",
            "research": research_data,
            "campaign": email_output
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Agent Execution Failed: {str(e)}")

@app.post("/api/verify-payment")
async def verify_payment(request: VerifyPaymentRequest):
    """
    Audits Tron USDT payment on-chain via Tronscan API and triggers instant Telegram broadcast!
    """
    try:
        client_info = {"client_name": request.client_name, "plan_name": request.plan_name}
        audit_result = verifier.verify_usdt_transaction(request.tx_hash, request.plan_amount, client_info=client_info)
        
        # If payment successful and referrer_id present, trigger PLG affiliate commission!
        if audit_result.get("status") == "success" and request.referrer_id:
            try:
                affiliate_mgr.register_new_sale(
                    client_name=request.client_name or "New Client",
                    plan_amount_usdt=audit_result.get("amount_usdt", request.plan_amount or 499.0),
                    referrer_id=request.referrer_id
                )
            except Exception as aff_e:
                print(f"⚠️ Affiliate commission log warning: {aff_e}")
                
        return audit_result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Blockchain Audit Error: {str(e)}")

@app.post("/api/webhook/tron-deposit")
async def tron_deposit_webhook(payload: Dict[str, Any] = Body(...)):
    """
    Live Blockchain Webhook endpoint for Tronscan / TronGrid node notifications.
    Automatically audits transaction and broadcasts Telegram alert upon receiving USDT transfer.
    """
    try:
        tx_hash = payload.get("tx_hash") or payload.get("hash") or payload.get("transaction_id", "")
        plan_amount = float(payload.get("amount", 499.0))
        client_name = payload.get("client_name", payload.get("sender", "Webhook Enterprise Client"))
        plan_name = payload.get("plan_name", "Autonomous AI Agency Tier")
        
        if not tx_hash:
            raise HTTPException(status_code=400, detail="Missing tx_hash in webhook payload.")
            
        client_info = {"client_name": client_name, "plan_name": plan_name}
        audit_result = verifier.verify_usdt_transaction(tx_hash, plan_amount, client_info=client_info)
        return {"webhook_status": "received_and_processed", "audit": audit_result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Tron Webhook Error: {str(e)}")

@app.post("/api/mine-businesses")
async def mine_no_website_businesses(request: MineRequest):
    """
    Discovers local businesses in a target city that lack a website.
    """
    try:
        results = miner.mine_businesses(request.city, request.category, request.limit)
        return results
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Miner Error: {str(e)}")

@app.post("/api/generate-website")
async def generate_luxury_website(request: GenerateSiteRequest):
    """
    Instantly compiles an Awwwards-style 3D website tailored for a local business without a website,
    provisions a live cloud URL, and creates a 0-to-100 client handover ZIP package.
    """
    try:
        site_result = infiltrator.generate_luxury_site(request.business_name, request.category, request.city, request.phone, request.custom_domain)
        return site_result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Shadow Infiltrator Error: {str(e)}")

@app.post("/api/affiliate/register-sale")
async def register_affiliate_sale(request: RegisterSaleRequest):
    """
    Registers a new viral referral sale or site upgrade,
    triggering instant 20% Month-1 USDT commission payout to Tron wallet.
    """
    try:
        res = affiliate_mgr.register_new_sale(request.client_name, request.plan_amount_usdt, request.referrer_id)
        return res
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Affiliate Error: {str(e)}")

@app.post("/api/affiliate/process-renewals")
async def process_affiliate_renewals():
    """
    Autonomous monthly cron job: Scans active renewals and pays 5% residual passive crypto commissions.
    """
    try:
        res = affiliate_mgr.process_monthly_renewals()
        return res
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Renewal Error: {str(e)}")

@app.post("/api/voice/call")
async def trigger_voice_outbound_call(request: VoiceCallRequest):
    """
    Triggers an autonomous AI voice telephony call (Vapi/Bland AI/ElevenLabs)
    inviting prospects to view their generated 3D portal without scam suspicion.
    """
    try:
        res = voice_agent.initiate_outbound_call(request.business_name, request.phone, request.city, request.live_cloud_url, request.contact_name)
        return res
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Telephony Error: {str(e)}")

@app.post("/api/lead/capture")
async def capture_work_email(request: LeadCaptureRequest):
    """
    Harvests verified enterprise work emails before unlocking interactive trial reports.
    """
    try:
        res = referral_agent.capture_lead_email(request.email, request.name, request.company, request.studio_source)
        return res
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Lead Capture Error: {str(e)}")

@app.post("/api/referral/reward")
async def grant_ambassador_reward(request: ReferralRewardRequest):
    """
    Grants sustainable SaaS Ambassador rewards (+500 Voice/Email Credits or $50 credit) per referral.
    """
    try:
        res = referral_agent.process_referral_reward(request.referrer_code, request.new_client_name, request.reward_choice)
        return res
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Referral Reward Error: {str(e)}")

@app.get("/api/health")
async def health_check():
    return {
        "status": "online",
        "service": "LeadFlow.AI Cloud Engine v7.0",
        "agents": [
            "ResearcherAgent (Live Web Scraper)",
            "CopywriterAgent (LLM Logic)",
            "BlockchainVerifier (Tronscan API)",
            "NoWebsiteMiner (OpenStreetMap / Directory Scraper)",
            "ShadowInfiltrator (Instant 3D Website Generator)",
            "AffiliateManager (20%/5% Crypto PLG Referral Loop)",
            "VoiceOutboundAgent (Vapi/Bland AI Telephony Assistant)",
            "ReferralRewardsAgent (SaaS Ambassador Rewards & Email Harvester)"
        ]
    }

if __name__ == "__main__":
    print("🚀 Starting LeadFlow.AI Central Engine on port 8000...")
    uvicorn.run(app, host="0.0.0.0", port=8000)
