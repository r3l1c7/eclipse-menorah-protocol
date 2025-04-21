#!/usr/bin/env python3
"""
compute_midpoint.py

Verifies that the midpoint of the 2,790-day Essene cycle (starting Oct 7, 2023)
falls exactly on the expected eclipse (the Shamash lamp).
Reads processed eclipse data from DATA/processed_eclipses.csv
and reports which event(s) coincide with the midpoint date.
Exits with error code if no event is found.
"""
import csv
import sys
from datetime import datetime, timedelta
from pathlib import Path

# Constants
START_DATE = datetime(2023, 10, 7)
ESSENE_CYCLE_DAYS = 7 * 364 + 2 * 7  # 2790 days
HALF_CYCLE_DAYS = ESSENE_CYCLE_DAYS // 2  # 1395 days

# File paths
PROCESSED_CSV = Path(__file__).parent.parent / 'DATA' / 'processed_eclipses.csv'


def main():
    midpoint_date = START_DATE + timedelta(days=HALF_CYCLE_DAYS)
    midpoint_str = midpoint_date.date().isoformat()
    print(f"Midpoint date (half of {ESSENE_CYCLE_DAYS} days): {midpoint_str}")

    found = []
    with open(PROCESSED_CSV, newline='') as fin:
        reader = csv.DictReader(fin)
        for row in reader:
            # row['date'] in ISO format, e.g. '2027-08-02T...'  
            event_dt = datetime.fromisoformat(row['date'])
            if event_dt.date().isoformat() == midpoint_str:
                found.append(row)

    if not found:
        print(f"ERROR: No eclipse found on midpoint date {midpoint_str}.")
        sys.exit(1)
    
    print(f"Eclipse(s) on midpoint date {midpoint_str}:")
    for row in found:
        print(f" - {row['date']} | {row['type']} | Hebrew: {row['hebrew_month']}/{row['hebrew_day']}/{row['hebrew_year']} | Window: {row['anchor_window']}")

    sys.exit(0)

if __name__ == '__main__':
    main()
