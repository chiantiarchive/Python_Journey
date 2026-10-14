

from datetime import datetime
from pathlib import Path

from src.task_loader import load_tasks
from src.task_reporter import save_task_report
from src.date_utils import calculate_reminder_date, format_human_date


def main():
    base_dir = Path(__file__).parent
    input_path = base_dir / "data" / "tasks.csv"
    output_dir = base_dir / "output"

    tasks = load_tasks(input_path)
    today = datetime.now().date()

    print(f"Today: {format_human_date(today)}\n")

    for task in tasks:
        due_date = task["due_date"]
        days_left = (due_date - today).days

        if days_left < 0:
            status = "Overdue"
        elif days_left == 0:
            status = "Due today"
        else:
            status = f"Due in {days_left} day(s)"

        print(
            f"{task['task']} - "
            f"Due: {format_human_date(due_date)} - "
            f"{status}"
        )

    print("\nFollow-up reminders:")

    for task in tasks:
        reminder_date = calculate_reminder_date(task["due_date"])

        print(
            f"{task['task']} - "
            f"Reminder on: {format_human_date(reminder_date)}"
        )

    report_path = save_task_report(tasks, output_dir, datetime.now())

    print(f"\nSaved report: {report_path}")


if __name__ == "__main__":
    main()