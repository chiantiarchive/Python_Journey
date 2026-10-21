


import csv
from pathlib import Path

from src.task_loader import load_tasks


def test_load_tasks(tmp_path):
    input_path = tmp_path / "tasks.csv"

    with input_path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["task", "due_date"])
        writer.writerow(["Send invoice", "2026-10-15"])

    tasks = load_tasks(input_path)

    assert len(tasks) == 1
    assert tasks[0]["task"]  == "Send invoice"