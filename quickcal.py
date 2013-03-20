 # -*- coding: utf-8 -*-

"""
Calendar Viewer

Copyright (c) 2012 Isaac Muse <isaacmuse@gmail.com>
License: MIT
"""

from datetime import date
import sublime_plugin
import sublime
from QuickCal.lib.enum.enum import enum
import re
from os.path import join, exists
from os import makedirs
import json
import urllib.request

MONTHS = enum("January February March April May June July August September October November December", start=1, name="Months")
WEEKDAYS = enum("Monday Tuesday Wednesday Thursday Friday Saturday Sunday", start=1, name="Days")

# Calendar display resources
CAL_HEADER = "|{0:^69}|\n"
CAL_ROW_TOP_DIV = "-----------------------------------------------------------------------\n"
CAL_ROW_MID_DIV = "-----------------------------------------------------------------------\n"
CAL_ROW_BTM_DIV = "-----------------------------------------------------------------------\n"
# (NO-BREAK SPACE) Unicode point U+00A0 or 0xC2A0: denoted with "."
# "...{0: ^3}..."
# "........."
CAL_CELL_CENTER_HIGHLIGHT = "   {0: ^3}   "
CAL_CELL_OUTER_HIGHLIGHT = "         "
# ". .{0: ^3}. ."
# ". ..... ."
CAL_CELL_CENTER_HOLIDAY = "   {0: ^3}   "
CAL_CELL_OUTER_HOLIDAY = "         "
CAL_CELL_CENTER = "   {0:^3}   "
CAL_CELL_OUTER = "         "
CAL_CELL_EMPTY = "         "
CAL_CELL_EMPTY_WALL = " "
CAL_CELL_WALL = "|"
CAL_HEADER_DAYS = "|   %s   |   %s   |   %s   |   %s   |   %s   |   %s   |   %s   |\n"
CAL_COL_LENGTH = 3
CAL_EVENTS = ""
CAL_HOLIDAYS = {}

QCAL = None

SHORT_MONTH = 30
LONG_MONTH = 31
FEB_MONTH = 28
FEB_LEAP_MONTH = 29
DAYS_IN_WEEK = 7


def get_today():
    obj = date.today()
    return Day(obj.day, MONTHS(obj.month), obj.year)


def tx_day(day):
    m = re.match(r"^(\d+)[^\d](\d+)[^\d](\d+)$", day)
    if m:
        return Day(m.group(2), MONTHS(int(m.group(1))), m.group(3))
    else:
        return get_today()


class CalendarEventListener(sublime_plugin.EventListener):
    def on_query_context(self, view, key, operator, operand, match_all):
        if view.settings().get("calendar_current", None) is not None and view.settings().get("calendar_today", None) is not None:
            if key == "calendar_view":
                return True
        return False


class Day(object):
    def __init__(self, day, month, year):
        self.day = int(day)
        self.month = month
        self.year = int(year)

    def __unicode__(self):
        return self.str

    def __str__(self):
        return ("%d/%d/%d" % (self.month.value, self.day, self.year))


