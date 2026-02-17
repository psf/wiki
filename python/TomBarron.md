# TomBarron

::: {#content dir="ltr" lang="en"}
This is my user page. I\'m going to use it to build docs I need that may then be worth moving elsewhere. To begin with\...

# Dates and Times {#Dates_and_Times}

Python has two modules that relate to dates and times (that I know of so far):

- datetime
- time

These are reasonably well documented in the online material, but I have not so far found a page or site that pulls all the information about these modules together in one place so one can understand how they relate to each other. This section is an attempt at that. First, an overview of the modules.

## datetime

The datetime module defines five classes:

- date - a date (year, month, day)
- time - a time within a day (hour, minute, second)
- datetime - combines a datetime.date and datetime.time
- timedelta - different between two datetime objects
- tzinfo - \"abstract base class for time zone info objects\" \[1\]

## time

The time module defines one class:

- time - access to system time with some formatting support

I found myself confused by a couple of aspects of these modules:

- datetime.time and time.time are completely different despite sharing a name.
- \'datetime\' is the name of both a module and a class.

From time.time, we can get the system time. We can then pass that information into an object of one of the datetime classes for more sophisticated formatting and date/time arithmetic. Some examples:

### What time is it? {#What_time_is_it.3F}

    >>> import time
    >>> now = time.time()
    >>> now
    1194011556.6974411
    >>> int(now)
    1194011556
    >>> import datetime
    >>> today = datetime.datetime.now()
    >>> today
    datetime.datetime(2007, 11, 2, 10, 33, 35, 713125)
    >>> print today
    2007-11-02 10:33:35.713125

### How about in human-friendly format? {#How_about_in_human-friendly_format.3F}

    >>> import time
    >>> time.asctime()
    'Fri Nov  2 09:55:28 2007'

### I don\'t like that format. How can I roll my own? {#I_don.27t_like_that_format._How_can_I_roll_my_own.3F}

    >>> import time
    >>> time.strftime("%Y/%m/%d %H:%M:%S")
    '2007/11/02 09:58:30'

The various format specifiers are described in the documentation for the time module at [http://docs.python.org/lib/module-time.html](http://docs.python.org/lib/module-time.html){.http}.

### What was the date 24 hours ago? {#What_was_the_date_24_hours_ago.3F}

    >>> import time
    >>> now = time.time()
    >>> now = now - 24 * 60 * 60
    >>> time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(now))
    '2007/11/01 10:00:32'

### I have a string representing a date/time. How do I turn it into something I can do computations on? {#I_have_a_string_representing_a_date.2Ftime._How_do_I_turn_it_into_something_I_can_do_computations_on.3F}

    >>> import time
    >>> then_str = "7 March 2000 4:38"
    >>> time.strptime(then_str, "%d %B %Y %H:%M")
    (2000, 3, 7, 4, 38, 0, 1, 67, -1)
    >>> (y, m, d, h, min, sec, wd, julian, dst) = time.strptime(then_str, "%d %B %Y %H:%M")
    >>> x = []
    >>> x = time.strptime(then_str, "%d %B %Y %H:%M")
    >>> x
    (2000, 3, 7, 4, 38, 0, 1, 67, -1)
    ...

### How do I turn the tuple into a timestamp (number of seconds since the epoch)? {#How_do_I_turn_the_tuple_into_a_timestamp_.28number_of_seconds_since_the_epoch.29.3F}

    ...
    >>> time.mktime(x)
    952421880.0

### How do I turn a timestamp into a datetime object? {#How_do_I_turn_a_timestamp_into_a_datetime_object.3F}

    >>> import time
    >>> import datetime
    >>> d = datetime.datetime.fromtimestamp(time.time())
    >>> d
    datetime.datetime(2007, 11, 2, 10, 25, 35, 947082)

### How long between date/time A and date/time B? {#How_long_between_date.2Ftime_A_and_date.2Ftime_B.3F}

    >>> import time
    >>> import datetime
    >>> atup = (2000, 3, 7, 0, 0, 0, 0, 0, 0)
    >>> btup = (2000, 12, 15, 0, 0, 0, 0, 0, 0)
    >>> diff = time.mktime(btup) - time.mktime(atup)
    >>> diff
    24451200.0
    >>> # or, using datetime....
    >>> a = datetime.datetime.fromtimestamp(time.mktime(atup))
    >>> b = datetime.datetime.fromtimestamp(time.mktime(btup))
    >>> c = b - a
    >>> c
    datetime.timedelta(283)
    >>> print c
    283 days, 0:00:00

### What was the date or timestamp of last Friday? {#What_was_the_date_or_timestamp_of_last_Friday.3F}

    >>> import time
    >>> now = time.time()
    >>> tup = time.localtime()
    >>> then = now - 24*60*60((7 + tup[6] - 4 - 1)%7 + 1)
    >>> # or, using datetime
    >>> import datetime
    >>> today = datetime.datetime.now()
    >>> today
    datetime.datetime(2007, 11, 2, 11, 27, 50, 37655)
    >>> diff = datetime.timedelta((7 + today.weekday() - 4 - 1)%7 + 1, 0, 0)
    >>> last_friday = today - diff
    >>> last_friday
    datetime.datetime(2007, 10, 26, 11, 27, 50, 37655)

In general, to compute the date of last Z,

- today - (7 + weekday - Z - 1) % 7 + 1

To compute the date of next Z,

- today + (7 + Z - weekday - 1) % 7 + 1

This assumes that Monday = 0, Tuesday = 1, \..., Sunday = 6, as is the case in python.

Note that the computation must be carried out in units of days.

### Can I give the datetime module a less cumbersome alias? {#Can_I_give_the_datetime_module_a_less_cumbersome_alias.3F}

    >>> import datetime as dt

## References {#References}

\[1\] \$ pydoc datetime.tzinfo

# Printing to stderr {#Printing_to_stderr}

    print >> sys.stderr, 'entering function'

# glob.glob vs os.listdir {#glob.glob_vs_os.listdir}

glob.glob doesn\'t get . files, os.listdir does

# Run a command and grab its output (or you can write to it) {#Run_a_command_and_grab_its_output_.28or_you_can_write_to_it.29}

     f = os.popen(command, 'r')
     output = f.readlines()

     g = os.popen(command, 'w')
     g.write('foobar')

## output and input {#output_and_input}

(fout, fin) = popen2.popen2(command)

## with stderr {#with_stderr}

(fout_plus_err, fin) = popen2.popen4(command)

# get the current machine\'s hostname {#get_the_current_machine.27s_hostname}

import socket host = socket.gethostname() print host

------------------------------------------------------------------------

[CategoryHomepage](CategoryHomepage)
:::
