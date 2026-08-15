# Research Design Decision Memo

## Objective

Evaluate whether failure events affect the market value and implied volatility of exposed firms. The original aviation design is the methodological reference; the space design is the potential new application.

| Track | Core question | Essential missing input | Main risk |
| --- | --- | --- | --- |
| 1. Airline replication + IV | Can the original result be reproduced and extended to options? | Original author data, PCTLAP construction, IV | Exact replication may depend on undocumented data construction |
| 2. Later aviation events | Does the mechanism persist in a newer period? | Event definition, PCTLAP, market and IV data | Comparability with the original setting |
| 3. Space launch failures | Do launch failures affect listed firms and their IV? | Exposure mapping, returns, IV, contract overlap | Many relevant firms are private or indirectly exposed |

## Current Evidence

- The NBER archive can support Track 1: it contains 151 quarterly airline-ticket files (1979Q1–2016Q3) suitable for fares, passengers, routes and carrier-market construction. Track 2 requires a newer extract for post-2016 events.
- ESA DISCOS supports Track 3: it supplies a reproducible launch-failure event universe, but not company exposure or market data.
- No equity-return or IV dataset has been added to this repository yet.

## Recommended Sequencing

1. Obtain the original paper, replication code and—if possible—author data.
2. Use the NBER summary and one or two pilot quarters to establish whether PCTLAP can be reconstructed.
3. In parallel, build a small, manually validated space `event_master` for listed, plausibly exposed firms.
4. Select the track after evaluating coverage of listed firms and IV availability.
