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

# Request Models
class AnalyzeRequest(BaseModel):
    url: str = Field(..., example="github.com", description="Target company website URL")
    prospect_name: str = Field(default="Decision Maker", example="David (CEO)", description="Name and role of the prospect")

class VerifyPaymentRequest(BaseModel):
    tx_hash: str = Field(..., description="Tron (TRC-20) USDT Transaction Hash")
    plan_amount: Optional[float] = Field(default=None, description="Expected USDT plan price (e.g. 199 or 499)")

class MineRequest(BaseModel):
    city: str = Field(default="Toronto", example="London", description="Target geographic city")
    category: str = Field(default="clinic", example="restaurant", description="Business category/niche")
    limit: int = Field(default=6, ge=1, le=20, description="Number of businesses to discover")

class GenerateSiteRequest(BaseModel):
    business_name: str = Field(..., example="Apex Dental Clinic", description="Name of the business")
    category: str = Field(default="Clinic", description="Business category")
    city: str = Field(default="Toronto", description="City location")
    phone: str = Field(default="+1 (555) 019-2831", description="Contact phone number")

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
    Audits Tron USDT payment on-chain via Tronscan API.
    """
    try:
        audit_result = verifier.verify_usdt_transaction(request.tx_hash, request.plan_amount)
        return audit_result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Blockchain Audit Error: {str(e)}")

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
    Instantly compiles an Awwwards-style 3D neon website tailored for a local business without a website.
    """
    try:
        site_result = infiltrator.generate_luxury_site(request.business_name, request.category, request.city, request.phone)
        return site_result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Shadow Infiltrator Error: {str(e)}")

@app.get("/api/health")
async def health_check():
    return {
        "status": "online",
        "service": "LeadFlow.AI Cloud Engine v3.0",
        "agents": [
            "ResearcherAgent (Live Web Scraper)",
            "CopywriterAgent (LLM Logic)",
            "BlockchainVerifier (Tronscan API)",
            "NoWebsiteMiner (OpenStreetMap / Directory Scraper)",
            "ShadowInfiltrator (Instant 3D Neon Website Generator)"
        ]
    }

if __name__ == "__main__":
    print("🚀 Starting LeadFlow.AI Central Engine on port 8000...")
    uvicorn.run(app, host="0.0.0.0", port=8000)
