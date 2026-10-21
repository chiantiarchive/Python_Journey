

import csv

from datetime import datetime


def load_tasks(input_path):
    tasks = []

    with input_path.open("r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            try:
                task = row["task"].strip()
                due_date = datetime.strptime(row["due_date"], "%Y-%m-%d").date()

                if not task:
                    print("Skipping a row with empty task name.")

                tasks.append({
                    "task": task,
                    "due_date": due_date,
                })

            except (KeyError, ValueError) as error:
                print(f"Skipping invalid row {row} as {error}")

    return tasks