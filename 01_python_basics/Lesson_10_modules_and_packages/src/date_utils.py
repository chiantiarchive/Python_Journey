

from datetime import datetime, timedelta


def format_human_date(date):
    return date.strftime("%B %d, %Y")


def format_filename_timestamp(now):
    return now.strftime("%Y-%m-%d_%H-%M-%S")


def calculate_days_left(due_date, today):
    return (due_date - today).days


def get_status(days_left):
    if days_left < 0:
        return "Overdue"
    elif days_left == 0:
        return "Due today"
    else:
        return f"Due in {days_left} day(s)"


def calculate_reminder_date(due_date, days_before=3):
    return due_date - timedelta(days=days_before)