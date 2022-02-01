# Empty unit-testing class
# Peter Brown, 26 Jan 2017

import unittest
from validdate import * # import the module to test

class TestValidDate(unittest.TestCase):
    def test_dateStr(self) -> None:
        self.assertTrue(isValidDateString('2/1/2022'))

    def test_dateStrTooLong(self) -> None:
        self.assertFalse(isValidDateString('2/1/2022/5'))

    def test_dateStrTooShort(self) -> None:
        self.assertFalse(isValidDateString('2/1'))

    def test_dateStrEmptyMonth(self) -> None:
        self.assertFalse(isValidDateString('/1/2022'))
    
    def test_dateStrEmptyDay(self) -> None:
        self.assertFalse(isValidDateString('2//2022'))

    def test_dateStrEmptyYear(self) -> None:
        self.assertFalse(isValidDateString('2/1/'))

    def test_dateStrNonDigitMonth(self) -> None:
        self.assertFalse(isValidDateString('-1/1/2022'))

    def test_dateStrNonDigitDay(self) -> None:
        self.assertFalse(isValidDateString('2/q/2022'))

    def test_dateStrNonDigitYear(self) -> None:
        self.assertFalse(isValidDateString('2/1/20.22'))

    def test_dateOK(self) -> None:
        self.assertTrue(isDate(2, 1, 2022))

    def test_dateZeroMonth(self) -> None:
        self.assertFalse(isDate(0, 1, 2022))

    def test_dateMonth13(self) -> None:
        self.assertFalse(isDate(13, 1, 2022))

    def test_dateMinMonth(self) -> None:
        self.assertTrue(isDate(1, 1, 2022))

    def test_dateMaxMonth(self) -> None:
        self.assertTrue(isDate(12, 1, 2022))

    # Gregorian calendar wasn't promulgated until 1582.
    # Insisting on the date of promulgation as the beginning
    # of the calendar allows me to avoid dealing with
    # two-digit years.
    def test_dateYearTooSmall(self) -> None:
        self.assertFalse(isDate(2, 1, 1581))

    # The Gregorian calendar has no endpoint, so there's no
    # year too large.
    
    # Every month starts with the first of the month.
    def test_dateDayTooSmall(self) -> None:
        self.assertFalse(isDate(2, 0, 2022))

    # 31-day months

    def test_dateDayTooBig31(self) -> None:
        self.assertFalse(isDate(1, 32, 2022))

    def test_dateMaxDay31(self) -> None:
        self.assertTrue(isDate(1, 31, 2022))

    # 30-day months

    def test_dateDayTooBig30(self) -> None:
        self.assertFalse(isDate(9, 31, 2022))

    def test_dateMaxDay30(self) -> None:
        self.assertTrue(isDate(9, 30, 2022))

    # February in a non-leap year

    def test_dateDayTooBigFebNormal(self) -> None:
        self.assertFalse(isDate(2, 29, 2022))

    def test_dateMaxDayFebNormal(self) -> None:
        self.assertTrue(isDate(2, 28, 2022))

    # February in a leap year

    def test_dateDayTooBigFebLeap(self) -> None:
        self.assertFalse(isDate(2, 30, 2020))

    def test_dateMaxDayFebLeap(self) -> None:
        self.assertTrue(isDate(2, 29, 2020))

if __name__ == '__main__':
    unittest.main()