#!/usr/bin/env python

##
# @file
# @author Wes Dean <wdean@flexion.us>
# @brief calculate and display date / time relative to another date / time
#
# @details
# This tool will accept a date / time and the distance (delta) from the
# provided date / time (days, hours, etc.) and write the result
# of combining the two.
#
#


from datetime import timedelta, datetime
import argparse


# Defaults


# This is the format in which the calculation result will be accepted and
# returned; the format uses the standard "strftime" (e.g., "%Y" for
# 4-digit year).
#
# For more information, see the standard library documentation:
# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
default_format = "%Y-%m-%dT%H:%M:%S"


# Set runtime variables

# Parse the CLI arguments
argparser = argparse.ArgumentParser(
    description="This tool will find the date / time relative to another date / time."
    "To use this tool, provide a date/time (the default is the current date / time) "
    "and the number of weeks, hours, minutes, and seconds from the provided date.  "
    "The tool will then write the resulting date/time to STDOUT."
    ""
    "The relative values (e.g., weeks, days, etc.) may be positive (meaning the resulting "
    "date will be after the provided date) or negative (meaning the resulting date will "
    "be before the provided date."
    ""
    "A date / time format may also be specified with --input-format and --output-format"
)

argparser.add_argument("-w", "--weeks", type=int,
                       help="number of weeks", default=0)
argparser.add_argument("-d", "--days", type=int, help="number of days", default=0)
argparser.add_argument("-H", "--hours", type=int,
                       help="number of hours", default=0)
argparser.add_argument("-m", "--minutes", type=int,
                       help="number of minutes", default=0)
argparser.add_argument("-s", "--seconds", type=int,
                       help="number of seconds", default=0)
argparser.add_argument("-i", "--input-format", type=str,
                       help="date input format string", default=default_format)
argparser.add_argument("-o", "--output-format", type=str,
                       help="date output format string", default=default_format)
argparser.add_argument(
    "date", type=str, help="date /time from which to calculate (defaults to current date / time)", default="", nargs="?")

args = argparser.parse_args()


# Calculate the starting date

# if we get nothing (or "now") then assume the current date / time
if ((args.date == None) or (args.date == "") or (args.date == "now")):
    target_date = datetime.now()
# if we get a string, attempt to parse that string into a datetime object
else:
    target_date = datetime.strptime(args.date, args.input_format)

# timedelta accepts relative values and returns a datetime object based on the
# relative value and the initial date
date_delta = timedelta(weeks=args.weeks, days=args.days,
                       hours=args.hours, minutes=args.minutes, seconds=args.seconds)

# perform the calculation
calculated_date = target_date + date_delta

# write the output to STDOUT in the requested format
print calculated_date.strftime(args.output_format)
