# Agent 06 — QA Regression Agent
**Mission:** Prevent reintroduction of payment theater and broken launch paths.

## Required tests
```bash
pytest tests/test_payment_security.py -q
pytest tests/test_api_smoke.py -q
```

## Must cover
- SIM bypass blocked in production
- Treasury mismatch rejected
- Replay rejected
- Health + generate-website smoke
- Public config never leaks bot tokens