class QuickCal(object):
    def init_holidays(self):
        global CAL_HOLIDAYS
        locale = sublime.load_settings("quickcal.sublime-settings").get("locale", "en-US")
        holiday_list = join(CAL_EVENTS, "%d_%s.json" % (self.year, locale))
        if self.force_update:
            CAL_HOLIDAYS = {}
        if self.year not in CAL_HOLIDAYS:
            if not exists(holiday_list):
                html_file = "http://holidata.net/%s/%d.json" % (locale, self.year)
                try:
                    response = urllib.request.urlretrieve(html_file, holiday_list)
                except:
                    return
            with open(holiday_list, 'r', encoding='utf-8') as f:
                CAL_HOLIDAYS[self.year] = json.loads("[%s]" % ','.join(f.readlines()))

    def list_holidays(self):
        bfr = ""
        dates = CAL_HOLIDAYS.get(self.year, [])
        target = "%4d-%02d-" % (self.year, self.month)
        for date in dates:
            if date["date"].startswith(target):
                if date["region"] in ["", sublime.load_settings("quickcal.sublime-settings").get("region", "")]:
                    bfr += "* %s: %s %s\n" % (
                        date["date"],
                        date["description"],
                        "(Region: %s)" % date["region"] if date["region"] != "" else ""
                    )
        return bfr

    def is_holiday(self, day):
        dates = CAL_HOLIDAYS.get(self.year, [])
        target = "%4d-%02d-%02d" % (self.year, self.month, day)
        for date in dates:
            if date["date"] == target and date["region"] in ["", sublime.load_settings("quickcal.sublime-settings").get("region", "")]:
                return True
        return False

    def is_leap_year(self):
        return ((self.year % 4 == 0) and (self.year % 100 != 0)) or (self.year % 400 == 0)

    def days_in_months(self):
        days = LONG_MONTH
        if self.month == MONTHS.February:
            days = FEB_LEAP_MONTH if self.is_leap_year() else FEB_MONTH
        elif self.month in [MONTHS.September, MONTHS.April, MONTHS.June, MONTHS.November]:
            days = SHORT_MONTH
        return days

    def show_calendar_row(self, first, last, empty_cells=(0, 0)):
        pos = enum("left center right")
        row = ""

        for p in pos:
            row += CAL_CELL_WALL
            if empty_cells[0] > 0:
                row += (CAL_CELL_EMPTY * empty_cells[0]) + (CAL_CELL_EMPTY_WALL * (empty_cells[0] - 1))
                row += CAL_CELL_WALL
            for d in range(first, last):
                is_holiday = self.is_holiday(d)
                if d == self.day and is_holiday:
                    if p == pos.center:
                        row += CAL_CELL_CENTER_HOLIDAY.format(d)
                    else:
                        row += CAL_CELL_OUTER_HIGHLIGHT
                elif d == self.day:
                    if p == pos.center:
                        row += CAL_CELL_CENTER_HIGHLIGHT.format(d)
                    else:
                        row += CAL_CELL_OUTER_HIGHLIGHT
                elif is_holiday:
                    if p == pos.center:
                        row += CAL_CELL_CENTER_HOLIDAY.format(d)
                    else:
                        row += CAL_CELL_OUTER_HOLIDAY
                else:
                    if p == pos.center:
                        row += CAL_CELL_CENTER.format(d)
                    else:
                        row += CAL_CELL_OUTER
                row += CAL_CELL_WALL
            if empty_cells[1] > 0:
                row += (CAL_CELL_EMPTY * empty_cells[1]) + (CAL_CELL_EMPTY_WALL * (empty_cells[1] - 1))
                row += CAL_CELL_WALL
            row += "\n"
        return row

    def show_calendar_header(self):
        bfr = CAL_ROW_TOP_DIV
        bfr += CAL_HEADER.format("%s %d" % (self.month, self.year))
        bfr += CAL_ROW_MID_DIV
        if self.sunday_first:
            bfr += (
                CAL_HEADER_DAYS % (
                    (str(WEEKDAYS.Sunday)[0:CAL_COL_LENGTH],) +
                    tuple(str(WEEKDAYS[x])[0:CAL_COL_LENGTH] for x in range(0, DAYS_IN_WEEK - 1))
                )
            )
        else:
            bfr += (CAL_HEADER_DAYS % tuple(str(WEEKDAYS[x])[0:CAL_COL_LENGTH] for x in range(0, DAYS_IN_WEEK)))
        return bfr

    def show_calendar_month(self, year, month, day=0, sunday_first=True, force_update=False):
        self.year = year
        self.month = month
        self.day = day
        self.sunday_first = sunday_first
        self.force_update = force_update

        self.init_holidays()
        num_days = self.days_in_months()
        weekday_month_start = WEEKDAYS(date(year, month, 1).isoweekday())
        if sunday_first:
            offset = int(weekday_month_start) if weekday_month_start != WEEKDAYS.Sunday else 0
        else:
            offset = int(weekday_month_start) - 1 if weekday_month_start != WEEKDAYS.Sunday else DAYS_IN_WEEK - 1

        start_row = 0
        if (num_days + offset) % DAYS_IN_WEEK:
            end_row = (num_days + offset) / DAYS_IN_WEEK
            end_offset = (DAYS_IN_WEEK * (end_row + 1)) - (num_days + offset)
        else:
            end_row = ((num_days + offset) / DAYS_IN_WEEK) - 1
            end_offset = (DAYS_IN_WEEK * end_row) - (num_days + offset)

        bfr = self.show_calendar_header()
        for r in range(0, int(end_row) + 1):
            bfr += CAL_ROW_MID_DIV
            if r == start_row and offset:
                start = 1
                end = DAYS_IN_WEEK - offset + 1
                empty_cells = (offset, 0)
            elif r == end_row and end_offset:
                start = 1 + DAYS_IN_WEEK - offset + (DAYS_IN_WEEK * (r - 1))
                end = num_days + 1
                empty_cells = (0, end_offset)
            else:
                start = 1 + DAYS_IN_WEEK - offset + (DAYS_IN_WEEK * (r - 1))
                end = start + DAYS_IN_WEEK
                empty_cells = (0, 0)
            bfr += self.show_calendar_row(start, end, empty_cells)
        bfr += CAL_ROW_BTM_DIV

        bfr += self.list_holidays()
        return bfr


