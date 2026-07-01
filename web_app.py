"""
LeadFlow.AI - Central Cloud Engine (Full-Stack Backend)
Powered by FastAPI & Uvicorn.
Orchestrates Autonomous AI Agents (Researcher, Copywriter, Blockchain Verifier)
and serves the 3D frontend interface.
"""

import uvicorn
from fastapi import FastAPI, HTTPException, Body
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any
import os

from researcher_agent import ResearcherAgent
from copywriter_agent import CopywriterAgent
from blockchain_verifier import BlockchainVerifier

app = FastAPI(
    title="LeadFlow.AI Autonomous SDR Engine",
    description="Backend AI API powering live web scraping, personalized email copywriting, and blockchain auditing.",
    version="2.0.0"
)

# Enable CORS for frontend flexibility
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize Agents
researcher = ResearcherAgent(timeout=12)
copywriter = CopywriterAgent(sender_name="Elena", sender_company="LeadFlow.AI")
verifier = BlockchainVerifier(timeout=10)

# Request Models
class AnalyzeRequest(BaseModel):
    url: str = Field(..., example="github.com", description="Target company website URL")
    prospect_name: str = Field(default="Decision Maker", example="David (CEO)", description="Name and role of the prospect")

class VerifyPaymentRequest(BaseModel):
    tx_hash: str = Field(..., description="Tron (TRC-20) USDT Transaction Hash")
    plan_amount: Optional[float] = Field(default=None, description="Expected USDT plan price (e.g. 199 or 499)")

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

@app.post("/api/analyze")
async def analyze_prospect(request: AnalyzeRequest):
    """
    Triggers the autonomous pipeline:
    1. Researcher Agent crawls the live website.
    2. Copywriter Agent synthesizes pain points & crafts personalized email.
    """
    try:
        # Step 1: Research
        research_data = researcher.extract_signals(request.url)
        
        # Step 2: Copywriting
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

@app.get("/api/health")
async def health_check():
    return {
        "status": "online",
        "service": "LeadFlow.AI Cloud Engine",
        "agents": ["ResearcherAgent (Live Web Scraper)", "CopywriterAgent (LLM Logic)", "BlockchainVerifier (Tronscan API)"]
    }

if __name__ == "__main__":
    print("🚀 Starting LeadFlow.AI Central Engine on port 8000...")
    uvicorn.run(app, host="0.0.0.0", port=8000)
