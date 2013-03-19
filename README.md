#QuickCal
<img src="http://dl.dropbox.com/u/342698/QuickCal/Example.png" border="0"/>

Sublime Text 3 plugin to show a month calendar

#Settings
These are the available settings at the current time:

```javascript
{
    // Locale for holidays, this is what will get pulled down from holidata.net
    // Please check http://holidata.net/locale_index.html to see available locale
    "locale": "en-US",

    // Sub region of locale.  For example, in the US, a sub region would be a state
    // such as Florida (FL).  If you have doubts about what to use, you can look in
    // one of the JSON files at http://holidata.net/locale_index.html to see what
    // regions are referenced in you locale file.
    "region": "",

    // Start with Sunday first when displaying calendar
    "sunday_first": true
}
```

#Holidays
Holidays are currently downloaded from holidata.net.  They are limited to about one year in advance of the current, and go back as far as 2011.  In the future the ability to import holidays from other sources may be added.

#Commands
Here are the availabe commands.  Example keymap is seen below:

```javascript
    //////////////////////////////////////////////////////////////
    // Calendar Shortcuts
    //////////////////////////////////////////////////////////////
    {
        "keys": ["ctrl+super+alt+c"],
        "command": "calendar"
    },
    {
        "keys": ["ctrl+super+alt+shift+c"],
        "command": "calendar_lookup"
    },
    {
        "keys": ["alt+right"],
        "command": "calendar_month_nav",
        "context":
        [
            {
                "key": "calendar_view"
            }
        ],
        "args": {"reverse": false}
    },
    {
        "keys": ["alt+left"],
        "command": "calendar_month_nav",
        "context":
        [
            {
                "key": "calendar_view"
            }
        ],
        "args": {"reverse": true}
    },
```

##CalendarCommand
Show todays date in the calendar (month view only)

##CalendarLookupCommand
Show an input panel allowing the user to define what day they would like to see in the calendar.  Input is entered month/day/year, where month, day, and year are numerical values.  Any non number delimter can be used, so things like ```3-2-2013``` is also acceptable.

##CalendarMonthNavCommand
A command that can only be run in a calendar view.  It allows you to navigate to the next/previous month.  It takes directional option called reverse, which, if set to ```true```, navigates to the previous month.

#Highlighting current days and holidays
By default, color schemes for the calendar does not show the current day (or day of interest) highlighted, nor does it highlight the holidays.  You must update your color scheme file with something like the following:

```xml
        <dict>
            <key>name</key>
            <string>Calendar Selected Day</string>
            <key>scope</key>
            <string>selected_day</string>
            <key>settings</key>
            <dict>
                <key>foreground</key>
                <string>#2D2D2D</string>
                <key>background</key>
                <string>#F2777A</string>
            </dict>
        </dict>
        <dict>
            <key>name</key>
            <string>Calendar Holiday</string>
            <key>scope</key>
            <string>holiday</string>
            <key>settings</key>
            <dict>
                <key>foreground</key>
                <string>#2D2D2D</string>
                <key>background</key>
                <string>#66CCCC</string>
            </dict>
        </dict>
```
