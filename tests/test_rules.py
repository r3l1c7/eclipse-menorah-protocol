import csv
import pytest
from datetime import datetime, timedelta
from pathlib import Path

# Import the functions and modules under test
from SRC.parse_eclipses import gregorian_to_hebrew, find_anchor_window, compute_half_saros
from SRC.generate_menorah import load_core_lamps
from SRC.compute_midpoint import START_DATE, HALF_CYCLE_DAYS

# Paths
DATA_DIR = Path(__file__).parent.parent / 'DATA'
PROCESSED_CSV = DATA_DIR / 'processed_eclipses.csv'


def test_compute_half_saros_interval():
    # Verify half-Saros interval = 3292 days + 4 hours
    dt = datetime(2014, 4, 15, 0, 0)
    twin = compute_half_saros(dt)
    expected = dt + timedelta(days=3292, hours=4)
    assert twin == expected, "Half-Saros twin computation is incorrect"


def test_midpoint_eclipse_exists():
    # Verify midpoint date lands on an eclipse
    midpoint_date = START_DATE + timedelta(days=HALF_CYCLE_DAYS)
    midpoint_str = midpoint_date.date().isoformat()
    found = False
    with open(PROCESSED_CSV, newline='') as fin:
        reader = csv.DictReader(fin)
        for row in reader:
            evt = datetime.fromisoformat(row['date']).date().isoformat()
            if evt == midpoint_str:
                found = True
                break
    assert found, f"No eclipse found on midpoint date {midpoint_str}"


def test_parse_eclipse_hebrew_conversion():
    # Sample date: 15 Nisan 5774 should map to 2014-04-15
    hy, hm, hd = gregorian_to_hebrew(datetime(2014,4,15))
    assert (hd, hm, hy) == (15, 1, 5774), "Hebrew conversion for 2014-04-15 is incorrect"


def test_anchor_window_identification():
    # Test a date inside war-week window
    dt = datetime(2023,10,10)
    label = find_anchor_window(dt)
    assert label == 'War‑Week 2023', "War-week window not identified correctly"


def test_core_lamp_count():
    # Ensure exactly 8 core lamps are loaded
    lamps = load_core_lamps()
    assert len(lamps) == 8, f"Expected 8 core lamps, got {len(lamps)}"
