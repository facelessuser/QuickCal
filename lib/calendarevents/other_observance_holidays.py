#!/usr/bin/python
"""
Other assorted observed holidays.

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


def get_kansas_day(year):
    """Get Kansas Day (Jan 29)."""

    return date(year, util.JAN, 29)


def get_groundhog_day(year):
    """Get Groundhog Day (Feb 2)."""

    return date(year, util.FEB, 2)


def get_national_wear_red_day(year):
    """
    Get National Wear Red Day.

    1st Friday in February
    """

    return util.get_date_in_month(year, util.FEB, util.FRI, 1)


def get_st_david_day(year):
    """Get St David Day (Mar 1)."""

    return date(year, util.MAR, 1)


def get_read_across_america_day(year):
    """Get Read Across America Day (Mar 2)."""

    return date(year, util.MAR, 2)


def get_employee_appreciation_day(year):
    """
    Get Employee Appreciation Day.

    1st Friday in March.
    """

    return util.get_date_in_month(year, util.MAR, util.FRI, 1)


def get_st_patrick_day(year):
    """Get St Patrick Day (Mar 17)."""

    return date(year, util.MAR, 17)


def get_national_tartan_day(year):
    """Get National Tartan Day (Apr 6)."""

    return date(year, util.APR, 6)


def get_national_explosive_ordnance_disposal(year):
    """
    Get National Explosive Ordnance Disposal.

    1st Saturday in May
    """

    return util.get_date_in_month(year, util.MAY, util.SAT, 1)


def get_cinco_de_mayo(year):
    """Get Cinco De Mayo (May 5)."""

    return date(year, util.MAY, 5)


def get_national_nurses_day(year):
    """Get National Nurses Day (May 6)."""

    return date(year, util.MAY, 6)


def get_national_missing_children_day(year):
    """Get National Missing Children Day (May 25)."""

    return date(year, util.MAY, 25)


def get_doughnut_day(year):
    """Get Doughnut Day (Jun 5)."""

    return date(year, util.JUN, 5)


def get_d_day(year):
    """Get D-day (Jun 6)."""

    return date(year, util.JUN, 6)


def get_us_army_birthday(year):
    """Get Us Army Birthday (Jun 14)."""

    return date(year, util.JUN, 14)


def get_us_coast_guard_birthday(year):
    """Get Us Coast Guard Birthday (Aug 4)."""

    return date(year, util.AUG, 4)


def get_senior_citizens_day(year):
    """Get Senior Citizens Day (Aug 21)."""

    return date(year, util.AUG, 21)


def get_women_equality_day(year):
    """Get Women Equality Day (Aug 26)."""

    return date(year, util.AUG, 26)


def get_air_force_birthday(year):
    """Get Air Force Birthday (Sep 18)."""

    return date(year, util.SEP, 18)


def get_leif_erikson_day(year):
    """Get Leif Erikson Day (Oct 9)."""

    return date(year, util.OCT, 9)


def get_us_navy_birthday(year):
    """Get Us Navy Birthday (Oct 13)."""

    return date(year, util.OCT, 13)


def get_marine_corps_birthday(year):
    """Get Marine Corps Birthday (Nov 10)."""

    return date(year, util.NOV, 10)


def get_st_nicholas_day(year):
    """Get St Nicholas Day (Dec 6)."""

    return date(year, util.DEC, 6)


def get_feast_of_our_lady_of_guadalupe(year):
    """Get Feast Of Our Lady Of Guadalupe (Dec 12)."""

    return date(year, util.DEC, 12)


def get_us_national_guard_birthday(year):
    """Get Us National Guard Birthday (Dec 13)."""

    return date(year, util.DEC, 13)


def get_kwanzaa(year):
    """Get Kwanzaa (Dec 26)."""

    return date(year, util.DEC, 26)


holidays = {
    "Kansas Day": get_kansas_day,
    "Groundhog Day": get_groundhog_day,
    "National Wear Red Day": get_national_wear_red_day,
    "St David Day": get_st_david_day,
    "Read Across America Day": get_read_across_america_day,
    "Employee Appreciation Day": get_employee_appreciation_day,
    "St Patrick Day": get_st_patrick_day,
    "National Tartan Day": get_national_tartan_day,
    "National Explosive Ordnance Disposal": get_national_explosive_ordnance_disposal,
    "Cinco De Mayo": get_cinco_de_mayo,
    "National Nurses Day": get_national_nurses_day,
    "National Missing Children Day": get_national_missing_children_day,
    "Doughnut Day": get_doughnut_day,
    "D-day": get_d_day,
    "US Army Birthday": get_us_army_birthday,
    "US Coast Guard Birthday": get_us_coast_guard_birthday,
    "Senior Citizens Day": get_senior_citizens_day,
    "Women Equality Day": get_women_equality_day,
    "Air Force Birthday": get_air_force_birthday,
    "Leif Erikson Day": get_leif_erikson_day,
    "US Navy Birthday": get_us_navy_birthday,
    "Marine Corps Birthday": get_marine_corps_birthday,
    "St Nicholas Day": get_st_nicholas_day,
    "Feast Of Our Lady Of Guadalupe": get_feast_of_our_lady_of_guadalupe,
    "Us National Guard Birthday": get_us_national_guard_birthday,
    "Kwanzaa": get_kwanzaa
}
