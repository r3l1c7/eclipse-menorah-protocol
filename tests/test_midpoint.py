import csv
import pytest
from datetime import datetime, timedelta
from pathlib import Path

# Import cycle parameters from compute_midpoint
from SRC.compute_midpoint import START_DATE, HALF_CYCLE_DAYS

# Path to processed data
DATA_DIR = Path(__file__).parent.parent / 'DATA'
PROCESSED_CSV = DATA_DIR / 'processed_eclipses.csv'


def test_midpoint_date_computation():
    """
    Verify that the computed midpoint date is exactly 1,395 days after START_DATE.
    """
    midpoint = START_DATE + timedelta(days=HALF_CYCLE_DAYS)
    expected_date = datetime(2023, 10, 7) + timedelta(days=1395)
    assert midpoint.date() == expected_date.date(), \
        f"Midpoint {midpoint.date()} does not match expected {expected_date.date()}"


def test_midpoint_eclipse_presence():
    """
    Ensure there is at least one eclipse entry on the midpoint date in processed_eclipses.csv.
    """
    midpoint = (START_DATE + timedelta(days=HALF_CYCLE_DAYS)).date().isoformat()
    found = False
    with open(PROCESSED_CSV, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            row_date = datetime.fromisoformat(row['date']).date().isoformat()
            if row_date == midpoint:
                found = True
                break
    assert found, f"No eclipse found on midpoint date {midpoint}."
