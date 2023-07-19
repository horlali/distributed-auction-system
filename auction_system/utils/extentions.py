from datetime import datetime


def date_string_to_datetime(date_string):
    return datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S")
