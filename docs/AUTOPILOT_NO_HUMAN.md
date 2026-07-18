# Autopilot mode (operate without you online)

## Goal
When you are offline/offline-internet, the business can still:
1. attract inbound visitors (SEO pages already live)
2. capture leads automatically
3. generate personalized demos
4. accept USDT payment
5. deliver site + ZIP automatically
6. ping Telegram if configured

## What is automatic NOW
- `/hire` and demo forms -> `/api/lead/capture` -> Autopilot builds demo + stores lead
- `/onboard` payment verify -> Autopilot fulfills order + `/delivery/{token}`
- Admin dashboard: `/autopilot`
- APIs: `/api/autopilot/status|leads|orders|events`

## What is NOT automatic without extra keys
- WhatsApp / Instagram outbound messaging
- Google Search Console button clicking
- Ranking guarantees

## Required env for best unattended mode
```
LEADFLOW_ENV=production
PUBLIC_BASE_URL=https://leadflow-ai-1vip.onrender.com
TRON_TREASURY_WALLET_ADDRESS=T...
TELEGRAM_BOT_TOKEN=...
ADMIN_CHAT_ID=...
LEADFLOW_ALLOW_SIM_PAYMENTS=false
```

## Unattended revenue path
Visitor discovers site via SEO/social -> `/hire` form -> auto demo link -> `/onboard` USDT payment -> auto delivery page.

## If you may go offline for days
1. Keep Render service alive (Starter plan better than Free sleep)
2. Confirm treasury wallet + Telegram envs
3. Share `/hire` link everywhere you can before disconnect
4. Optionally ask a VA only to monitor `/autopilot` and reply hot leads
