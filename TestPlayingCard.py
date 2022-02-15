# Empty unit-testing class
# Peter Brown, 26 Jan 2017

import unittest
from PlayingCard import PlayingCard

class TestPlayingCard(unittest.TestCase):
    def test_create_ace_of_spades(self) -> None:
        self.assertEqual(str(PlayingCard('ace', 'Spades')), 'Ace of spades')
        
    def test_create_all(self) -> None:
        for rank in PlayingCard._RANK_NAMES[1:]:
            with self.subTest(r=rank):
                for suit in PlayingCard._SUITS:
                    with self.subTest(s=suit):
                        self.assertEqual(str(PlayingCard(rank, suit)),
                             rank + ' of ' + suit)

    def test_invalid_rank(self) -> None:
        with self.assertRaises(AssertionError):
            PlayingCard('', 'hearts')

    def test_invalid_suit(self) -> None:
        with self.assertRaises(AssertionError):
            PlayingCard('3', 'kidneys')


if __name__ == '__main__':
    unittest.main()