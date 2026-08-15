#!/usr/bin/env python3
"""Stream NBER DB1A fixed-width ZIP files into quarterly descriptive summaries."""

from __future__ import annotations

import argparse
import csv
import re
import sys
import zipfile
from collections import Counter
from pathlib import Path


ZIP_PATTERN = re.compile(r"nboe(\d{3})\.zip$", re.IGNORECASE)


def as_int(value: bytes) -> int | None:
    value = value.strip()
    if not value:
        return None
    try:
        return int(value)
    except ValueError:
        return None


def quarter_from_code(code: str) -> tuple[int, int]:
    year_two_digits, quarter = int(code[:2]), int(code[2])
    if quarter not in {1, 2, 3, 4}:
        raise ValueError(f"Invalid quarter code: {code}")
    year = 2000 + year_two_digits if year_two_digits <= 30 else 1900 + year_two_digits
    return year, quarter


def analyse_archive(path: Path) -> dict[str, object]:
    match = ZIP_PATTERN.search(path.name)
    if not match:
        raise ValueError(f"Unexpected archive name: {path.name}")
    year, quarter = quarter_from_code(match.group(1))

    with zipfile.ZipFile(path) as archive:
        members = [entry for entry in archive.namelist() if entry.lower().endswith(".asc")]
        if len(members) != 1:
            raise ValueError(f"Expected one ASC file in {path.name}, found {members}")
        with archive.open(members[0]) as raw_file:
            rows = 0
            valid_rows = 0
            passenger_sum = 0
            fare_x_passengers = 0
            fare_passengers = 0
            distance_x_passengers = 0
            distance_passengers = 0
            carriers: set[bytes] = set()
            routes: set[tuple[bytes, bytes, bytes]] = set()
            ticket_types: Counter[str] = Counter()

            for raw in raw_file:
                rows += 1
                line = raw.rstrip(b"\r\n")
                if len(line) < 52:
                    continue
                pax = as_int(line[34:40])
                if pax is None:
                    continue
                valid_rows += 1
                passenger_sum += pax

                carrier = line[40:42].strip()
                if carrier:
                    carriers.add(carrier)
                route = tuple(field.strip() for field in (line[1:4], line[4:7], line[7:10]))
                routes.add(route)
                ticket_types[line[51:52].decode("latin-1", errors="replace").strip() or "blank"] += 1

                fare = as_int(line[18:22])
                if fare is not None:
                    fare_x_passengers += fare * pax
                    fare_passengers += pax
                distance = as_int(line[30:34])
                if distance is not None:
                    distance_x_passengers += distance * pax
                    distance_passengers += pax

    return {
        "year": year,
        "quarter": quarter,
        "period": f"{year}Q{quarter}",
        "archive": path.name,
        "rows": rows,
        "valid_rows": valid_rows,
        "passenger_sum": passenger_sum,
        "passenger_weighted_mean_fare_as_stored": round(fare_x_passengers / fare_passengers, 4) if fare_passengers else "",
        "passenger_weighted_mean_distance": round(distance_x_passengers / distance_passengers, 4) if distance_passengers else "",
        "unique_reporting_carriers": len(carriers),
        "unique_airport_itineraries": len(routes),
        "ticket_type_counts": "; ".join(f"{key}:{value}" for key, value in sorted(ticket_types.items())),
    }


def write_summary(rows: list[dict[str, object]], output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    fields = list(rows[0])
    with output.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def write_report(rows: list[dict[str, object]], output: Path) -> None:
    total_rows = sum(int(row["valid_rows"]) for row in rows)
    total_passengers = sum(int(row["passenger_sum"]) for row in rows)
    periods = [str(row["period"]) for row in rows]
    output.write_text(
        "# NBER DB1A Quarterly Descriptive Analysis\n\n"
        f"- Archives processed: {len(rows)}\n"
        f"- Coverage: {periods[0]} to {periods[-1]}\n"
        f"- Valid fixed-width records: {total_rows:,}\n"
        f"- Sum of the dataset's passenger field: {total_passengers:,}\n\n"
        "The companion CSV is descriptive only. Fare is reported in the source field's stored units; "
        "its monetary scale must be verified against DB1A documentation before economic interpretation. "
        "The archive supports aviation-route and carrier-overlap construction, not the current space track.\n",
        encoding="utf-8",
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-dir", type=Path, required=True)
    parser.add_argument("--output-csv", type=Path, required=True)
    parser.add_argument("--output-report", type=Path, required=True)
    args = parser.parse_args()

    archives = sorted(args.input_dir.glob("nboe*.zip"), key=lambda item: quarter_from_code(ZIP_PATTERN.search(item.name).group(1)))
    if not archives:
        raise SystemExit("No nboe*.zip archives found.")

    results = []
    for number, archive in enumerate(archives, start=1):
        print(f"[{number}/{len(archives)}] {archive.name}", file=sys.stderr, flush=True)
        results.append(analyse_archive(archive))

    write_summary(results, args.output_csv)
    write_report(results, args.output_report)


if __name__ == "__main__":
    main()
