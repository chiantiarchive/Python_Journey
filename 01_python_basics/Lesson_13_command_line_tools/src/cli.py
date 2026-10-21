

import argparse
from datetime import datetime
from pathlib import Path

from src.date_utils import(
    calculate_days_left,
    calculate_reminder_date,
    format_human_date,
    get_status,
)

from src.task_loader import load_tasks
from src.task_reporter import save_task_report


def build_parser():
    parser = argparse.ArgumentParser(
        description="Generate a task due-date report."
    )

    parser.add_argument(
        "command",
        choices=["report"],
        help="Action to perform.",
    )

    parser.add_argument(
        "--input",
        default="data/tasks.csv",
        help="Path to the input CSV file."
    )

    parser.add_argument(
        "--output",
        default="output",
        help="Folder where the report will be saved.",
    )

    parser.add_argument(
        "--verbose",
        action="store_true",
        help="show extra progress information.",
    )

    return parser


def run_report(args):
    input_path = Path(args.input)
    output_dir = Path(args.output)

    if args.verbose:
        print(f"Loading task from: {input_path}")

    tasks = load_tasks(input_path)

    if args.verbose:
        print(f"Loaded {len(tasks)} task(s)")

    today = datetime.now().date()

    for task in tasks:
        due_date = task["due_date"]
        days_left = calculate_days_left(due_date, today)
        status = get_status(days_left)

        print(
            f"{task["task"]} - "
            f"Due: {format_human_date(due_date)} - "
            f"{status}"
        )  

    print("\nFollow-up reminders: ")

    for task in tasks:
        reminder_date = calculate_reminder_date(task["due_date"])

        print(
            f"{task["task"]} - "
            f"Reminder on: {reminder_date}"
        )

    report_path = save_task_report(tasks, output_dir, today)

    print(f"\nSaved report: {report_path}")


def main():
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "report":
        run_report(args)