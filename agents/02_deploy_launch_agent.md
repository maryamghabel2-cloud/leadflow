# Agent 02 — Deploy Launch Agent
**Mission:** Put FastAPI + static funnel on a public URL with secrets, healthchecks, zero demo tokens in prod.

## Acceptance criteria
1. `https://<service>/api/health` returns online
2. Env vars set on host: `TRON_TREASURY_WALLET_ADDRESS`, `TELEGRAM_BOT_TOKEN`, `ADMIN_CHAT_ID`, `LEADFLOW_ENV=production`
3. `SIM` payments fail in production
4. GitHub Pages continues serving demos; API serves on Render/Railway
5. No secrets committed to git

## Tasks
- [ ] Deploy via `render.yaml` or `docker compose`
- [ ] Wire custom domain later
- [ ] Disable auto `git push` from runtime in production (`CLOUD_AUTO_PUSH=false`)
- [ ] Add uptime monitor

## Commands
```bash
# local
export LEADFLOW_ENV=development
uvicorn web_app:app --reload --port 8000

# prod container
docker compose up --build -d
```
