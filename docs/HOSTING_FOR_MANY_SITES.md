# Hosting strategy for many clinic websites

## Short answer
You do **not** need one paid host per client at the beginning.

## Recommended phases

### Phase 0 — Now (pre-revenue / first sales)
- Keep LeadFlow app on **Render free/starter**
- Keep demos on **same Render service** (`/live_demos/...`) + GitHub Pages mirror
- Cost: ~$0–7/mo
- Goal: sell first packages, not perfect infra

### Phase 1 — After 1–5 paid clients
Buy **one** VPS or shared host (Hetzner/DigitalOcean/Cloudflare Pages + one backend):
- LeadFlow API on one service
- Client static sites as:
  - `client1.yourdomain.com`
  - or `yourdomain.com/client1/`
  - or each client brings their own domain → point DNS to your host
- Cost: typically **$5–20/mo total** for many static sites

### Phase 2 — After 10+ clients
Still often **one** platform:
- Cloudflare Pages / Netlify / S3+CloudFront for static sites (almost free at low traffic)
- One backend for payments/leads
- Optional: separate staging environment

## When you need more than one host
- Strict client isolation / compliance demands
- Very high traffic on one property
- Client insists on their own server account (enterprise)

## What each client actually needs
Most dental/medspa sites are **static HTML + form endpoint**.
That means dozens of sites can live on one cheap host.

## SEO note for multi-site
- Each client should eventually have **their own domain**
- Your LeadFlow marketing site (`/hire`) is separate and should rank for “clinic website Dubai”
- Client sites rank for “dentist Dubai Marina” etc.

## Practical recommendation for you now
1. Stay on free/cheap Render + GitHub Pages until first cash
2. After first sale, buy **one** small VPS or use Cloudflare Pages
3. Do **not** buy separate hosting for every demo
