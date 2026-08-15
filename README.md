# 🚀 Launch Failure Finance Research

An event-study research dataset on the financial effects of orbital launch failures.

`ESA DISCOS v2` `119 Failure Events` `2000–2026`

## 📊 Current Dataset

| File | Description |
| --- | --- |
| `data/processed/esa_discos_failed_launches_since_2000.csv` | Analysis-ready table of 119 launch failures, sorted newest to oldest |
| `data/raw/esa_discos/` | Original ESA DISCOS API responses, retained for reproducibility |
| `docs/data_dictionary.md` | Field definitions, coverage and limitations |

## 🧾 Available Now

- Launch date, flight number, COSPAR number and failure flag
- Vehicle and launch-site details for all 119 events
- Linked organisations or countries for 44 events
- Raw API data and a processed CSV table

## ➡️ Next Step

Build an `event_master` that connects each failure to affected companies, tickers, returns, implied volatility and validated event sources.

## 📚 Source

ESA DISCOS (Database and Information System Characterising Objects in Space). Please retain ESA attribution when using or redistributing derived data.
