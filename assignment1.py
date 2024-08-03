#!/usr/bin/env python3
#Author name : amir iravani

import sys
from datetime import datetime, timedelta

def after(date_str):
    """
    Given a date string in the format 'YYYY-MM-DD' or 'dd/mm/yyyy', returns the date of the next day.

    Parameters:
    - date_str (str): Date in 'YYYY-MM-DD' or 'dd/mm/yyyy' format.

    Returns:
    - str: Date of the next day in the same format as the input.
    """
    formats = ['%Y-%m-%d', '%d/%m/%Y']
    for fmt in formats:
        try:
            date_obj = datetime.strptime(date_str, fmt)
            next_day = date_obj + timedelta(days=1)
            return next_day.strftime(fmt)
        except ValueError:
            continue
    raise ValueError("Date format is incorrect")

def leap_year(year):
    """
    Determines if a given year is a leap year.

    Parameters:
    - year (int): Year to check.

    Returns:
    - bool: True if the year is a leap year, False otherwise.
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def mon_max(month, year):
    """
    Returns the maximum number of days in a given month and year.

    Parameters:
    - month (int): Month (1 to 12).
    - year (int): Year.

    Returns:
    - int: Maximum number of days in the specified month.
    """
    if month == 2:
        return 29 if leap_year(year) else 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31

def valid_date(date_str):
    """
    Checks if the provided date string is a valid date.

    Parameters:
    - date_str (str): Date in 'YYYY-MM-DD' or 'dd/mm/yyyy' format.

    Returns:
    - bool: True if the date is valid, False otherwise.
    """
    formats = ['%Y-%m-%d', '%d/%m/%Y']
    for fmt in formats:
        try:
            datetime.strptime(date_str, fmt)
            return True
        except ValueError:
            continue
    return False

def day_iter(date_str, num):
    """
    Adds a specified number of days to a given date and returns the new date.

    Parameters:
    - date_str (str): Date in 'YYYY-MM-DD' format.
    - num (int): Number of days to add (can be positive or negative).

    Returns:
    - str: New date in 'YYYY-MM-DD' format.
    """
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    new_date = date_obj + timedelta(days=num)
    return new_date.strftime('%Y-%m-%d')

def count_weekends(start_date_str, end_date_str):
    """
    Counts the number of weekend days between two dates.

    Parameters:
    - start_date_str (str): Start date in 'YYYY-MM-DD' format.
    - end_date_str (str): End date in 'YYYY-MM-DD' format.

    Returns:
    - int: Number of weekend days between the two dates.
    """
    start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
    end_date = datetime.strptime(end_date_str, '%Y-%m-%d')
    count = 0
    current_date = start_date

    while current_date <= end_date:
        if current_date.weekday() >= 5:  # 5 for Saturday, 6 for Sunday
            count += 1
        current_date += timedelta(days=1)

    return count

def usage():
    """
    Prints the usage message and exits the script.
    """
    print("Usage: assignment1.py <start_date: yyyy-mm-dd> <end_date: yyyy-mm-dd>")
    sys.exit(1)

# Main script logic
if __name__ == "__main__":
    if len(sys.argv) != 3:
        usage()

    start_date_str, end_date_str = sys.argv[1], sys.argv[2]

    if not (valid_date(start_date_str) and valid_date(end_date_str)):
        usage()

    start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
    end_date = datetime.strptime(end_date_str, '%Y-%m-%d')

    if start_date > end_date:
        print(f"The end date is {end_date.strftime('%a, %d/%m/%Y')}.")
    else:
        num_weekends = count_weekends(start_date_str, end_date_str)
        print(f"The period between {start_date_str} and {end_date_str} includes {num_weekends} weekend days.")
