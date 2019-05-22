# datetime_from_now
This is a quick Python script to accept a datetime, apply a delta, and display the result

## Installation
This script only imports from datetime which is a part of the Python Standard Library; therefore, no extra modules are required.
Similarly, the entire program is self-contained in a single file; it can be copied anywhere where Python is installed and run there.

## Usage
The following is the result of using the `--help` flag:
```
usage: from_now.py [-h] [-w WEEKS] [-d DAYS] [-H HOURS] [-m MINUTES]
                   [-s SECONDS] [-i INPUT_FORMAT] [-o OUTPUT_FORMAT] [-u]
                   [date]

This tool will find the date / time relative to another date / time.To use
this tool, provide a date/time (the default is the current date / time) and
the number of weeks, hours, minutes, and seconds from the provided date. The
tool will then write the resulting date/time to STDOUT.The relative values
(e.g., weeks, days, etc.) may be positive (meaning the resulting date will be
after the provided date) or negative (meaning the resulting date will be
before the provided date.A date / time format may also be specified with
--input-format and --output-format and defaults to ISO-8601

positional arguments:
  date                  date /time from which to calculate (defaults to
                        current date / time)

optional arguments:
  -h, --help            show this help message and exit
  -w WEEKS, --weeks WEEKS
                        number of weeks
  -d DAYS, --days DAYS  number of days
  -H HOURS, --hours HOURS
                        number of hours
  -m MINUTES, --minutes MINUTES
                        number of minutes
  -s SECONDS, --seconds SECONDS
                        number of seconds
  -i INPUT_FORMAT, --input-format INPUT_FORMAT
                        date input format string
  -o OUTPUT_FORMAT, --output-format OUTPUT_FORMAT
                        date output format string
  -u, --utc             set to use UTC; otherwise, use local timezone
```

## Default format
The default time format is ISO-8601; this corresponds to the Python datetime format string of:
`%Y-%m-%dT%%H%M%S.%fZ`

## Examples
```shell
from_now.py --utc --days 7
```

Result: `2019-05-27T23:14:27.522175Z`

This will return the date / time exactly seven days from right now.

```shell
from_now.py --hours -1 --input-format "%Y%m%d"
```

Result: `20190520`

This will return the date / time exactly one hour ago.


