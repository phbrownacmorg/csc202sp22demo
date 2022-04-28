# Test leapyear.py

import unittest
from leapyear import *  # import the module to test

class TestLeapYear(unittest.TestCase):

    ## Test Julian rule: all the values of year % 4

    # year % 4 == 2
    def test_2022(self) -> None:
        # assertEqual is the most common test
        self.assertEqual(isLeapYear(2022), False) 

    # year % 4 == 1
    def test_2021(self) -> None:
        # assertFalse is a useful test for Booleans
        self.assertFalse(isLeapYear(2021))        #

    # year % 4 == 3
    def test_2023(self) -> None:
        # assertFalse is a useful test for Booleans
        self.assertFalse(isLeapYear(2023))

    # year % 4 == 0
    def test_2024(self) -> None:
        # assertTrue is also a useful test for Booleans
        self.assertTrue(isLeapYear(2024))

    ## Test Gregorian extensions: century years

    # year % 400 == 0
    def test_2000(self) -> None:
        self.assertTrue(isLeapYear(2000))

    # year % 400 == 300
    def test_1900(self) -> None:
        self.assertFalse(isLeapYear(1900))

    # year % 400 == 200
    def test_1800(self) -> None:
        self.assertFalse(isLeapYear(1800))

    # year % 400 == 100
    def test_2100(self) -> None:
        self.assertFalse(isLeapYear(2100))


if __name__ == '__main__':
    unittest.main()