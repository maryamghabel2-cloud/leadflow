"""Payment security regression tests for LeadFlow.AI."""

import os
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))


@pytest.fixture()
def isolated_env(tmp_path, monkeypatch):
    db = tmp_path / "payments.db"
    monkeypatch.setenv("LEADFLOW_PAYMENT_DB", str(db))
    monkeypatch.delenv("TRON_TREASURY_WALLET_ADDRESS", raising=False)
    yield tmp_path


def test_sim_payment_blocked_in_production(isolated_env, monkeypatch):
    monkeypatch.setenv("LEADFLOW_ENV", "production")
    monkeypatch.delenv("LEADFLOW_ALLOW_SIM_PAYMENTS", raising=False)
    from blockchain_verifier import BlockchainVerifier

    v = BlockchainVerifier(treasury_wallet="TRealTreasuryWalletAddressForTests111")
    res = v.verify_usdt_transaction("SIM_TRON_should_fail", 499)
    assert res["status"] in {"failed", "simulation_disabled"}
    assert res.get("confirmed") is False


def test_sim_payment_allowed_in_dev(isolated_env, monkeypatch):
    monkeypatch.setenv("LEADFLOW_ENV", "development")
    monkeypatch.setenv("LEADFLOW_ALLOW_SIM_PAYMENTS", "true")
    from blockchain_verifier import BlockchainVerifier

    v = BlockchainVerifier(treasury_wallet="TRealTreasuryWalletAddressForTests111")
    res = v.verify_usdt_transaction("SIM_TRON_dev_ok", 499)
    assert res["status"] == "success"
    assert res.get("simulation") is True


def test_usdt_contract_as_treasury_rejected(isolated_env, monkeypatch):
    monkeypatch.setenv("LEADFLOW_ENV", "production")
    monkeypatch.setenv("LEADFLOW_ALLOW_SIM_PAYMENTS", "false")
    from blockchain_verifier import BlockchainVerifier

    v = BlockchainVerifier(treasury_wallet=BlockchainVerifier.USDT_TRC20_CONTRACT)
    # Non-sim path with fake hash will attempt API; still misconfigured first if we short-circuit
    # Force non-sim hash
    res = v.verify_usdt_transaction("a" * 64, 499)
    assert res["status"] == "misconfigured"


def test_replay_protection_via_api(isolated_env, monkeypatch):
    monkeypatch.setenv("LEADFLOW_ENV", "development")
    monkeypatch.setenv("LEADFLOW_ALLOW_SIM_PAYMENTS", "true")
    monkeypatch.setenv("TRON_TREASURY_WALLET_ADDRESS", "TRealTreasuryWalletAddressForTests111")

    # Re-import app stack cleanly
    for mod in [
        "payment_ledger",
        "blockchain_verifier",
        "web_app",
    ]:
        sys.modules.pop(mod, None)

    from fastapi.testclient import TestClient
    from web_app import app

    client = TestClient(app)
    payload = {
        "tx_hash": "SIM_TRON_replay_test_001",
        "plan_amount": 499,
        "client_name": "Replay Test Co",
    }
    r1 = client.post("/api/verify-payment", json=payload)
    assert r1.status_code == 200
    assert r1.json()["status"] == "success"

    r2 = client.post("/api/verify-payment", json=payload)
    assert r2.status_code == 200
    assert r2.json()["status"] == "replay_rejected"


def test_public_config_hides_missing_wallet(isolated_env, monkeypatch):
    monkeypatch.delenv("TRON_TREASURY_WALLET_ADDRESS", raising=False)
    for mod in ["web_app", "blockchain_verifier", "payment_ledger"]:
        sys.modules.pop(mod, None)
    from fastapi.testclient import TestClient
    from web_app import app

    client = TestClient(app)
    r = client.get("/api/config/public")
    assert r.status_code == 200
    body = r.json()
    assert body["treasury_configured"] is False
    assert "TELEGRAM" not in str(body)
    assert "token" not in str(body).lower() or "bot" not in str(body).lower()
