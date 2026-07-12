"""Smoke tests for core LeadFlow API routes."""

import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))


@pytest.fixture()
def client(tmp_path, monkeypatch):
    monkeypatch.setenv("LEADFLOW_PAYMENT_DB", str(tmp_path / "p.db"))
    monkeypatch.setenv("LEADFLOW_ENV", "development")
    monkeypatch.setenv("LEADFLOW_ALLOW_SIM_PAYMENTS", "true")
    monkeypatch.setenv("TRON_TREASURY_WALLET_ADDRESS", "TRealTreasuryWalletAddressForTests111")
    for mod in ["web_app", "payment_ledger", "blockchain_verifier"]:
        sys.modules.pop(mod, None)
    from fastapi.testclient import TestClient
    from web_app import app

    return TestClient(app)


def test_health(client):
    r = client.get("/api/health")
    assert r.status_code == 200
    assert r.json()["status"] == "online"


def test_index(client):
    r = client.get("/")
    assert r.status_code == 200


def test_analyze(client):
    r = client.post("/api/analyze", json={"url": "example.com", "prospect_name": "Alex (CEO)"})
    assert r.status_code == 200
    assert r.json()["status"] == "success"
    assert "campaign" in r.json()


def test_generate_website(client):
    r = client.post(
        "/api/generate-website",
        json={
            "business_name": "Smoke Test Clinic",
            "category": "Clinic",
            "city": "Paris",
            "phone": "+33 1 00 00 00",
        },
    )
    assert r.status_code == 200
    body = r.json()
    assert body["status"] == "success"
    assert "live_cloud_demo_url" in body
