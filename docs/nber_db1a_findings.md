# NBER DB1A / DB1B — Initial Findings

## Processing Result

The local `nboeALL` archive was processed directly from its ZIP files. No raw archive files were copied into Git.

| Measure | Result |
| --- | ---: |
| Quarterly archives processed | 151 |
| Coverage | 1979Q1–2016Q3 |
| Valid fixed-width records | 520,326,214 |
| Sum of source passenger field | 1,231,445,628 |
| Lowest quarterly record count | 952,717 (1980Q4) |
| Highest quarterly record count | 6,143,323 (2016Q2) |

The complete quarterly output is [`data/airline/processed/nber_db1a_quarterly_summary.csv`](../data/airline/processed/nber_db1a_quarterly_summary.csv).

## Descriptive Patterns

- The source passenger-field total rises from 3.80 million in 1979Q1 to 12.70 million in 2016Q3 (+234.7%). This is descriptive, not an estimate of total U.S. passengers without validating DB1A expansion rules.
- The number of distinct airport-itinerary combinations rises from 128,954 to 171,496 (+33.0%), peaking at 185,458 in 2006Q2.
- Passenger-weighted itinerary distance rises from 856.8 to 1,100.8 miles in the summary.
- Reporting-carrier counts vary materially over time: 21–51 by quarter. This makes stable carrier identifiers and merger/codeshare treatment essential for any panel analysis.

## Data-Quality Implications

The passenger-weighted fare field has a sharp peak of 445.14 in 1995Q4, versus 196.11 in 2016Q3. The stored fare value must therefore be validated against the DB1A documentation and checked for changes in coding, sampling or composition before it is used as a continuous economic outcome.

## Relevance to the Three Tracks

| Track | Assessment |
| --- | --- |
| Airline replication | Useful input. The archive contains the carrier, airport, itinerary, distance, passenger and fare fields needed to investigate route overlap. |
| Later aviation events | Incomplete on its own: coverage ends in 2016Q3, so a newer DB1B extract is required for later periods. |
| Space launch failures | Not a direct input. It should not be merged with the ESA DISCOS event file. |

## What It Can and Cannot Establish

The data are suitable for constructing candidate route/itinerary exposure measures. They do **not** contain the original paper's PCTLAP as a ready-made field. Reconstructing PCTLAP still requires the paper's exact definition, a carrier/route concordance, treatment of mergers and codeshares, and validation against the original authors' result.
