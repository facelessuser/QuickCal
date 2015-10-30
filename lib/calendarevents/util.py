"""
General common resources.

Copyright (c) 2015 Kauinoa

License: MIT
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the "Software"), to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of
the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO
THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
from __future__ import unicode_literals
from __future__ import absolute_import
from datetime import timedelta, date
import calendar

MON = 0
TUE = 1
WED = 2
THU = 3
FRI = 4
SAT = 5
SUN = 6

JAN = 1
FEB = 2
MAR = 3
APR = 4
MAY = 5
JUN = 6
JUL = 7
AUG = 8
SEP = 9
OCT = 10
NOV = 11
DEC = 12

WEEKEND = (SAT, SUN)


def get_date_in_month(year, month, weekday, weeknum):
    """Get the date in month."""

    now = date(year, month, 1)
    while(now.weekday() != weekday):
        now += timedelta(days=1)
    if (weeknum > 0):
        num_days = (weeknum - 1) * 7
        if(num_days > 0):
            now += timedelta(days=num_days)
    return now


def last_day_in_month(year, month, weekday):
    """Get last day in month."""

    num_days = calendar.monthrange(year, month)[1]
    my_date = date(year, month, num_days)
    while my_date.weekday() != weekday:
        my_date -= timedelta(days=1)
    return my_date


def is_leap_year(year):
    """Get leap year."""

    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
