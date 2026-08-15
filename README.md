<div align="center">

# 🚀 Launch Failure Finance Research

### Event-study research on failure events, equity returns and implied volatility

`Aviation replication` &nbsp;•&nbsp; `Aviation extension` &nbsp;•&nbsp; `Space launch failures`

</div>

---

## Research Paths

| | Research path | What is available now | Next requirement |
| :---: | --- | --- | --- |
| ✈️ | **Airline replication + IV** | NBER DB1A quarterly summaries, 1979Q1–2016Q3 | Original-paper data/code and PCTLAP reconstruction |
| 📈 | **Later aviation events** | Replication framework and NBER audit | Post-2016 airline data, event definition, returns and IV |
| 🛰️ | **Space launch failures** | 119 ESA DISCOS failure events since 2000 | Company/ticker mapping, returns, IV and contract exposure |

> **Current decision:** evaluate the exact reproducibility of the aviation overlap measure while building a small validated space-event pilot.

## Data at a Glance

```text
data/
├── airline/    NBER-derived quarterly summary — 151 archives processed
└── space/      ESA DISCOS raw API responses + 119-event research table
```

| Dataset | Use | Key limitation |
| --- | --- | --- |
| [NBER DB1A summary](data/airline/processed/nber_db1a_quarterly_summary.csv) | Airline routes, carriers, fares and passengers | Archive ends in 2016Q3; PCTLAP is not a ready-made variable |
| [ESA DISCOS event table](data/space/processed/esa_discos_failed_launches_since_2000.csv) | Launch-failure event universe | Does not identify affected listed firms or market outcomes |

## Start Here

1. [Decision memo](docs/00_decision_memo.md) — comparison of the three designs.
2. [NBER findings](docs/nber_db1a_findings.md) — processing results and data-quality caveats.
3. [Airline replication brief](docs/tracks/01_airline_replication.md) · [later aviation brief](docs/tracks/02_airline_extension.md) · [space brief](docs/tracks/03_space_extension.md).

## Missing Research Inputs

Equity returns, benchmark returns, option implied volatility, company/ticker mapping, `PCTLAP`, `ContractOverlap`, and contract-level USAspending data have **not** yet been added. This repository does not assume that these inputs are already available.
