

import csv
from datetime import datetime, timedelta
from pathlib import Path


def load_tasks(input_path):
    tasks = []

    with input_path.open("r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            try:
                task = row["task"].strip()
                due_date = datetime.strptime(row["due_date"], "%Y-%m-%d").date()

                tasks.append({
                    "task": task,
                    "due_date": due_date,
                })

            except (KeyError, ValueError) as error:
                print(f"Skipping invalid row {row}: {error}")

    return tasks


def save_task_report(tasks, output_dir):
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
    output_path = output_dir / f"task_report_{timestamp}.txt"

    lines = [
        "Task Due-Date Report",
        f"Generated: {now.strftime('%B %d, %Y at %I:%M %p')}",
        "=" * 40,
    ]

    for task in tasks:
        due_date = task["due_date"]
        days_left = (due_date - now.date()).days

        if days_left < 0:
            status = "Overdue"
        elif days_left == 0:
            status = "Due today"
        else:
            status = f"Due in {days_left} day(s)"

        lines.append(
            f"{task['task']} - Due: {due_date.strftime('%B %d, %Y')} - {status}"
        )

    output_dir.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"\nSaved report: {output_path}")


def main():
    base_dir = Path(__file__).parent
    input_path = base_dir / "input" / "tasks.csv"
    output_dir = base_dir / "output"

    tasks = load_tasks(input_path)
    today = datetime.now().date()

    print(f"Today: {today.strftime('%B %d, %Y')}\n")

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
            f"Due: {due_date.strftime('%B %d, %Y')} - "
            f"{status}"
        )

    print("\nFollow-up reminders:")

    for task in tasks:
        due_date = task["due_date"]
        reminder_date = due_date - timedelta(days=3)

        print(
            f"{task['task']} - "
            f"Reminder on: {reminder_date.strftime('%B %d, %Y')}"
        )

    save_task_report(tasks, output_dir)


if __name__ == "__main__":
    main()