#!/usr/bin/env python3

'''
OPS445 Assignment 1
Program: assignment1.py
The python code in this file is original work written by
"Student Name". No code in this file is copied from any other source
except those provided by the course instructor, including any person,
textbook, or on-line resource. I have not shared this python script
with anyone or anything except for submission for grading. I understand
that the Academic Honesty Policy will be enforced and
violators will be reported and appropriate action will be taken.

Author: Zhaofa Zhang
Semester: FALL 2024
Description: student ID: zzhang276
'''

import sys

def day_of_week(date: str) -> str:
    "Based on the algorithm by Tomohiko Sakamoto"
    day, month, year = (int(x) for x in date.split('/'))
    days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    offset = {1: 0, 2: 3, 3: 2, 4: 5, 5: 0, 6: 3, 7: 5, 8: 1, 9: 4, 10: 6, 11: 2, 12: 4}
    if month < 3:
        year -= 1
    num = (year + year // 4 - year // 100 + year // 400 + offset[month] + day) % 7
    return days[num]
'''
This function calculates the day of the week for a given date. It implements Tomohiko Sakamoto's date algorithm, converting the date into the corresponding weekday name
'''
def leap_year(year: int) -> bool:
    "Return True if the year is a leap year"
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    else:
        return year % 4 == 0
'''
This is a placeholder function that determines whether a year is a leap year. 
'''
def mon_max(month: int, year: int) -> int:
    "Returns the maximum day for a given month. Includes leap year check"
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        return 29 if leap_year(year) else 28
    else:
        return -1
'''This function returns the maximum number of days in a specified month. It checks if February falls in a leap year; if it is a leap year, February has 29 days; otherwise, it has 28 days.'''
def after(date: str) -> str:
    '''
    after() -> date for next day in DD/MM/YYYY string format

    Return the date for the next day of the given date in DD/MM/YYYY format.
    This function has been tested to work for year after 1582
    '''
    day, mon, year = (int(x) for x in date.split('/'))
    day += 1  # next day

    mon_max_day = mon_max(mon, year)

    if day > mon_max_day:
        day = 1
        mon += 1
        if mon > 12:
            mon = 1
            year += 1

    return f"{day:02}/{mon:02}/{year}"
'''This function calculates the next day of a given date. First, it increments the day by one. 
If it exceeds the maximum number of days for that month, it rolls over to the next month. If it's December, it rolls over to the next year.'''
def before(date: str) -> str:
    "Returns previous day's date as DD/MM/YYYY"
    day, mon, year = (int(x) for x in date.split('/'))
    day -= 1  # previous day

    if day < 1:
        mon -= 1
        if mon < 1:
            mon = 12
            year -= 1
        day = mon_max(mon, year)

    return f"{day:02}/{mon:02}/{year}"
'''This function calculates the previous day of a given date. It first subtracts one from the day, then checks 
if it's below the first day of the month. If it does, it goes back to the previous month. If it's January, it goes back to the previous year.'''
def usage():
    "Print a usage message to the user"
    print(f"Usage: {sys.argv[0]} DD/MM/YYYY NN")
    sys.exit()
'''
This function checks the input and displays the correct format if there are any errors.'''
def valid_date(date: str) -> bool:
    "Check validity of date"
    try:
        day, mon, year = (int(x) for x in date.split('/'))
        if mon < 1 or mon > 12:
            return False
        if day < 1 or day > mon_max(mon, year):
            return False
        return True
    except ValueError:
        return False
'''
This function checks the date format. It checks if the day and month are reasonable and can be parsed as integers.
'''
def day_iter(start_date: str, num: int) -> str:
    "Iterates from start date by num to return end date in DD/MM/YYYY"
    date = start_date
    if num >= 0:
        for _ in range(num):
            date = after(date)
    else:
        for _ in range(-num):
            date = before(date)
    return date
'''T
his function returns the date after applying a given offset in days to a specified date. If the offset (num) is positive, it calls the after function; if it's negative, it calls the before function.'''
if __name__ == "__main__":
    if len(sys.argv) != 3:
        usage()
        '''Checks the number of arguments.'''
    start_date = sys.argv[1]
    if not valid_date(start_date):
        usage()
        '''Checks the date is valid.'''
    try:
        num_days = int(sys.argv[2])
    except ValueError:
        usage()
        '''Converts the second argument to a number representing the offset in days.'''
    end_date = day_iter(start_date, num_days)
    print(f'The end date is {day_of_week(end_date)}, {end_date}.')
    '''Shows the final date and day of the week.'''
