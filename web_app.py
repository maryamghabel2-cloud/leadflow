"""
LeadFlow.AI - Central Cloud Engine (Full-Stack Backend) v4.1 hardened
Powered by FastAPI & Uvicorn.
"""

from __future__ import annotations

import os
from typing import Optional, Dict, Any, List

import uvicorn
from fastapi import FastAPI, HTTPException, Body
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

from researcher_agent import ResearcherAgent
from copywriter_agent import CopywriterAgent
from blockchain_verifier import BlockchainVerifier
from no_website_miner import NoWebsiteMiner
from shadow_infiltrator import ShadowInfiltrator
from affiliate_manager import AffiliateManager
from voice_outbound_agent import VoiceOutboundAgent
from referral_rewards_agent import ReferralRewardsAgent
from payment_ledger import PaymentLedger

app = FastAPI(
    title="LeadFlow.AI Autonomous SDR & Shadow Infiltrator Engine",
    description=(
        "Backend AI API powering live web scraping, personalized email copywriting, "
        "blockchain auditing, and instant website generation."
    ),
    version="4.1.0",
)

# Serve generated media assets (dental photos, etc.)
if os.path.isdir("generated_sites/assets"):
    app.mount("/assets", StaticFiles(directory="generated_sites/assets"), name="assets")


# CORS: restrict in production via env LEADFLOW_CORS_ORIGINS=https://yourdomain.com,https://...
_cors_raw = os.environ.get("LEADFLOW_CORS_ORIGINS", "").strip()
if _cors_raw:
    _allow_origins: List[str] = [o.strip() for o in _cors_raw.split(",") if o.strip()]
    _allow_credentials = True
else:
    # Dev default: open origins but credentials off (safer combo)
    _allow_origins = ["*"]
    _allow_credentials = False

app.add_middleware(
    CORSMiddleware,
    allow_origins=_allow_origins,
    allow_credentials=_allow_credentials,
    allow_methods=["*"],
    allow_headers=["*"],
)

researcher = ResearcherAgent(timeout=12)
copywriter = CopywriterAgent(sender_name="Elena", sender_company="LeadFlow.AI")
verifier = BlockchainVerifier(timeout=10)
miner = NoWebsiteMiner(timeout=12)
infiltrator = ShadowInfiltrator(output_dir="generated_sites")
affiliate_mgr = AffiliateManager()
voice_agent = VoiceOutboundAgent()
referral_agent = ReferralRewardsAgent()
ledger = PaymentLedger()


# ---------------------------------------------------------------------------
# Request models
# ---------------------------------------------------------------------------
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
    live_cloud_url: str = Field(
        ...,
        example="https://maryamghabel2-cloud.github.io/leadflow/generated_sites/live_demos/apex_dental_lounge_live.html",
    )
    contact_name: str = Field(default="Decision Maker", example="Dr. Wright")


class AnalyzeRequest(BaseModel):
    url: str = Field(..., example="github.com")
    prospect_name: str = Field(default="Decision Maker", example="David (CEO)")


class VerifyPaymentRequest(BaseModel):
    tx_hash: str = Field(..., description="Tron (TRC-20) USDT Transaction Hash")
    plan_amount: Optional[float] = Field(default=None, description="Expected USDT amount")
    client_name: Optional[str] = Field(default="New Enterprise Client")
    plan_name: Optional[str] = Field(default="0-to-100 Cloud Web Agency Package")
    referrer_id: Optional[str] = Field(default=None)


class RegisterSaleRequest(BaseModel):
    client_name: str = Field(..., example="Vanguard Legal New York")
    plan_amount_usdt: float = Field(..., example=499.0)
    referrer_id: str = Field(default="alex_growth", example="alex_growth")


class MineRequest(BaseModel):
    city: str = Field(default="Toronto", example="London")
    category: str = Field(default="clinic", example="restaurant")
    limit: int = Field(default=6, ge=1, le=20)


