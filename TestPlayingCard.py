# Empty unit-testing class
# Peter Brown, 26 Jan 2017

import unittest
from typing import List
from AbstractCard import AbstractCard
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

    def testSuit(self) -> None:
        for rank in PlayingCard._RANK_NAMES[1:]:
            with self.subTest(r=rank):
                for suit in PlayingCard._SUITS:
                    with self.subTest(s=suit):
                        self.assertEqual(PlayingCard(rank, suit).suit(), suit)

    def testRank(self) -> None:
        for rank in PlayingCard._RANK_NAMES[1:]:
            with self.subTest(r=rank):
                for suit in PlayingCard._SUITS:
                    with self.subTest(s=suit):
                        self.assertEqual(PlayingCard(rank, suit).rank(), 
                                        PlayingCard._RANK_NAMES.index(rank))

    def testRankName(self) -> None:
        for rank in PlayingCard._RANK_NAMES[1:]:
            with self.subTest(r=rank):
                for suit in PlayingCard._SUITS:
                    with self.subTest(s=suit):
                        self.assertEqual(PlayingCard(rank, suit).rankName(), 
                                            rank)

    def testMakeDeck(self) -> None:
        deck: List[AbstractCard] = PlayingCard.makeDeck()
        self.assertEqual(len(deck), 52)
        for i in range(52):
            self.assertEqual(deck[i].suit(), PlayingCard._SUITS[i % 4])
            self.assertEqual(deck[i].rank(), (i // 4) + 1)


if __name__ == '__main__':
    unittest.main()