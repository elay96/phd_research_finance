# Literature

## Key Paper

| Paper | Why it is central | Local copy |
| --- | --- | --- |
| Bosch, Jean-Claude; Eckard, E. Woodrow; and Singal, Vijay (1998), *The Competitive Impact of Air Crashes: Stock Market Evidence*, **Journal of Law and Economics** 41, 503–519. | This is the methodological anchor for the aviation replication and the template for the space-extension design. It estimates non-crash airlines' abnormal returns around fatal air crashes and relates them to route overlap (`PCTLAP`). | [`1998_Bosch_Eckard_Singal_Competitive_Impact_of_Air_Crashes.pdf`](key_papers/1998_Bosch_Eckard_Singal_Competitive_Impact_of_Air_Crashes.pdf) |

### Design to Replicate

- Sample: 25 fatal crashes from 1978–1996 and 250 non-crash-airline observations.
- Event outcome: cumulative abnormal returns over the `(0, 2)` window, using CRSP daily stock data.
- Competition measure: `PCTLAP`, the percentage of the non-crash airline's RPMs from routes shared with the crash airline.
- Ticket-data source: DOT Ticket Dollar Value Origin & Destination database, a quarterly 10% sample of airline tickets.

### Implication for This Repository

The NBER DB1A archive supplies the raw route/ticket input for rebuilding the overlap measure. Equity returns and implied volatility still need to be acquired separately. The key-paper PDF is included locally for research reference; the large NBER raw archive is local-only and excluded from Git.