class GenerateSiteRequest(BaseModel):
    business_name: str = Field(..., example="Apex Dental Clinic")
    category: str = Field(default="Clinic")
    city: str = Field(default="Toronto")
    phone: str = Field(default="+1 (555) 019-2831")
    custom_domain: Optional[str] = Field(default=None)


# ---------------------------------------------------------------------------
# Static pages
# ---------------------------------------------------------------------------
@app.get("/")
async def serve_index():
    if os.path.exists("index.html"):
        return FileResponse("index.html")
    return {"message": "LeadFlow.AI API Engine is Running. Frontend index.html not found."}


@app.get("/onboard")
async def serve_onboard():
    if os.path.exists("onboard.html"):
        return FileResponse("onboard.html")
    return {"message": "Onboard interface not found. Please create onboard.html."}



@app.get("/agency")
async def serve_agency():
    if os.path.exists("agency_dashboard.html"):
        return FileResponse("agency_dashboard.html")
    return {"message": "Agency dashboard not found."}

@app.get("/metaverse")
async def serve_metaverse():
    if os.path.exists("index_metaverse_3d.html"):
        return FileResponse("index_metaverse_3d.html")
    return {"message": "Metaverse page not found."}

@app.get("/enterprise")
async def serve_enterprise():
    if os.path.exists("index_enterprise_minimal.html"):
        return FileResponse("index_enterprise_minimal.html")
    return {"message": "Enterprise page not found."}

@app.get("/hire")
async def serve_hire():
    if os.path.exists("hire.html"):
        return FileResponse("hire.html")
    return {"message": "Hire page not found."}


@app.get("/first-customer")
async def serve_first_customer():
    if os.path.exists("first_customer.html"):
        return FileResponse("first_customer.html")
    return {"message": "First customer ops page not found."}


@app.get("/go")
async def serve_go_alias():
    """Short alias for the first-customer command center."""
    if os.path.exists("first_customer.html"):
        return FileResponse("first_customer.html")
    return {"message": "First customer ops page not found."}


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
    raise HTTPException(status_code=404, detail="Generated website file not found.")


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


# ---------------------------------------------------------------------------
# Public config (safe for frontend — never leak secrets)
# ---------------------------------------------------------------------------

@app.get("/robots.txt")
async def robots_txt():
    from fastapi.responses import PlainTextResponse
    host = os.environ.get("PUBLIC_BASE_URL", "https://leadflow-ai-1vip.onrender.com").rstrip("/")
    body = (
        "User-agent: *\n"
        "Allow: /\n"
        "Disallow: /first-customer\n"
        "Disallow: /go\n"
        "Disallow: /agency\n"
        "Disallow: /docs\n"
        "Disallow: /redoc\n"
        "Disallow: /openapi.json\n"
        f"Sitemap: {host}/sitemap.xml\n"
    )
    # fix f-string properly
    body = (
        "User-agent: *\n"
        "Allow: /\n"
        "Disallow: /first-customer\n"
        "Disallow: /go\n"
        "Disallow: /agency\n"
        "Disallow: /docs\n"
        "Disallow: /redoc\n"
        "Disallow: /openapi.json\n"
        + f"Sitemap: {host}/sitemap.xml\n"
    )
    return PlainTextResponse(body)


@app.get("/sitemap.xml")
async def sitemap_xml():
    from fastapi.responses import Response
    host = os.environ.get("PUBLIC_BASE_URL", "https://leadflow-ai-1vip.onrender.com").rstrip("/")
    urls = [
        "/",
        "/hire",
        "/onboard",
        "/miner",
        "/live_demos/marina_pearl_dental_live.html",
        "/live_demos/nordic_smile_studio_live.html",
    ]
    items = []
    for u in urls:
        pr = "1.0" if u == "/" else "0.8"
        items.append(f"  <url><loc>{host}{u}</loc><changefreq>weekly</changefreq><priority>{pr}</priority></url>")
    xml = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
    xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    xml += "\n".join(items) + "\n</urlset>\n"
    return Response(content=xml, media_type="application/xml")



