# LeadFlow SEO Agent Fleet

Self-contained SEO agents for LeadFlow (no paid SEO SaaS required).

Inspired by open-source patterns from:
- [JeffLi1993/seo-audit-skill](https://github.com/JeffLi1993/seo-audit-skill)
- [zurd46/AISeoAgent](https://github.com/zurd46/AISeoAgent)
- [Bhanunamikaze/Agentic-SEO-Skill](https://github.com/Bhanunamikaze/Agentic-SEO-Skill)
- [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo)

## Agents

| Agent | File | Job |
|---|---|---|
| Technical SEO | `technical_seo_agent.py` | title/meta/h1/canonical/og/schema/images/lang |
| Local UAE SEO | `local_uae_seo_agent.py` | Dubai/UAE keyword coverage + NAP/local signals |
| Content SEO | `content_seo_agent.py` | draft UAE landing/blog outlines |
| Orchestrator | `run_seo_fleet.py` | audit site + write report + apply safe fixes |

## Run

```bash
cd /home/user/leadflow
python3 seo_agents/run_seo_fleet.py --base-url https://leadflow-ai-1vip.onrender.com
# or local files only:
python3 seo_agents/run_seo_fleet.py --local
```

Reports land in `seo_reports/`.
