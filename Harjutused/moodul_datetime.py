"""
Loo funktsioon convert_timezone(datetime_str: str, from_timezone: str, to_timezone: str) , mis võtab sisendina kuupäeva
ja aja, algse ajavööndi ja sihtajavööndi ning tagastab kuupäeva ja aja sihtajavööndis ISO 8601 standardi järgi.
"""
import datetime
from pytz import timezone


def convert_timezone(datetime_str: str, from_timezone: str, to_timezone: str):
    date_format = "%Y-%m-%d %H:%M:%S"
    datetime_obj = datetime.datetime.strptime(datetime_str, date_format)
    from_timezone_obj = timezone(from_timezone)
    to_timezone_obj = timezone(to_timezone)
    datetime_obj = from_timezone_obj.localize(datetime_obj)
    datetime_obj = datetime_obj.astimezone(to_timezone_obj)
    return datetime_obj

datetime_str = "2023-12-31 12:00:00"
from_timezone = "UTC"
to_timezone = "America/New_York"
result = convert_timezone(datetime_str, from_timezone, to_timezone)
print(result) # 2023-12-31 07:00:00-05:00

"""
Loo funktsioon format_date(date: datetime) , mis võtab sisendina datetime objekti ja tagastab 
selle inimloetavas kuupäevaformaadis."""

import datetime

def format_date(date: datetime.datetime):
    return date.strftime("%d-%m-%Y")

date = datetime.datetime(2023, 12, 31)
result = format_date(date)
print(result) # 31-12-2023