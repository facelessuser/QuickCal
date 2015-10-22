#!/usr/bin/python
"""
Christian holidays.

A number are specifically Catholic, but things like Christmas and Easter are very much recognized by all other
Christian sects.

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
from . import util
import sys

PY3 = sys.version_info >= (3, 0) and sys.version_info < (4, 0)

if PY3:
    from functools import lru_cache
else:
    def lru_cache(maxsize=100, typed=False):
        """Dummy cache for PY2."""

        def decorator(target):
            """Dummy decorator."""

            return target

        return decorator


def get_epiphany(year):
    """
    Get Three Kings' Day.

    In the United States, is on January 6.
    """

    return date(year, util.JAN, 6)


def get_ash_wednesday(year):
    """
    Get Ash Wednesday.

    Ash Wednesday date of Easter - 6 weeks = Sunday of Lent
    Sunday of lent - 4 days = Ash Wednesday
    """

    return get_easter_sunday(year) - timedelta((6 * 7) + 4)


def get_palm_sunday(year):
    """
    Get Palm Sunday.

    The Sunday before Easter.
    """

    return get_easter_sunday(year) - timedelta(7)


def get_maundy_thursday(year):
    """
    Get Maundy Thursday.

    The day before Good Friday.
    """

    return get_easter_sunday(year) - timedelta(3)


def get_good_friday(year):
    """
    Get Good Friday.

    2 Days before Easter Sunday.
    """

    return get_easter_sunday(year) - timedelta(2)


def get_holy_saturday(year):
    """
    Get Holy Saturday.

    1 day before Easter Sunday.
    """

    return get_easter_sunday(year) - timedelta(1)


@lru_cache()
def get_easter_sunday(year):
    """Get Easter Sunday."""

    a = year % 19
    b = year // 100
    c = year % 100
    d = (19 * a + b - b // 4 - ((b - (b + 8) // 25 + 1) // 3) + 15) % 30
    e = (32 + 2 * (b % 4) + 2 * (c // 4) - d - (c % 4)) % 7
    f = d + e - 7 * ((a + 11 * d + 22 * e) // 451) + 114
    month = f // 31
    day = f % 31 + 1
    return date(year, month, day)


def get_easter_monday(year):
    """
    Get Easter Munday.

    Easter + 1 day.
    """

    return get_easter_sunday(year) + timedelta(1)


def get_ascension_day(year):
    """
    Get Ascension day.

    Easter Sunday + 39 days on a Thursday.
    """

    return get_easter_sunday(year) + timedelta(39)


def get_pentecost(year):
    """
    Get Pentecost.

    Easter Sunday + 49 days on a Sunday.
    """

    return get_easter_sunday(year) + timedelta(49)


def get_whit_monday(year):
    """
    Get Whit Monday.

    Pentecost + 1 day or Easter + 50 days.
    """

    return get_easter_sunday(year) + timedelta(50)


def get_trinity_sunday(year):
    """
    Get Trinity Sunday.

    Pentecost + 1 week or Easter + 56 days on a Sunday.
    """

    return get_easter_sunday(year) + timedelta(56)


def get_corpus_christi(year):
    """
    Get Corpus Christi.

    Thursday after Trinity Sunday.
    """

    return get_easter_sunday(year) + timedelta(60)


def get_assumption_of_mary(year):
    """Get Assumption of Mary (August 15th)."""

    return date(year, util.AUG, 15)


def get_feast_of_st_francis_of_assisi(year):
    """Get Feast of St Francis of Assisi (October 4th)."""

    return date(year, util.OCT, 4)


def get_all_saints_day(year):
    """Get All Saints Day (November 1st)."""

    return date(year, util.NOV, 1)


def get_all_souls_day(year):
    """Get All Souls Day (November 2nd)."""

    return date(year, util.NOV, 2)


def get_first_sunday_of_advent(year):
    """
    Get First Sunday of Advent.

    Find the Sunday closest to St Andrew's Day (November 30th).
    """

    date_fwd = date(year, util.NOV, 30)
    date_bkwd = date(year, util.NOV, 30)
    while date_fwd.weekday() != util.SUN and date_bkwd.weekday() != util.SUN:
        date_fwd += timedelta(days=1)
        date_bkwd -= timedelta(days=1)

    if(date_bkwd.weekday() == util.SUN):
        return date_bkwd
    else:
        return date_fwd


def get_feast_of_the_immaculate_conception(year):
    """Get Feast of the Immaculate Conception (December 8th)."""

    return date(year, util.DEC, 8)


def get_christmas_eve(year):
    """Get Christmas Eve (December 24)."""
    return date(year, util.DEC, 24)


def get_christmas_day(year):
    """Get Christmas Day (December 25)."""

    return date(year, util.DEC, 25)


holidays = {
    "Three Kings' Day": get_epiphany,
    "Ash Wednesday": get_ash_wednesday,
    "Palm Sunday": get_palm_sunday,
    "Maundy Thursday": get_maundy_thursday,
    "Good Friday": get_good_friday,
    "Holy Saturday": get_holy_saturday,
    "Easter Sunday": get_easter_sunday,
    "Easter Monday": get_easter_monday,
    "Ascension Day": get_ascension_day,
    "Pentecost": get_pentecost,
    "Whit Monday": get_whit_monday,
    "Trinity Sunday": get_trinity_sunday,
    "Corpus Christi": get_corpus_christi,
    "Assumption of Mary": get_assumption_of_mary,
    "Feast of St Francis of Assisi": get_feast_of_st_francis_of_assisi,
    "All Saints Day": get_all_saints_day,
    "All Souls' Day": get_all_souls_day,
    "First Sunday of Advent": get_first_sunday_of_advent,
    "Feast of the Immaculate Conception": get_feast_of_the_immaculate_conception,
    "Christmas Eve": get_christmas_eve,
    "Christmas Day": get_christmas_day
}
