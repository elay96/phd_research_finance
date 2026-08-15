# Track 1 — Airline Replication with Implied Volatility

Replicate the original aviation study using its event definition and overlap measure, then add an IV response around each event.

## Inputs

- Original paper, data appendix, code and author data if obtainable.
- NBER DB1A/DB1B for route, carrier, passenger and fare construction.
- Equity returns, benchmark returns and option IV for affected carriers.

## Key Open Item

`PCTLAP` is the critical reconstruction task. In the key paper, it is the percentage of each non-crash airline's revenue passenger miles (RPMs) that comes from routes shared with the crash airline. The authors use the quarter before the crash where possible, define a market by origin and destination, and treat itineraries with no more than one connection as substitutes. This must be rebuilt reproducibly from the ticket data; it is not an off-the-shelf NBER variable.

The key paper uses 25 fatal crashes (1978–1996), 250 non-crash-airline observations, CRSP daily stock data and the DOT O&D ticket data. See [`literature/README.md`](../../literature/README.md).

## Deliverable

A replication table, a return event study, an IV event study and a documented PCTLAP build.
