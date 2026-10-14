

from pathlib import Path

from src.date_utils import (
    calculate_days_left, 
    format_filename_timestamp, 
    format_human_date, 
    get_status,
    )


def build_task_lines(tasks, today):
    lines = [
        "Task Due-Date Report",
        f"Generated: {format_human_date(today)}",
        "=" * 40,
    ]

    for task in tasks:
        due_date = task["due_date"]
        days_left = calculate_days_left(due_date, today)
        status = get_status(days_left)

        lines.append(
            f"{task['task']} - "
            f"Due: {format_human_date(due_date)} - "
            f"{status}"
        )

    return lines


def save_task_report(tasks, output_dir, now):
    timestamp = format_filename_timestamp(now)
    output_path = output_dir / f"task_report_{timestamp}.txt"

    lines = build_task_lines(tasks, now.date())
    lines.append("=" * 40)

    output_dir.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    return output_path