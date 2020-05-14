# Checks if a date is valid
# WIP

import re
from datetime import datetime


def validate_date(date):
    check_date = re.compile(r"(\d\d)/([0-1]\d)/([1-2]\d\d\d)")  # detect DD/MM/YYYY format
    day = int(check_date.search(date).group(1))  # set variables
    month = int(check_date.search(date).group(2))
    year = int(check_date.search(date).group(3))

    if month == 4 and day == 31:
        return "False: too many days in the month!"
    if month == 6 and day == 31:
        return "False: too many days in the month!"
    if month == 9 and day == 31:
        return "False: too many days in the month!"
    if month == 11 and day == 31:
        return "False: too many days in the month!"

    if month == 2:
        if day > 28 and year % 4 != 0:  # the year is not leap year
            return "False, february can't have more than 29 days in non-leap years!"
        elif day > 28 and year % 4 == 0 and year % 100 == 0:
            return "False: february can't have more than 28 days in leap years divisible by 100"
        elif day > 29 and year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
            return "False: february can't have more than 29 days in leap years divisible by 100 and 400"
        elif day > 29 and year % 4 == 0:  # it is leap year
            return "False, february can't have more than 29 days in leap years!"

    return True


# tests
print(validate_date('21/06/2061'))  # True
print(validate_date('31/11/2019'))  # false, no 31st of november

print(validate_date('29/02/2004'))  # True, february can have 29 days in leap years
print(validate_date('29/02/2100'))  # False, february can't have more than 28 days in leap years divisible by 100
print(validate_date('29/02/2000'))  # True, february can have 29 days in leap years divisible by 100 and 400

print("""
superior version:""")


def validate(date_text):
    try:
        if date_text != datetime.strptime(date_text, "%Y-%m-%d").strftime('%Y-%m-%d'):
            raise ValueError
        return True
    except ValueError:
        return False


print(validate('2061-06-21'))
print(validate('2019-11-31'))
print(validate('2004-02-29'))
print(validate('2100-02-29'))
print(validate('2000-02-29'))
