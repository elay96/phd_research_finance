# Track 3 - Space Launch Failures

Apply the event-study framework to orbital launch failures.

## Current Data

ESA DISCOS provides 119 failure-flagged launches from 2000 onward in `data/space/`.

## Required Enrichment

- Failure narrative and severity.
- Affected company, ticker and exposure classification.
- Returns, IV and benchmark data.
- ContractOverlap: an exposure measure based on shared public-sector customers and project types. USAspending is a candidate source for U.S. federal award data.

## Deliverable

A validated event-level dataset and return/IV event study for listed space-sector exposures.
