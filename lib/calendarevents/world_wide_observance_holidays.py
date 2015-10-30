#!/usr/bin/python
"""
World Wide observance holidays.

Fairly common calendar events recognized in the US.

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


def get_world_braille_day_worldwide(year):
    """Get World Braille Day Worldwide (Jan 4)."""

    return date(year, util.JAN, 4)


def get_international_programmers_day_jan_worldwide(year):
    """Get International Programmers' Day Worldwide (Jan 7)."""

    return date(year, util.JAN, 7)


def get_world_religion_day_worldwide(year):
    """
    Get World Religion Day Worldwide.

    3rd Sunday in January
    """

    return util.get_date_in_month(year, util.JAN, util.SUN, 3)


def get_world_leprosy_day_worldwide(year):
    """
    Get World Leprosy Day Worldwide.

    Last Sunday in January
    """

    return util.last_day_in_month(year, util.JAN, util.SUN)


def get_international_customs_day_worldwide(year):
    """Get International Customs Day Worldwide (Jan 26)."""

    return date(year, util.JAN, 26)


def get_world_wetlands_day_worldwide(year):
    """Get World Wetlands Day Worldwide (Feb 2)."""

    return date(year, util.FEB, 2)


def get_world_day_of_the_sick_worldwide(year):
    """Get World Day Of The Sick Worldwide (Feb 11)."""

    return date(year, util.FEB, 11)


def get_self_injury_awareness_day_worldwide(year):
    """Get Self injury Awareness Day Worldwide (Mar 1)."""

    return date(year, util.MAR, 1)


def get_international_women_day_worldwide(year):
    """Get International Women's Day Worldwide (Mar 8)."""

    return date(year, util.MAR, 8)


def get_world_kidney_day_worldwide(year):
    """
    Get World Kidney Day Worldwide.

    2nd Thursday in March
    """

    return util.get_date_in_month(year, util.MAR, util.THU, 2)


def get_earth_hour_worldwide(year):
    """
    Get Earth Hour Worldwide.

    Last Saturday in March
    """

    return util.last_day_in_month(year, util.MAR, util.SAT)


def get_april_fool_day_worldwide(year):
    """Get April Fool's Day Worldwide (Apr 1)."""

    return date(year, util.APR, 1)


def get_international_day_for_monuments_and_sites_worldwide(year):
    """Get International Day For Monuments And Sites Worldwide (Apr 18)."""

    return date(year, util.APR, 18)


def get_earth_day_worldwide(year):
    """Get Earth Day Worldwide (Apr 22)."""

    return date(year, util.APR, 22)


def get_world_ovarian_cancer_day_worldwide(year):
    """Get World Ovarian Cancer Day Worldwide (May 8)."""

    return date(year, util.MAY, 8)


def get_world_autoimmune_arthritis_day_worldwide(year):
    """Get World Autoimmune Arthritis Day Worldwide (May 20)."""

    return date(year, util.MAY, 20)


def get_african_liberation_day_worldwide(year):
    """Get African Liberation Day Worldwide (May 25)."""

    return date(year, util.MAY, 25)


def get_international_overdose_awareness_day_worldwide(year):
    """Get International Overdose Awareness Day Worldwide (Aug 31)."""

    return date(year, util.AUG, 31)


def get_world_sexual_health_day_worldwide(year):
    """Get World Sexual Health Day Worldwide (Sep 4)."""

    return date(year, util.SEP, 4)


def get_international_programmers_day_sept_worldwide(year):
    """
    Get International Programmers' Day Worldwide.

    Sept 13th unless leap year then it is the 12th
    """

    return date(year, util.SEP, (13 - util.is_leap_year(year)))


def get_world_vegetarian_day_worldwide(year):
    """Get World Vegetarian Day Worldwide (Oct 1)."""

    return date(year, util.OCT, 1)


def get_world_cerebral_palsy_day_worldwide(year):
    """
    Get World Cerebral Palsy Day Worldwide.

    1st Wednesday in October.
    """

    return util.get_date_in_month(year, util.OCT, util.WED, 1)


def get_world_stroke_day_worldwide(year):
    """Get World Stroke Day Worldwide (Oct 29)."""

    return date(year, util.OCT, 29)


def get_world_vegan_day_worldwide(year):
    """Get World Vegan Day Worldwide (Nov 1)."""

    return date(year, util.NOV, 1)


def get_world_prematurity_day_worldwide(year):
    """Get World Prematurity Day Worldwide (Nov 17)."""

    return date(year, util.NOV, 17)


def get_international_men_day_worldwide(year):
    """Get International Men's Day Worldwide (Nov 19)."""

    return date(year, util.NOV, 19)


holidays = {
    "World Braille Day Worldwide": get_world_braille_day_worldwide,
    "International Programmers' Day Worldwide (January)": get_international_programmers_day_jan_worldwide,
    "World Religion Day Worldwide": get_world_religion_day_worldwide,
    "World Leprosy Day Worldwide": get_world_leprosy_day_worldwide,
    "International Customs Day Worldwide": get_international_customs_day_worldwide,
    "World Wetlands Day Worldwide": get_world_wetlands_day_worldwide,
    "World Day Of The Sick Worldwide": get_world_day_of_the_sick_worldwide,
    "Self-injury Awareness Day Worldwide": get_self_injury_awareness_day_worldwide,
    "International Women's Day Worldwide": get_international_women_day_worldwide,
    "World Kidney Day Worldwide": get_world_kidney_day_worldwide,
    "Earth Hour Worldwide": get_earth_hour_worldwide,
    "April Fool's Day Worldwide": get_april_fool_day_worldwide,
    "International Day For Monuments And Sites Worldwide": get_international_day_for_monuments_and_sites_worldwide,
    "Earth Day Worldwide": get_earth_day_worldwide,
    "World Ovarian Cancer Day Worldwide": get_world_ovarian_cancer_day_worldwide,
    "World Autoimmune Arthritis Day Worldwide": get_world_autoimmune_arthritis_day_worldwide,
    "African Liberation Day Worldwide": get_african_liberation_day_worldwide,
    "International Overdose Awareness Day Worldwide": get_international_overdose_awareness_day_worldwide,
    "World Sexual Health Day Worldwide": get_world_sexual_health_day_worldwide,
    "International Programmers' Day Worldwide (September)": get_international_programmers_day_sept_worldwide,
    "World Vegetarian Day Worldwide": get_world_vegetarian_day_worldwide,
    "World Cerebral Palsy Day Worldwide": get_world_cerebral_palsy_day_worldwide,
    "World Stroke Day Worldwide": get_world_stroke_day_worldwide,
    "World Vegan Day Worldwide": get_world_vegan_day_worldwide,
    "World Prematurity Day Worldwide": get_world_prematurity_day_worldwide,
    "International Men's Day Worldwide": get_international_men_day_worldwide
}