@app.get("/api/config/public")
async def public_config():
    treasury = os.environ.get("TRON_TREASURY_WALLET_ADDRESS", "").strip()
    usdt_contract = BlockchainVerifier.USDT_TRC20_CONTRACT
    misconfigured = (not treasury) or (treasury == usdt_contract)
    env = os.environ.get("LEADFLOW_ENV", "development")
    return {
        "product": "LeadFlow.AI",
        "version": "4.1.0",
        "environment": env,
        "primary_offer": {
            "name": "Dubai Growth Clinic Website Package",
            "price_usdt": 1499,
            "billing": "one_time",
            "currency": "USDT_TRC20",
            "tiers": [
                {"id": "launch", "price_usdt": 799, "name": "Launch"},
                {"id": "growth", "price_usdt": 1499, "name": "Growth"},
                {"id": "authority", "price_usdt": 2999, "name": "Authority"}
            ],
            "markets": ["Dubai", "UAE", "Istanbul"],
            "languages": ["en", "ar"]
        },
        "treasury_wallet": treasury if not misconfigured else "",
        "treasury_configured": not misconfigured,
        "payments_enabled": not misconfigured and env.lower() in {"production", "prod", "development"},
        "warning": (
            None
            if not misconfigured
            else "TRON_TREASURY_WALLET_ADDRESS is missing or incorrectly set to the USDT contract. Payments disabled."
        ),
        # Never expose bot tokens / API keys here
    }


# ---------------------------------------------------------------------------
# Agents API
# ---------------------------------------------------------------------------
@app.post("/api/analyze")
async def analyze_prospect(request: AnalyzeRequest):
    try:
        research_data = researcher.extract_signals(request.url)
        email_output = copywriter.generate_email(request.prospect_name, research_data)
        return {"status": "success", "research": research_data, "campaign": email_output}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Agent Execution Failed: {str(e)}")


@app.post("/api/verify-payment")
async def verify_payment(request: VerifyPaymentRequest):
    """
    Audits Tron USDT payment on-chain and enforces:
    - no simulation in production (handled in BlockchainVerifier)
    - treasury destination match
    - replay protection via PaymentLedger
    """
    try:
        tx_hash = (request.tx_hash or "").strip()
        if not tx_hash:
            raise HTTPException(status_code=400, detail="tx_hash is required")

        if ledger.has_processed(tx_hash):
            return {
                "status": "replay_rejected",
                "tx_hash": tx_hash,
                "confirmed": False,
                "message": "This transaction hash was already used. Replay rejected.",
                "telegram_alert_sent": False,
            }

        client_info = {"client_name": request.client_name, "plan_name": request.plan_name}
        audit_result = verifier.verify_usdt_transaction(
            tx_hash, request.plan_amount, client_info=client_info
        )

        if audit_result.get("status") == "success":
            ledger.record_success(
                tx_hash=tx_hash,
                amount_usdt=float(audit_result.get("amount_usdt") or 0),
                sender=audit_result.get("sender"),
                receiver=audit_result.get("receiver"),
                client_name=request.client_name,
                plan_name=request.plan_name,
            )
            if request.referrer_id:
                try:
                    affiliate_mgr.register_new_sale(
                        client_name=request.client_name or "New Client",
                        plan_amount_usdt=audit_result.get(
                            "amount_usdt", request.plan_amount or 499.0
                        ),
                        referrer_id=request.referrer_id,
                    )
                except Exception as aff_e:
                    print(f"⚠️ Affiliate commission log warning: {aff_e}")

        return audit_result
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Blockchain Audit Error: {str(e)}")


