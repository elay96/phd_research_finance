# NBER DB1A / DB1B Source Data

The full 2.7 GB archive is intentionally stored outside Git at `/Users/elay96/Downloads/nboeALL`. This folder contains 151 quarterly `nboe*.zip` archives.

`scripts/analyze_nber_db1a.py` reads the archive without extracting it permanently and produces a compact quarterly summary in `processed/`. The source archive is relevant to the aviation tracks, not the space track.

Initial results and caveats are in [`docs/nber_db1a_findings.md`](../../docs/nber_db1a_findings.md).
