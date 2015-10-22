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

------

TODO:
    Jan 29  Thursday    Kansas Day  Observance
    Feb 2   Monday  Groundhog Day   Observance
    Feb 6   Friday  National Wear Red Day   Observance first Friday of February
    Mar 1   Sunday  St. David's Day Observance
    Mar 2   Monday  Read Across America Day Observance
    Mar 6   Friday  Employee Appreciation Day   Observance  first Friday in March.
    Mar 17  Tuesday St. Patrick's Day   Observance
    Apr 6   Monday  National Tartan Day Observance
    Apr 22  Wednesday   Administrative Professionals Day Observance is on the Wednesday of the last full week of April
    May 2   Saturday    National Explosive Ordnance Disposal (EOD) Day  Observance   first saturday in May
    May 5   Tuesday Cinco de Mayo   Observance
    May 6   Wednesday   National Nurses Day Observance
    May 25  Monday  National Missing Children's Day Observance
    Jun 5   Friday  Doughnut Day    Observance
    Jun 6   Saturday    D-Day   Observance
    Jun 14  Sunday  U.S. Army Birthday  Observance
    Aug 4   Tuesday U.S. Coast Guard Birthday   Observance
    Aug 21  Friday  Senior Citizens Day Observance
    Aug 26  Wednesday   Women's Equality Day    Observance
    Sep 18  Friday  Air Force Birthday  Observance
    Oct 9   Friday  Leif Erikson Day    Observance
    Oct 13  Tuesday U.S. Navy Birthday  Observance
    Oct 16  Friday  Boss's Day  Observance   on October 16, or the nearest working day
    Nov 10  Tuesday Marine Corps Birthday   Observance
    Dec 6   Sunday  St Nicholas' Day    Observance
    Dec 12  Saturday    Feast of Our Lady of Guadalupe  Observance
    Dec 13  Sunday  U.S. National Guard Birthday    Observance
    Dec 26  Saturday    Kwanzaa (until Jan 1)   Observance
"""
from __future__ import unicode_literals
from __future__ import absolute_import
from datetime import date


def get_kansas_day(year):
    """Get Kansas Day (January 4th)."""

    return date(year, 1, 4)


holidays = {
    "Kansas Day": get_kansas_day
}
