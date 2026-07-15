## Operator UI

Use the live command center: `/first-customer` (alias `/go`).

# LeadFlow — Launch & First Revenue Playbook
**CEO mode. No theater. Cash only.**

## Status after this audit session
- Hard audit completed (`CEO_AUDIT_REPORT.md`)
- Payment path hardened (sim gate, treasury check, replay ledger)
- Onboard wallet no longer hardcodes USDT contract
- 6 execution agents written under `agents/`
- **9/9 automated tests passing**
- Still blocked on **your real Tron wallet + deploy credentials** (I cannot invent those)

## What YOU must do in the next 48 hours (non-delegable)

### 1) Create / confirm treasury wallet
- Use a Tron wallet you control (TronLink / hardware)
- Copy the address (starts with `T...`)
- **Never** use `TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t` (that is the USDT contract)

### 2) Push hardened code to GitHub
This workspace has the fixed code. From your machine (with git auth):

```bash
cd leadflow
git add -A
git status
git commit -m "fix: harden payments, honest product offer, agent fleet, tests"
git push origin main
```

### 3) Deploy API (Render recommended — blueprint exists)
1. New Web Service from repo `maryamghabel2-cloud/leadflow`
2. Use Docker / `render.yaml`
3. Set env:
   - `LEADFLOW_ENV=production`
   - `LEADFLOW_ALLOW_SIM_PAYMENTS=false`
   - `TRON_TREASURY_WALLET_ADDRESS=T...your wallet...`
   - `TELEGRAM_BOT_TOKEN` + `ADMIN_CHAT_ID` (optional but useful)
4. Confirm:
   - `GET /api/health` → online, `treasury_configured: true`
   - `GET /api/config/public` → shows your wallet
   - `POST /api/verify-payment` with `SIM_TRON_x` → **fails**

### 4) End-to-end money test ($1 USDT)
1. Send **1 USDT TRC-20** to your treasury
2. Paste real tx hash in `/onboard`
3. Confirm success path + Telegram alert
4. Confirm **replay of same hash fails**

### 5) First sales sprint (14 days)
Follow `agents/04_revenue_ops_agent.md` exactly:
- 1 niche, 1 city, 30 real demos, manual outreach
- Offer: free live demo → $499 ownership
- Target: 1–3 paid clients

## What not to do
- Do not advertise simulated revenue
- Do not auto-call strangers with AI voice yet
- Do not expand to SaaS tiers before 10 website sales
- Do not enable `LEADFLOW_ALLOW_SIM_PAYMENTS` in production

## Definition of “launched”
Only when all are true:
1. Production API live with real treasury
2. Real $1 test payment verified
3. At least one real customer paid ≥ $199
4. Public messaging matches actual product
