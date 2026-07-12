# LeadFlow.AI

**Autonomous demo website factory + crypto checkout for local businesses.**

> Honest status (2026-07-12): Core demo generation works. Real revenue pipeline is being hardened.  
> Simulated campaign metrics are **not** real cash. See [`REALITY_CHECK.md`](./REALITY_CHECK.md) and [`CEO_AUDIT_REPORT.md`](./CEO_AUDIT_REPORT.md).

## What it is

LeadFlow generates premium one-page marketing sites for local businesses (dental, dining, legal, realty, etc.), hosts a live demo URL, and can verify a **USDT TRC-20** payment before releasing a deployment ZIP.

## Primary commercial offer (current wedge)

| Item | Detail |
|---|---|
| Product | Premium website package |
| Price | **$499 USDT (one-time)** |
| Proof | Free live demo first |
| Delivery | ZIP handover + optional deploy help |

Monthly AI-SDR / telephony upsell is **phase 2** after real website sales.

## Quick start (local)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install pytest  # for tests

export LEADFLOW_ENV=development
export LEADFLOW_ALLOW_SIM_PAYMENTS=true
# For real payments (required in production):
# export TRON_TREASURY_WALLET_ADDRESS=TYourRealTronWalletHere
# export TELEGRAM_BOT_TOKEN=...
# export ADMIN_CHAT_ID=...

uvicorn web_app:app --host 0.0.0.0 --port 8000
```

Open:
- http://localhost:8000/ — marketing portal
- http://localhost:8000/onboard — payment onboarding
- http://localhost:8000/miner — business miner UI
- http://localhost:8000/docs — OpenAPI

## Production env (required)

```bash
export LEADFLOW_ENV=production
export LEADFLOW_ALLOW_SIM_PAYMENTS=false
export TRON_TREASURY_WALLET_ADDRESS=TYourRealWallet  # NOT the USDT contract
export TELEGRAM_BOT_TOKEN=123:ABC
export ADMIN_CHAT_ID=123456789
export LEADFLOW_CORS_ORIGINS=https://your-frontend-domain.com
export CLOUD_AUTO_PUSH=false
```

Deploy:

```bash
docker compose up --build -d
# or push to Render using render.yaml
```

## Security notes

1. Never display the USDT contract (`TR7NHqje...`) as a deposit wallet.
2. Simulation hashes `SIM_TRON_*` are rejected in production.
3. Verifier enforces treasury destination match.
4. Payment ledger blocks tx hash replay.

## Tests

```bash
source .venv/bin/activate
pytest tests/ -q
```

## Agent fleet (ops)

See [`agents/`](./agents/) for execution playbooks:
1. Security Payment
2. Deploy Launch
3. Honest Product
4. Revenue Ops (first $499)
5. Data Integrity
6. QA Regression

## Repo honesty

| Claim | Reality |
|---|---|
| 17 live demos | Real HTML on GitHub Pages |
| $1,996 campaign revenue | **Simulated** (`SIM_TRON_`) |
| Voice calls | Simulated until Vapi/ElevenLabs keys |
| SaaS multi-tenant | Not built yet |

## License

Private / all rights reserved unless otherwise stated by the owner.
