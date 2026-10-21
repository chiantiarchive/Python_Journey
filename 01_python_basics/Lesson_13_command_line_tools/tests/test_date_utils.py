

from datetime import date

from src.date_utils import (
    calculate_days_left,
    calculate_reminder_date,
    get_status
)


def test_calculate_days_left():
    due_date = date(2026, 10, 15)
    today = date(2026, 10, 13)

    assert calculate_days_left(due_date, today) == 2



def test_get_status_overdue():
    assert get_status(-1) == "Overdue"


def test_get_status_due_today():
    assert get_status(0) == "Due today"


def test_get_status_future():
    assert get_status(4) == "Due in 4 day(s)"


def test_calculate_reminder_date():
    due_date = date(2026, 10, 15)

    assert calculate_reminder_date(due_date) == date(2026, 10, 12)