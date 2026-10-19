

from datetime import date

from src.task_utils import (
    calculate_days_left,
    calculate_reminder_date,
    get_status,
)


def test_calculate_days_left_future():
    due_date = date(2026, 10, 15)
    today = date(2026, 10, 13)

    assert calculate_days_left(due_date, today) == 2


def test_calculate_days_left_today():
    due_date = date(2026, 10, 13)
    today = date(2026, 10, 13)

    assert calculate_days_left(due_date, today) == 0


def test_calculate_days_left_past():
    due_date = date(2026, 10, 10)
    today = date(2026, 10, 13)

    assert calculate_days_left(due_date, today) == -3


def test_status_overdue():
    assert get_status(-1) == "Overdue"


def test_status_due_today():
    assert get_status(0) == "Due today"


def test_status_future():
    assert get_status(4) == "Due in 4 day(s)"


def test_reminder_date():
    due_date = date(2026, 10, 15)
    reminder_date = calculate_reminder_date(due_date)

    assert reminder_date == date(2026, 10, 12)


