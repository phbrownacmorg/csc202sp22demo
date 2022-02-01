# Read a date in m/d/yyyy form from the terminal, and determine
# whether or not the date is a valid date on the Gregorian calendar.

from typing import List
from leapyear import isLeapYear

def isValidDay(month:int, day:int, year:int) -> bool:
    valid:bool = (day >= 1) and (day <= 31)

    if month in (9, 4, 6, 11) and (day > 30):
        valid = False
    elif (month == 2) and (day > 29):
        valid = False
    elif (month == 2) and (not isLeapYear(year)) and (day > 28):
        valid = False

    return valid

def isDate(month:int, day:int, year:int) -> bool:
    valid:bool = (1 <= month <= 12)

    valid = valid and (year >= 1582)
    valid = valid and (day > 0)
    valid = valid and isValidDay(month, day, year)

    return valid

def isValidDateString(dateStr:str) -> bool:
    """Takes a date string DATESTR and returns a Boolean that is
    True iff DATESTR represents a valid date in m/d/yyyy format."""
    result:bool = True

    # Parse the string into its components
    parts:List[str] = dateStr.split('/')
    if len(parts) != 3:
        result = False
    elif not (parts[0].isdigit() and parts[1].isdigit() and parts[2].isdigit()):
        result = False
    else:
        month:int = int(parts[0])
        day:int = int(parts[1])
        year:int = int(parts[2])
        result = isDate(month, day, year)

    return result


def main(args:List[str]) -> int:
    dateString:str = input('Please enter a date in m/d/yyyy format: ')
    print('The string "{0}" does'.format(dateString), end=' ')

    if not isValidDateString(dateString):
        print('NOT', end=' ')

    print('represent a valid date.')
    # Conventional return value indicating successful completion
    return 0

if __name__ == '__main__':
    import sys
    main(sys.argv)