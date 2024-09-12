from datetime import date, timedelta


def get_previous_month_range() -> tuple[date, date]:
    today_date = date.today()
    last_day = today_date.replace(day=1) - timedelta(days=1)
    first_day = today_date.replace(day=1) - timedelta(days=last_day.day)
    return first_day, last_day


def get_yesterday() -> tuple[date]:
    return date.today() - timedelta(days=1)


def get_today() -> tuple[date]:
    return date.today()
