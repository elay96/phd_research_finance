# Track 1 — Airline Replication with Implied Volatility

Replicate the original aviation study using its event definition and overlap measure, then add an IV response around each event.

## Inputs

- Original paper, data appendix, code and author data if obtainable.
- NBER DB1A/DB1B for route, carrier, passenger and fare construction.
- Equity returns, benchmark returns and option IV for affected carriers.

## Key Open Item

`PCTLAP` is the critical reconstruction task. It should be documented as a reproducible function of route or itinerary overlap, not treated as an off-the-shelf NBER variable.

## Deliverable

A replication table, a return event study, an IV event study and a documented PCTLAP build.
