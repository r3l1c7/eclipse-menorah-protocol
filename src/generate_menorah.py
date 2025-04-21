#!/usr/bin/env python3
"""
generate_menorah.py

Read processed eclipse data and produce:
 - Chronological list of the eight core lamps (including Shamash)
 - Ordinal pairings (1↔8, 2↔7, 3↔6) with thematic complements
 - A simple timeline chart (menorah.png) plotting each lamp and label

Usage:
    python SRC/generate_menorah.py --output menorah.png
"""
import csv
import sys
from datetime import datetime
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Paths
DATA_DIR = Path(__file__).parent.parent / 'DATA'
PROCESSED_CSV = DATA_DIR / 'processed_eclipses.csv'

# Thematic labels for pairing
THEMES = [
    'Redemption ↔ Jubilee',
    'Booths ↔ Rededication',
    'War‑Week Seal ↔ Siege‑Week Moon'
]

# Lamp positions for labeling
Y_POS = [0, 1, 2, 3, 2, 1, 0, -1]


def load_core_lamps():
    lamps = []
    with open(PROCESSED_CSV, newline='') as fin:
        reader = csv.DictReader(fin)
        for row in reader:
            # Filter: eclipse must have an anchor_window (direct or half-Saros)
            if row['anchor_window']:
                # Keep only total or annular
                if 'Total' in row['type'] or 'Annular' in row['type']:
                    dt = datetime.fromisoformat(row['date'])
                    lamps.append({
                        'datetime': dt,
                        'type': row['type'],
                        'hebrew': f"{row['hebrew_month']}/{row['hebrew_day']}/{row['hebrew_year']}",
                        'window': row['anchor_window'],
                        'feast': row['feast_fast'],
                    })
    # Sort chronologically
    lamps.sort(key=lambda x: x['datetime'])
    if len(lamps) != 8:
        print(f"ERROR: Expected 8 core lamps, found {len(lamps)}", file=sys.stderr)
        sys.exit(1)
    return lamps


def pair_lamps(lamps):
    # ordinal pairing: 1↔8, 2↔7, 3↔6
    pairs = []
    n = len(lamps)
    for i in range(3):
        pairs.append((lamps[i], lamps[n-1-i], THEMES[i]))
    return pairs


def plot_menorah(lamps, output_path):
    dates_list = [lamp['datetime'] for lamp in lamps]
    labels = [f"L{i+1}: {lamp['datetime'].date()}" for i, lamp in enumerate(lamps)]

    fig, ax = plt.subplots(figsize=(12, 2))
    ax.scatter(dates_list, Y_POS, marker='o')
    for i, lamp in enumerate(lamps):
        ax.annotate(labels[i], (dates_list[i], Y_POS[i]), xytext=(0, 8), textcoords='offset points', ha='center')

    ax.xaxis.set_major_locator(mdates.AutoDateLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    ax.get_yaxis().set_visible(False)
    fig.autofmt_xdate(rotation=30)
    fig.tight_layout()
    fig.savefig(output_path)
    print(f"Menorah timeline saved to {output_path}")


def main():
    import argparse
    p = argparse.ArgumentParser(description='Generate the Eclipse Menorah chart')
    p.add_argument('--output', required=True, help='Output image path')
    args = p.parse_args()

    lamps = load_core_lamps()
    pairs = pair_lamps(lamps)

    print("Core Eight Lamps:")
    for idx, lamp in enumerate(lamps, 1):
        print(f"L{idx}: {lamp['datetime'].date()} - {lamp['type']} - {lamp['window']} - Hebrew {lamp['hebrew']} {lamp['feast']}")
    print("
Ordinal Pairings and Themes:")
    for a, b, theme in pairs:
        print(f"{a['datetime'].date()} ↔ {b['datetime'].date()} => {theme}")

    plot_menorah(lamps, args.output)

if __name__ == '__main__':
    main()
