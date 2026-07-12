# Agent 05 — Data Integrity Agent
**Mission:** Production never invents fake businesses, fake revenue, or ephemeral leads.

## Rules
1. `NoWebsiteMiner` in production must **fail closed** if Overpass/API fails (no synthetic 555 numbers).
2. Leads stored in SQLite/Postgres, not process memory.
3. Campaign ledgers must include `"mode": "simulation" | "live"`.
4. Affiliate commissions only after verified on-chain payment + treasury match.

## Tasks
- [ ] Add `allow_synthetic_fallback` flag (default False in production)
- [ ] Persist leads from `/api/lead/capture`
- [ ] Fix first_100 ledger summary honesty fields
