"""
Kirjutage funktsioon calculate_date_difference(date1: str, date2: str),
mis võtab sisendina kaks kuupäeva ja tagastab nende vahe päevades.
"""

import datetime

def calculate_date_difference(date1: str, date2: str) -> int:
    date_format = "%Y-%m-%d"
    date1 = datetime.datetime.strptime(date1, date_format)
    date2 = datetime.datetime.strptime(date2, date_format)
    return abs((date2 - date1).days)