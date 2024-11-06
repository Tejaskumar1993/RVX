from datetime import datetime, timedelta


def format_date(date):
    """Helper function to format date as MM/DD/YYYY."""
    return date.strftime("%m/%d/%Y")


def get_previous_month_range():
    today = datetime.today()
    first_day_of_current_month = today.replace(day=1)
    last_day_of_previous_month = first_day_of_current_month - timedelta(days=1)
    first_day_of_previous_month = last_day_of_previous_month.replace(day=1)
    return format_date(first_day_of_previous_month), format_date(
        last_day_of_previous_month
    )


def get_previous_week_range():
    today = datetime.today()
    start_of_previous_week = today - timedelta(days=today.weekday() + 7)
    end_of_previous_week = start_of_previous_week + timedelta(days=6)
    return format_date(start_of_previous_week), format_date(end_of_previous_week)


def get_quarter_date_range(quarter):
    year = datetime.today().year
    if quarter == 1:
        return format_date(datetime(year, 1, 1)), format_date(datetime(year, 3, 31))
    elif quarter == 2:
        return format_date(datetime(year, 4, 1)), format_date(datetime(year, 6, 30))
    elif quarter == 3:
        return format_date(datetime(year, 7, 1)), format_date(datetime(year, 9, 30))
    elif quarter == 4:
        return format_date(datetime(year, 10, 1)), format_date(datetime(year, 12, 31))