@app.post("/api/webhook/tron-deposit")
async def tron_deposit_webhook(payload: Dict[str, Any] = Body(...)):
    try:
        tx_hash = payload.get("tx_hash") or payload.get("hash") or payload.get("transaction_id", "")
        plan_amount = float(payload.get("amount", 499.0))
        client_name = payload.get("client_name", payload.get("sender", "Webhook Enterprise Client"))
        plan_name = payload.get("plan_name", "Autonomous AI Agency Tier")

        if not tx_hash:
            raise HTTPException(status_code=400, detail="Missing tx_hash in webhook payload.")

        if ledger.has_processed(tx_hash):
            return {
                "webhook_status": "duplicate_ignored",
                "audit": {
                    "status": "replay_rejected",
                    "tx_hash": tx_hash,
                    "message": "Already processed",
                },
            }

        client_info = {"client_name": client_name, "plan_name": plan_name}
        audit_result = verifier.verify_usdt_transaction(tx_hash, plan_amount, client_info=client_info)
        if audit_result.get("status") == "success":
            ledger.record_success(
                tx_hash=tx_hash,
                amount_usdt=float(audit_result.get("amount_usdt") or 0),
                sender=audit_result.get("sender"),
                receiver=audit_result.get("receiver"),
                client_name=client_name,
                plan_name=plan_name,
            )
        return {"webhook_status": "received_and_processed", "audit": audit_result}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Tron Webhook Error: {str(e)}")


@app.post("/api/mine-businesses")
async def mine_no_website_businesses(request: MineRequest):
    try:
        results = miner.mine_businesses(request.city, request.category, request.limit)
        return results
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Miner Error: {str(e)}")


@app.post("/api/generate-website")
async def generate_luxury_website(request: GenerateSiteRequest):
    try:
        site_result = infiltrator.generate_luxury_site(
            request.business_name,
            request.category,
            request.city,
            request.phone,
            request.custom_domain,
        )
        return site_result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Shadow Infiltrator Error: {str(e)}")


@app.post("/api/affiliate/register-sale")
async def register_affiliate_sale(request: RegisterSaleRequest):
    try:
        res = affiliate_mgr.register_new_sale(
            request.client_name, request.plan_amount_usdt, request.referrer_id
        )
        return res
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Affiliate Error: {str(e)}")


@app.post("/api/affiliate/process-renewals")
async def process_affiliate_renewals():
    try:
        res = affiliate_mgr.process_monthly_renewals()
        return res
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Renewal Error: {str(e)}")


@app.post("/api/voice/call")
async def trigger_voice_outbound_call(request: VoiceCallRequest):
    try:
        res = voice_agent.initiate_outbound_call(
            request.business_name,
            request.phone,
            request.city,
            request.live_cloud_url,
            request.contact_name,
        )
        return res
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Telephony Error: {str(e)}")


@app.post("/api/lead/capture")
async def capture_work_email(request: LeadCaptureRequest):
    try:
        # Durable storage
        durable = ledger.capture_lead(
            request.email, request.name, request.company, request.studio_source
        )
        # Keep in-memory agent response shape for UI compatibility
        res = referral_agent.capture_lead_email(
            request.email, request.name, request.company, request.studio_source
        )
        res["durable_lead_id"] = durable.get("lead_id")
        res["persisted"] = True
        return res
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Lead Capture Error: {str(e)}")


@app.post("/api/referral/reward")
async def grant_ambassador_reward(request: ReferralRewardRequest):
    try:
        res = referral_agent.process_referral_reward(
            request.referrer_code, request.new_client_name, request.reward_choice
        )
        return res
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Referral Reward Error: {str(e)}")


@app.get("/api/health")
async def health_check():
    treasury = os.environ.get("TRON_TREASURY_WALLET_ADDRESS", "").strip()
    return {
        "status": "online",
        "service": "LeadFlow.AI Cloud Engine v4.1",
        "environment": os.environ.get("LEADFLOW_ENV", "development"),
        "treasury_configured": bool(treasury)
        and treasury != BlockchainVerifier.USDT_TRC20_CONTRACT,
        "sim_payments_allowed": verifier.allow_sim_payments,
        "agents": [
            "ResearcherAgent",
            "CopywriterAgent",
            "BlockchainVerifier (hardened)",
            "NoWebsiteMiner",
            "ShadowInfiltrator",
            "AffiliateManager",
            "VoiceOutboundAgent (simulated until keys set)",
            "ReferralRewardsAgent",
            "PaymentLedger",
        ],
    }


if __name__ == "__main__":
    print("🚀 Starting LeadFlow.AI Central Engine on port 8000...")
    uvicorn.run(app, host="0.0.0.0", port=8000)
