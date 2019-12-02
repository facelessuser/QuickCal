#!/usr/bin/python
"""
Calendar Events.

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
from collections import namedtuple
from datetime import date
from . import christian_holidays
from . import common_observance_holidays
from . import important_observance_holidays
from . import federal_holidays
from . import dst_holidays
from . import other_observance_holidays
from . import world_wide_observance_holidays
from . import us_state_birthday_holidays
import re

WORD_CHARS = re.compile(r'\w', re.UNICODE)


def get_current_year():
    """Get the current year."""

    return date.today().year


def simplify_name(name):
    """Force characters to lower case and remove non work chars."""

    return ''.join([match.group(0) for match in WORD_CHARS.finditer(name.lower().replace(' ', '_'))])


class Holiday(namedtuple('Holiday', ['name', 'date', 'calculate'])):
    """Holiday object."""

    def __repr__(self):
        """String representation."""

        return '{} - {} '.format(self.date, self.name,)


class Holidays(object):
    """Retrieves holidays for the given year."""

    def __init__(self, year):
        """Initialize."""

        self.holidays = {}
        self.year = year

    def update_year(self, year):
        """Update the internal year."""

        self.year = year

        for name, holiday in self.holidays.items():
            self.holidays[name] = Holiday(holiday.name, holiday.calculate(self.year), holiday.calculate)

    def get(self, name):
        """Attempt to retrieve the given holiday."""

        return self.holidays.get(name)

    def get_all(self):
        """Get all holidays."""

        return self.holidays.values()

    def add_holiday(self, name, holiday):
        """
        Add a holiday.

        Duplicates will be ignored.
        """

        simple_name = simplify_name(name)

        if simple_name not in self.holidays:
            if hasattr(holiday, '__call__'):
                d = holiday(self.year)
                self.holidays[simple_name] = Holiday(name, d, holiday)
            elif isinstance(holiday, (list, tuple)) and len(holiday) == 2:
                function = lambda y, m=holiday[0], d=holiday[1]: date(y, m, d)  # noqa: E731
                d = function(self.year)
                self.holidays[simple_name] = Holiday(name, d, function)
            else:
                # I don't know, maybe we should throw an exception...
                # ignore for now
                pass

    def add_holidays(self, holidays):
        """Add a dictionary of holidays."""

        for name, holiday in holidays.items():
            self.add_holiday(name, holiday)


def test():
    """Test function."""

    my_holidays = Holidays(get_current_year())
    my_holidays.add_holidays(christian_holidays.holidays)
    my_holidays.add_holidays(dst_holidays.holidays)
    my_holidays.add_holidays(common_observance_holidays.holidays)
    my_holidays.add_holidays(federal_holidays.holidays)
    my_holidays.add_holidays(important_observance_holidays.holidays)
    my_holidays.add_holidays(other_observance_holidays.holidays)
    my_holidays.add_holidays(world_wide_observance_holidays.holidays)
    my_holidays.add_holidays(us_state_birthday_holidays.holidays)
    print('---- Now ----')
    for day in my_holidays.get_all():
        if day.date is None:
            print('>>>>> Omitted %s' % day.name)
        else:
            print(day)
    print('---- Time Travel ----')
    my_holidays.update_year(1980)
    for day in my_holidays.get_all():
        if day.date is None:
            print('>>>>> Omitted %s' % day.name)
        else:
            print(day)
