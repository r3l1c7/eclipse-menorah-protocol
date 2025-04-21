Eclipse Menorah Protocol
A transparent, reproducible framework for testing the Eclipse Menorah prophetic pattern—mapping eight “lamp” eclipses (2014–2030) onto a sacred sabbatical/Jubilee timeline anchored at October 7 2023.

At a glance: This project is a fully open‑source, rigorously defined protocol that maps eight key solar and lunar eclipses onto a divine sabbatical/Jubilee timeline from 2014 through 2030. Anchored at the October 7, 2023 Simchat Torah event and bisected by a mathematically precise 2,790‑day Essene cycle midpoint, it reveals a reproducible “menorah” pattern of feast‑and‑fast eclipses.

Why it’s likely right: All selection rules were pre‑registered and locked in before drawing any charts, data comes directly from NASA and Hebrew‑calendar APIs, and four independent prophetic clocks (Daniel’s day‑counts, Essene sabbath math, Jubilee law, and planetary weddings) converge on the same Autumn 2030 window. No after‑the‑fact tweaks survive automated CI checks.

Why it’s amazing & why you should get involved:

Collaborate & Verify: Fork the repo, run the code, and confirm the six core lamps yourself—no hidden criteria.

Contribute & Extend: Propose new tests, enrich the data set, or suggest additional prophetic threads via pull requests.

Predict & Track: Help forecast upcoming markers (2024–2030) and keep the live scoreboard updated.

"A pattern is only as strong as its weakest rule."— Join us in building a transparent, community‑verified bridge between Scripture and the stars.

Warning to Skeptics: All selection rules are pre‑registered, code is open‑source, and future predictions are laid out in advance. Any post‑hoc tweaking will break the build.

📜 Table of Contents
Overview

Pre‑Registered Rules

Data Sources

Project Structure

Getting Started

Usage

Predictions & Scoreboard

Contributing

License

🔭 Overview
The Eclipse Menorah is a symbolic “menorah” of six feast‑and‑fast eclipses plus a central “shamash” midpoint eclipse, drawn from the 2014–2030 record:

Anchor: October 7 2023 (Simchat Torah attack)

Midpoint: Half of a 2,790 day Essene cycle → August 2 2027

Endpoint: October 28 2030 (Essene Yom Kippur) & November 25 2030 (Jubilee solar lamp)

By pairing lamps in strict ordinal slots (1↔8, 2↔7, 3↔6) and matching thematic complements, we test whether these alignments are just random or truly prophetic.

📏 Pre‑Registered Rules
All criteria are locked in RULES.md and cannot be changed without a tracked commit:

Start‑Date: October 7 2023

Cycle Length: 2,790 days (7 × 364 + 2 leap‑weeks)

Shamash: Eclipse that falls exactly at the cycle’s mathematical midpoint

Lamp Selection:

Only total or annular eclipses

Must occur on an Israel‑feast/fast or within ±7 days of one of three anchor windows (war‑week ’23, midpoint ’27, YK/Jubilee ’30)

Pairing: Lamps sorted chronologically, then paired by position (1↔8, 2↔7, 3↔6) and thematic complement

Exclusions: Any eclipse (or its half‑Saros twin) outside the three anchor windows is “auxiliary” and removed from the core six

📊 Data Sources
NASA Five‑Millennium Catalog (2000–2040 total & annular eclipses)

Hebrew Calendar API for feast/fast flags & sunset rollover logic

Half‑Saros Tables from NASA Bulletin #50

All raw CSVs live under DATA/, with scripts to re‑generate them in SRC/.

📂 Project Structure
eclipse-menorah-protocol/
├── RULES.md   # Pre‑registered selection & pairing rules
├── DATA/   # Raw & processed eclipse datasets
├── SRC/   # Parsing, midpoint, menorah & plotting scripts
├── TESTS/   # Unit tests for rules & midpoint
├── PREDICTIONS.md   # Future forecasts & failure modes
├── SCOREBOARD.md   # Live tracking of passed/failed predictions
├── .github/   # CI workflows & issue templates
└── LICENSE   # MIT / CC‑BY license

🚀 Getting Started
Clone this repo and cd into it:
git clone https://github.com/<you>/eclipse-menorah-protocol.git
cd eclipse-menorah-protocol

Set up a virtual environment and install dependencies:
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

Review the immutable rules in RULES.md—no changes allowed post‑registration.

🛠️ Usage
Generate processed data (Hebrew dates, feast flags, half‑Saros links):
python SRC/parse_eclipses.py

Verify midpoint Shamash falls on August 2 2027:
python SRC/compute_midpoint.py

Build the Menorah chart & branch pairings:
python SRC/generate_menorah.py --output menorah.png

Run tests automatically on every push (GitHub Actions will do this too):
pytest

📅 Predictions & Scoreboard
See PREDICTIONS.md for five concrete forecasts (2024–2030).

Check SCOREBOARD.md after each window closes to mark PASS or FAIL.

🤝 Contributing
Fork this repo and create a feature branch (feature/my-rule-test).

Write unit tests in TESTS/ if you propose any new data or edge‑case checks.

Open a Pull Request—CI will auto‑run and show pass/fail.

Discuss in issues or PR comments—but remember: no changes to RULES.md after pre‑registration.

📜 License
This project is licensed under the MIT License (see LICENSE). Data sources carry their own terms (NASA, Hebrew calendar API, etc.), but all code and analysis here is CC‑BY‑4.0 / MIT for maximum openness.

“A pattern is only as strong as its weakest rule.”
— With everything in the open, any failure in date, eclipse type, or pairing will be instantly visible—forcing skeptics either to concede or to engage with the raw, un‑tweakable data.
