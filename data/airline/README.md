# NBER DB1A / DB1B Source Data

The full 2.7 GB archive is stored locally at `data/airline/raw/nboeALL/` and is excluded from Git. This folder contains 151 quarterly `nboe*.zip` archives.

`scripts/analyze_nber_db1a.py` reads the archive without extracting it permanently and produces a compact quarterly summary in `processed/`. The source archive is relevant to the aviation tracks, not the space track.

Initial results and caveats are in [`docs/nber_db1a_findings.md`](../../docs/nber_db1a_findings.md).

## Extending Coverage

The local archive ends in 2016Q3. If later aviation events are required, manually download the missing quarterly DB1B files from **2016Q4 onward** from the [NBER DOT DB1A/DB1B page](https://www.nber.org/research/data/department-transportation-db1adb1b) or the BTS download service. Place compatible quarterly ZIP files in `raw/nboeALL/`, then rerun:

```bash
python3 scripts/analyze_nber_db1a.py \
  --input-dir data/airline/raw/nboeALL \
  --output-csv data/airline/processed/nber_db1a_quarterly_summary.csv \
  --output-report docs/nber_db1a_descriptive_analysis.md
```