class CalendarLookupCommand(sublime_plugin.WindowCommand):
    def lookup(self, value):
        if value != "":
            m = re.match(r"^(\d+)[^\d](\d+)[^\d](\d+)$", value)
            if m:
                win = sublime.active_window()
                if win is not None:
                    win.run_command("calendar", {"day": value})

    def run(self):
        today = get_today()
        # Ask for date
        v = self.window.show_input_panel(
            "Date to Look Up: ",
            str(today),
            self.lookup,
            None,
            None
        )
        v.run_command("select_all")


class CalendarCommand(sublime_plugin.WindowCommand):
    def run(self, day=None):
        calendar_view_exists = False
        for v in self.window.views():
            if v.settings().get("calendar_today", None) is not None:
                view = v
                calendar_view_exists = True
                break

        if not calendar_view_exists:
            view = self.window.new_file()
            view.set_name(".calendar")
            view.settings().set("draw_white_space", "none")
        else:
            view.set_read_only(False)
            self.window.focus_view(view)

        view.run_command("show_calendar", {"day": day})


class ShowCalendarCommand(sublime_plugin.TextCommand):
    def run(self, edit, day):
        view = self.view
        today = get_today() if day is None else tx_day(day)
        bfr = QCAL.show_calendar_month(
            today.year,
            today.month,
            today.day,
            sunday_first=sublime.load_settings("quickcal.sublime-settings").get("sunday_first", True),
            force_update=True
        )
        view.set_syntax_file("Packages/QuickCal/Calendar.tmLanguage")
        view.replace(edit, sublime.Region(0, view.size()), bfr)
        view.sel().clear()
        view.settings().set("calendar_current", {"month": str(today.month), "year": today.year})
        view.settings().set("calendar_today", {"month": str(today.month), "year": today.year, "day": today.day})
        view.set_scratch(True)
        view.set_read_only(True)


class CalendarMonthNavCommand(sublime_plugin.TextCommand):
    def run(self, edit, reverse=False):
        current_month = self.view.settings().get("calendar_current", None)
        today = self.view.settings().get("calendar_today", None)
        if current_month is not None and today is not None:
            self.view.set_read_only(False)
            next = self.next(current_month, today) if not reverse else self.previous(current_month, today)
            self.view.replace(
                edit,
                sublime.Region(0, self.view.size()),
                QCAL.show_calendar_month(
                    next.year,
                    next.month,
                    next.day,
                    sunday_first=sublime.load_settings("quickcal.sublime-settings").get("sunday_first", True)
                )
            )
            self.view.sel().clear()
            self.view.settings().set("calendar_current", {"month": str(next.month), "year": next.year})
            self.view.set_read_only(True)

    def next(self, current, today):
        m = MONTHS(current["month"])
        next = MONTHS(int(m) + 1) if m != MONTHS.December else MONTHS.January
        year = current["year"] + 1 if next == MONTHS.January else current["year"]
        day = today["day"] if today["month"] == str(next) and year == today["year"] else 0
        return Day(day, next, year)

    def previous(self, current, today):
        m = MONTHS(current["month"])
        previous = MONTHS(int(m) - 1) if m != MONTHS.January else MONTHS.December
        year = current["year"] - 1 if previous == MONTHS.December else current["year"]
        day = today["day"] if today["month"] == str(previous) and year == today["year"] else 0
        return Day(day, previous, year)


def plugin_loaded():
    global CAL_EVENTS
    global QCAL
    QCAL = QuickCal()
    CAL_EVENTS = join(sublime.packages_path(), "User", "CalendarEvents")
    if not exists(CAL_EVENTS):
        makedirs(CAL_EVENTS)
