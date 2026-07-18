# Agent 08 - Autopilot Engine

## Mission
Keep LeadFlow selling and fulfilling while founder is offline.

## Owns
- `autopilot_engine.py`
- `/api/autopilot/*`
- `/delivery/{token}`
- `/autopilot` dashboard

## Loops
1. Inbound lead -> demo build -> notify
2. Payment success -> fulfill -> delivery URL -> notify
3. Status snapshot for monitoring

## Human only exceptions
- Outbound WhatsApp/IG prospecting
- Google Search Console manual quota actions
- Dispute/refund judgment calls
