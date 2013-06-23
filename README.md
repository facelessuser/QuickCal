# QuickCal
![Example output](http://dl.dropbox.com/u/342698/QuickCal/Example.png "Example output")

Sublime Text 3 plugin to show a month calendar

# Settings
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

# Holidays
Holidays are currently downloaded from holidata.net.
They are limited to about one year in advance of the current, and go back as far as 2011.
In the future the ability to import holidays from other sources may be added.

# Commands
Commands are accessible via the command palette.

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
# License

QuickCal is released under the MIT license.

Copyright (c) 2012 Isaac Muse <isaacmuse@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
