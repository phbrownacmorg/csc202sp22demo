from typing import List

def isLeapYear(year:int) -> bool:
    # Pre: (it has to be a year in the Gregorian calendar)
    assert year > 1581
    # Return a Boolean value telling whether the given YEAR is a leap year.
    leap:bool = ((year % 4) == 0) # Julian rule
    # Gregorian adjustment
    if ((year % 100) == 0) and ((year % 400) != 0):
        leap = False
    # Post:
    assert leap == ((year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)))
    return leap

def main(args:List[str]) -> int:
    # Get a year from the user
    year:int = int(input('Please enter a 4-digit year: '))

    print(year, 'is', end=' ')
    if not isLeapYear(year):
        print('NOT', end=' ')
    print('a leap year.')

    # Conventional return value indicating successful completion
    return 0

if __name__ == '__main__':
    import sys
    main(sys.argv)