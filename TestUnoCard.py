# Empty unit-testing class
# Peter Brown, 26 Jan 2017

import unittest
from AbstractCard import AbstractCard
from UnoCard import UnoCard

class TestUnoCard(unittest.TestCase):
    # All methods whose names start with "test"
    # will be treated as tests
    def test_create_green_5(self) -> None:
        self.assertEqual(str(UnoCard('5', 'Green')), 'green 5')

    def test_create_all_color(self) -> None:
        for rank in UnoCard._COLOR_RANKS:
            with self.subTest(r=rank):
                for suit in UnoCard._COLOR_SUITS:
                    with self.subTest(s=suit):
                        self.assertEqual(str(UnoCard(rank, suit)),
                             suit + ' ' + rank)

    def test_create_all_wild(self) -> None:
        self.assertEqual(str(UnoCard('', 'wild')), 'wild')
        self.assertEqual(str(UnoCard('draw 4', 'wild')), 'wild draw 4')

    def test_invalid_rank(self) -> None:
        with self.assertRaises(AssertionError):
            UnoCard('', 'red')

    def test_invalid_suit(self) -> None:
        with self.assertRaises(AssertionError):
            UnoCard('3', 'kidneys')


if __name__ == '__main__':
    unittest.main()