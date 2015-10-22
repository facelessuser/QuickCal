#!/usr/bin/python
"""
Common observance holidays.

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
from datetime import timedelta, date
from . import util


def get_stephen_foster_memorial_day(year):
    """Get Stephen Foster Memorial Day (January 13th)."""

    return date(year, util.JAN, 13)


def get_national_freedom_day(year):
    """Get National Freedom Day (February 1st)."""

    return date(year, util.FEB, 1)


def get_shrove_tuesday_mardi_gras(year):
    """Get Mardi Gras (February 17th)."""

    return date(year, util.FEB, 17)


def get_tax_day(year):
    """Get Tax Day (April 15th)."""

    return date(year, util.APR, 15)


def get_take_kid_to_work_day(year):
    """
    Get Take our Daughers and Sons to Work Day.

    4th Thursday in April.
    """

    return util.get_date_in_month(year, util.APR, util.THU, 4)


def get_law_day(year):
    """Get Law Day (May 1st)."""

    return date(year, util.MAY, 1)


def get_loyalty_day(year):
    """Get Loyalty Day (May 1st)."""

    return date(year, util.MAY, 1)


def get_national_day_of_prayer(year):
    """Get National Day of Prayer."""

    return util.get_date_in_month(year, util.MAY, util.THU, 1)


def get_peace_officers_memorial_day(year):
    """Get Peace Officers Memorial Day."""

    return date(year, util.MAY, 15)


def get_national_defense_transportation_day(year):
    """Get National Defence Transportation Day."""

    return util.get_date_in_month(year, util.MAY, util.FRI, 3)


def get_armed_forces_day(year):
    """Get Armed Forces Day."""

    return util.get_date_in_month(year, util.MAY, util.SAT, 3)


def get_national_maritime_day(year):
    """Get National Maritime Day."""

    return date(year, util.MAY, 22)


def get_flag_day(year):
    """Get Flag Day."""

    return date(year, util.JUN, 14)


def get_american_eagle_day(year):
    """Get American Eagle Day."""

    return date(year, util.JUN, 20)


def get_parents_day(year):
    """Get Parents Day."""

    return util.get_date_in_month(year, util.JUL, util.SUN, 4)


def get_purple_heart_day(year):
    """Get Purple Heart Day."""

    return date(year, util.OCT, 7)


def get_national_aviation_day(year):
    """Get National Aviation Day."""

    return date(year, util.OCT, 19)


def get_patriot_day(year):
    """Get Patriot Day."""

    return date(year, util.NOV, 11)


def get_carl_garner_federal_lands_cleanup_day(year):
    """Get Carl Garner Federal Lands Cleanup Day."""

    mydate = util.get_date_in_month(year, util.SEP, util.MON, 0)
    while mydate.weekday() != util.SAT:
        mydate += timedelta(days=1)
    return mydate


def get_national_grandparents_day(year):
    """Get National Grandparents Day."""

    mydate = util.get_date_in_month(year, util.SEP, util.MON, 0)
    while mydate.weekday() != util.SUN:
        mydate += timedelta(days=1)
    return mydate


def get_constitution_day_and_citizenship_day_observed(year):
    """
    Get Constitution Day and/or Citizenship Day Observed.

    If actual day is on Saturday then Firday is observed.
    If actual day is on Sunday then Monday is observed.
    """

    mydate = None
    if (date(year, util.SEP, 17).weekday() == util.SAT):
        mydate = date(year, util.SEP, 16)
    elif (date(year, util.SEP, 17).weekday() == util.SUN):
        mydate = date(year, util.SEP, 18)
    return mydate


def get_constitution_day_and_citizenship_day(year):
    """Get Constitution Day and CitizenshipDay (September 17th)."""

    return date(year, util.SEP, 17)


def get_national_powmia_recognition_day(year):
    """
    Get National POW/MIA Recognition Day.

    3rd Friday in September.
    """

    return util.get_date_in_month(year, util.SEP, util.FRI, 3)


def get_gold_star_mothers_day(year):
    """
    Get Gold Star Mother's Day.

    Last Sunday in September.
    """

    return util.last_day_in_month(year, util.SEP, util.SUN)


def get_child_health_day(year):
    """
    Get Child Health Day.

    First Monday in October.
    """

    return util.get_date_in_month(year, util.OCT, util.MON, 1)


def get_white_cane_safety_day(year):
    """Get White Can Safety Day (October 15th)."""

    return date(year, util.OCT, 15)


def get_cyber_monday(year):
    """
    Get Cyber Monday.

    First Monday after Thanksgiving.
    """

    my_date = util.get_date_in_month(year, util.NOV, util.THU, 4)
    while my_date.weekday() != util.MON:
        my_date += timedelta(days=1)
    return my_date


def get_pearl_harbor_rembrance_day(year):
    """Get Pearl Harbor Remembrance Day (December 7th)."""

    return date(year, util.DEC, 7)


def get_pan_american_aviation_day(year):
    """Get Pan American Aviation Day (December 17th)."""

    return date(year, util.DEC, 17)


def get_wright_brothers_day(year):
    """Get Wright Brothers Day (December 17th)."""

    return date(year, util.DEC, 17)


holidays = {
    "Stephen Foster Memorial Day": get_stephen_foster_memorial_day,
    "National Freedom Day": get_national_freedom_day,
    "Mardi Gras": get_shrove_tuesday_mardi_gras,
    "Tax Day": get_tax_day,
    "Take our Daughters and Sons to Work Day Observance": get_take_kid_to_work_day,
    "Law Day": get_law_day,
    "Loyalty Day": get_loyalty_day,
    "National Day of Prayer": get_national_day_of_prayer,
    "Peace Officers Memorial Day": get_peace_officers_memorial_day,
    "National Defense Transportation Day": get_national_defense_transportation_day,
    "Armed Forces Day": get_armed_forces_day,
    "National Maritime Day": get_national_maritime_day,
    "Flag Day": get_flag_day,
    "American Eagle Day": get_american_eagle_day,
    "Parents' Day": get_parents_day,
    "Purple Heart Day": get_purple_heart_day,
    "National Aviation Day": get_national_aviation_day,
    "Patriot Day": get_patriot_day,
    "Carl Garner Federal Lands Cleanup Day": get_carl_garner_federal_lands_cleanup_day,
    "National Grandparents Day": get_national_grandparents_day,
    "Constitution Day and Citizenship Day (Observed)": get_constitution_day_and_citizenship_day_observed,
    "Constitution Day and Citizenship Day": get_constitution_day_and_citizenship_day,
    "National POW/MIA Recognition Day": get_national_powmia_recognition_day,
    "Gold Star Mother's Day": get_gold_star_mothers_day,
    "Child Health Day": get_child_health_day,
    "White Cane Safety Day": get_white_cane_safety_day,
    "Cyber Monday": get_cyber_monday,
    "Pearl Harbor Remembrance Day": get_pearl_harbor_rembrance_day,
    "Pan American Aviation Day": get_pan_american_aviation_day,
    "Wright Brothers Day": get_wright_brothers_day
}
