#!/usr/bin/python
"""
Important US observance holidays.

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
from datetime import date
from . import util
from . import christian_holidays
from . import federal_holidays


def get_new_years_day(year):
    """Get New Years Day (January 1st)."""

    return federal_holidays.get_new_years_day(year)


def get_valentines_day(year):
    """Get Valentine's Day (February 14th)."""

    return date(year, util.FEB, 14)


def get_easter_sunday(year):
    """Get Easter Sunday."""

    return christian_holidays.get_easter_sunday(year)


def get_thomas_jeffersons_birthday(year):
    """Get Thomas Jefferson's Birthday (April 13th)."""

    return date(year, util.APR, 13)


def get_mothers_day(year):
    """Get Mother's Day (2nd Sunday in May)."""

    return util.get_date_in_month(year, util.MAY, util.SUN, 2)


def get_fathers_day(year):
    """Get Father's Day (3rd Sunday in July)."""

    return util.get_date_in_month(year, util.JUL, util.SUN, 3)


def get_halloween(year):
    """Get Halloween Day (October 31st)."""

    return date(year, util.OCT, 31)


def get_christmas_eve(year):
    """Get Christmas Eve (December 24th)."""

    return christian_holidays.get_christmas_eve(year)


def get_new_years_eve(year):
    """Get New Year's Eve."""

    return date(year, util.DEC, 31)


holidays = {
    "New Year's Day": get_new_years_day,
    "Valentine's Day": get_valentines_day,
    "Thomas Jefferson's Birthday": get_thomas_jeffersons_birthday,
    "Mother's Day": get_mothers_day,
    "Father's Day": get_fathers_day,
    "Easter Sunday": get_easter_sunday,
    "Halloween Day": get_halloween,
    "Christmas Eve": get_christmas_eve,
    "New Year's Eve": get_new_years_eve
}
