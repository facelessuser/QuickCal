#!/usr/bin/python
"""
US Federal holidays.

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
from datetime import date
from . import util
from . import christian_holidays


def get_new_years_day(year):
    """Get New Year's Day (January 1st)."""

    return date(year, 1, 1)


def get_martin_luther_king_day(year):
    """
    Get Martin Luther King Day.

    3rd Monday in January.
    """

    return util.get_date_in_month(year, util.JAN, util.MON, 3)


def get_presidents_day(year):
    """
    Get Presidents' Day.

    3rd Monday in February.
    """

    return util.get_date_in_month(year, util.FEB, util.MON, 3)


def get_memorial_day(year):
    """Get Memorial Day (Last Monday in May)."""

    return util.last_day_in_month(year, util.MAY, util.MON)


def get_independence_day_observed(year):
    """
    Get Independence Day Observed.

    If 4th of July falls on Sat, then it will be observed on be Friday the 3rd.
    If 4th of July falls on Sun, then it will be observed on Monday the 5th.
    """

    if date(year, util.JUL, 4).weekday() == util.SAT:
        return date(year, util.JUL, 3)
    elif date(year, util.JUL, 4).weekday() == util.SUN:
        return date(year, util.JUL, 5)
    else:
        return None


def get_independence_day(year):
    """Get Independence Day (July 4th)."""

    return date(year, util.JUL, 4)


def get_labor_day(year):
    """
    Get Labor day.

    1st Monday of September.
    """

    return util.get_date_in_month(year, util.SEP, util.MON, 1)


def get_columbus_day(year):
    """
    Get Columbus Day.

    2nd Monday of October.
    """

    return util.get_date_in_month(year, util.OCT, util.MON, 2)


def get_veterans_day(year):
    """Get Veteran's Day (November 11th)."""

    return date(year, util.NOV, 11)


def get_thanksgiving_day(year):
    """
    Get Thanksgiving day.

    4th Thursday of November.
    """

    return util.get_date_in_month(year, util.NOV, util.THU, 4)


def get_christmas_day(year):
    """Get Christmas (December 25th)."""

    return christian_holidays.get_christmas_day(year)


holidays = {
    "New Year's Day": get_new_years_day,
    "Martin Luther King Day": get_martin_luther_king_day,
    "Presidents' Day": get_presidents_day,
    "Memorial Day": get_memorial_day,
    "Independence Day (Observed)": get_independence_day_observed,
    "Independence Day": get_independence_day,
    "Labor Day": get_labor_day,
    "Columbus Day": get_columbus_day,
    "Veteran's Day": get_veterans_day,
    "Thanksgiving": get_thanksgiving_day,
    "Christmas Day": get_christmas_day
}
