

import csv
from pathlib import Path

base_dir = Path(__file__).parent
input_path = base_dir / "input" / "clients.csv"

with input_path.open("r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row)

