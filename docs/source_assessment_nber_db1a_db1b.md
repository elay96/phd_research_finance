# Source Assessment — NBER DB1A / DB1B Airline Ticket Data

## Decision

**Do not add the 2.7 GB `nboeALL` archive to this repository.** It is a direct input to the aviation replication and extension tracks, but not to the space-launch track. The repository retains a reproducible processing script and compact derived summaries instead.

The archive contains quarterly U.S. airline origin-and-destination ticket microdata. It can support research on airline fares, passenger flows, routes and carrier market shares; it does not identify launch events, space companies, equity prices, options, returns or implied volatility.

## Local audit

- Local archive: `/Users/elay96/Downloads/nboeALL`
- Size: 2.7 GB
- Contents: 151 quarterly ZIP archives named `nboe*.zip`
- Example archive inspected: `nboe001.zip`
- Example files: `NBOE001.ASC` (fixed-width data), `nboe.dct` (field dictionary), `nboe001.rpt` (processing report), airport-code files

The inspected DB1A dictionary contains airport fields (`apt1`–`apt3`), carrier fields (`cr1`, `cr2`, `crrep`), fare, distance, passenger count and ticket-type fields. This confirms that the collection is airline-ticket data rather than a financial-market or space-sector dataset.

## What DB1B is useful for

DB1B is a quarterly 10% sample of airline tickets from reporting carriers. Its ticket, market and coupon tables are designed for analysis of passenger itineraries, fares, routes, miles and carrier market shares.

It would be relevant only if the project were expanded to an **aviation passenger-market** event study—for example, estimating how airline accidents or route disruptions affect fares or passenger demand. That is a different identification setting from the present launch-failure finance study.

## Recommended data for the current project

Prioritise these additions to `event_master` instead:

1. A validated event narrative and failure-severity classification.
2. Affected-company and ticker mapping, including private-company status.
3. Daily equity returns, benchmark returns and market-cap data.
4. Option implied volatility and trading-volume data where listed options exist.
5. Contract, payload, customer, insurance and news-source evidence.

## Sources

- [BTS DB1B database profile](https://www.transtats.bts.gov/DatabaseInfo.asp?QO_VQ=EFI&Yv0x=D)
- [BTS DB1B ticket-table description](https://www.transtats.bts.gov/TableInfo.asp?QO_fu146_anzr=b4vtv0+n0q+Qr56v0n6v10+f748rB&V0s1_b0yB=D&gnoyr_VQ=FKF)
