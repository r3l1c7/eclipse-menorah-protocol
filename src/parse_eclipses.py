#!/usr/bin/env python3
"""
parse_eclipses.py

Reads raw eclipse data from DATA/eclipses.csv, annotates each event with:
 - Hebrew calendar date
 - Feast/Fast flag
 - Anchor-window label (war-week, midpoint, YK/Jubilee)
 - Half‑Saros twin ISO timestamp
Outputs the enriched table to DATA/processed_eclipses.csv.
"""
import csv
from datetime import datetime, timedelta
from pathlib import Path
from pyluach import dates

# --- File paths ---
RAW_CSV = Path(__file__).parent.parent / 'DATA' / 'eclipses.csv'
PROCESSED_CSV = Path(__file__).parent.parent / 'DATA' / 'processed_eclipses.csv'

# --- Constants ---
# Hebrew feast & fast days mapping: (month, day) -> label
FEASTS_FASTS = {
    (1, 15): 'Pesach I',           # Nisan 15
    (1, 16): 'Pesach II',          # Nisan 16
    (3, 6):  'Shavuot',            # Sivan 6
    (7, 15): 'Sukkot I',           # Tishri 15
    (10,10): '10 Tevet Fast',      # Tevet 10
    (4, 17): '17 Tammuz Fast',     # Tammuz 17
    (9, 24): '24 Kislev (Hanukkah Eve)',
}

# Anchor windows for prophetic pivot detection
ANCHOR_WINDOWS = [
    # (start_datetime, end_datetime, label)
    (datetime(2023,10,7) - timedelta(days=7), datetime(2023,10,7) + timedelta(days=7), 'War‑Week 2023'),
    (datetime(2027,8,2), datetime(2027,8,2), 'Midpoint 2027'),
    (datetime(2030,10,28), datetime(2030,11,25), 'YK/Jubilee 2030'),
]

# Half‑Saros interval constants
HALF_SAROS_DAYS = 3292
HALF_SAROS_HOURS = 4

# --- Helper functions ---
def gregorian_to_hebrew(dt: datetime):
    """Convert Gregorian datetime to Hebrew year, month, day."""
    g = dates.GregorianDate(dt.year, dt.month, dt.day)
    h = g.to_heb()
    return h.year, h.month, h.day


def find_anchor_window(dt: datetime) -> str:
    """Return the label of the anchor window dt falls into, if any."""
    for start, end, label in ANCHOR_WINDOWS:
        if start <= dt <= end:
            return label
    return ''


def compute_half_saros(dt: datetime) -> datetime:
    """Compute the half‑Saros twin datetime."""
    return dt + timedelta(days=HALF_SAROS_DAYS, hours=HALF_SAROS_HOURS)


# --- Main processing ---
def main():
    with open(RAW_CSV, newline='') as fin, open(PROCESSED_CSV, 'w', newline='') as fout:
        reader = csv.DictReader(fin)
        fieldnames = reader.fieldnames + [
            'hebrew_year','hebrew_month','hebrew_day',
            'feast_fast','anchor_window','half_saros_iso'
        ]
        writer = csv.DictWriter(fout, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            # Parse Gregorian datetime
            dt = datetime.fromisoformat(row['date'])
            
            # Convert to Hebrew date
            hy, hm, hd = gregorian_to_hebrew(dt)
            # Check feast/fast
            feast = FEASTS_FASTS.get((hm, hd), '')
            
            # Determine which anchor window it or its half-Saros twin hits
            win = find_anchor_window(dt)
            if not win:
                twin = compute_half_saros(dt)
                win = find_anchor_window(twin)
            
            # Compute half-Saros twin timestamp
            half_iso = compute_half_saros(dt).isoformat()

            # Update row
            row.update({
                'hebrew_year':   hy,
                'hebrew_month':  hm,
                'hebrew_day':    hd,
                'feast_fast':    feast,
                'anchor_window': win,
                'half_saros_iso': half_iso,
            })

            writer.writerow(row)


if __name__ == '__main__':
    main()
