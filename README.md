# Launch Failure Finance Research

Research workspace for evaluating three event-study designs that combine market returns and implied volatility (IV).

| Track | Research design | Current status |
| --- | --- | --- |
| 1. Airline replication | Replicate the original aviation study and add IV | NBER DB1A/DB1B audit and quarterly summary in progress |
| 2. Airline extension | Apply the original design to later aviation events | Design pending original-paper review and event definition |
| 3. Space extension | Apply the design to orbital launch failures | 119 ESA DISCOS failure events since 2000 are available |

## Repository Map

```text
data/
  airline/       NBER-derived summaries; source archive remains outside Git
  space/         ESA DISCOS raw responses and processed failure-event table
docs/
  00_decision_memo.md
  tracks/        One brief for each research path
scripts/         Reproducible data-processing code
```

## Available Data

- `data/space/processed/esa_discos_failed_launches_since_2000.csv`: 119 launch failures from 2000 onward.
- `data/space/raw/esa_discos/`: preserved ESA DISCOS API responses.
- `data/airline/processed/`: quarterly NBER DB1A summaries generated locally from the 151-file archive.

## Not Yet Acquired

The repository does not yet contain equity returns, benchmark returns, option implied volatility, company/ticker mappings, PCTLAP, ContractOverlap or contract-level USAspending extracts. These are the next research inputs, not assumed available.

See [the decision memo](docs/00_decision_memo.md) for scope, data requirements and next steps.
