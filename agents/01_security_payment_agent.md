# Agent 01 — Security Payment Agent
**Mission:** Make payment verification safe enough to accept real USDT without product theft.  
**Owner:** Security / Backend  
**Priority:** P0 — block launch until done

## Scope
- `blockchain_verifier.py`
- `web_app.py` payment endpoints
- `onboard.html` wallet display
- SQLite ledger for processed transactions

## Acceptance criteria
1. In `LEADFLOW_ENV=production`, any `SIM_TRON_*` hash returns **failed**, never success.
2. Verifier requires `TRON_TREASURY_WALLET_ADDRESS` and rejects txs whose TRC-20 `to_address` ≠ treasury.
3. Same `tx_hash` cannot unlock twice (replay protection).
4. UI never shows USDT contract address as deposit wallet.
5. Unit tests in `tests/test_payment_security.py` all green.

## Tasks
- [ ] Remove/gate simulation bypass
- [ ] Enforce treasury match
- [ ] Persist processed hashes
- [ ] Public config endpoint for wallet display
- [ ] Rate-limit `/api/verify-payment` (basic in-memory or middleware)

## Out of scope
- Full KYC, multi-chain, Stripe (phase 2)
