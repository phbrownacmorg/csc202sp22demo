# Empty unit-testing class
# Peter Brown, 26 Jan 2017

import unittest
from typing import List
from AbstractCard import AbstractCard
from PlayingCard import PlayingCard
from UnoCard import UnoCard

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

    def testEQ(self) -> None:
        for rank1 in PlayingCard._RANK_NAMES[1:]:
            with self.subTest(r1=rank1):
                for suit1 in PlayingCard._SUITS:
                    with self.subTest(s1=suit1):
                        card1: PlayingCard = PlayingCard(rank1, suit1)

                        for rank2 in PlayingCard._RANK_NAMES[1:]:
                            with self.subTest(r2=rank2):
                                for suit2 in PlayingCard._SUITS:
                                    with self.subTest(s2=suit2):
                                        card2 = PlayingCard(rank2, suit2)

                                        if rank1 == rank2 and suit1 == suit2:
                                            self.assertTrue(card1 == card2)
                                        else:
                                            self.assertFalse(card1 == card2)
        # Verify the exceptions
        with self.assertRaises(NotImplementedError):
            PlayingCard('5', 'spades') == 5
        with self.assertRaises(NotImplementedError):
            PlayingCard('5', 'diamonds') == UnoCard('5', 'red')

    def testNE(self) -> None:
        for rank1 in PlayingCard._RANK_NAMES[1:]:
            with self.subTest(r1=rank1):
                for suit1 in PlayingCard._SUITS:
                    with self.subTest(s1=suit1):
                        card1: PlayingCard = PlayingCard(rank1, suit1)

                        for rank2 in PlayingCard._RANK_NAMES[1:]:
                            with self.subTest(r2=rank2):
                                for suit2 in PlayingCard._SUITS:
                                    with self.subTest(s2=suit2):
                                        card2 = PlayingCard(rank2, suit2)

                                        if rank1 == rank2 and suit1 == suit2:
                                            self.assertFalse(card1 != card2)
                                        else:
                                            self.assertTrue(card1 != card2)
        # Verify the exceptions
        with self.assertRaises(NotImplementedError):
            PlayingCard('5', 'spades') != 5
        with self.assertRaises(NotImplementedError):
            PlayingCard('5', 'diamonds') != UnoCard('5', 'red')

    def testLT(self) -> None:
        for rank_i in range(1, len(PlayingCard._RANK_NAMES)):
            rank1: str = PlayingCard._RANK_NAMES[rank_i]
            with self.subTest(r1 = rank1):
                for suit1 in PlayingCard._SUITS:
                    with self.subTest(s1=suit1):
                        card1: PlayingCard = PlayingCard(rank1, suit1)

                        for rank_j in range(1, len(PlayingCard._RANK_NAMES)):
                            rank2: str = PlayingCard._RANK_NAMES[rank_j]
                            with self.subTest(r2=rank2):
                                for suit2 in PlayingCard._SUITS:
                                    with self.subTest(s2=suit2):
                                        card2: PlayingCard = PlayingCard(rank2, suit2)

                                        if (rank_i < rank_j):
                                            self.assertTrue(card1 < card2)
                                        elif (rank_j < rank_i):
                                            self.assertFalse(card1 < card2)
                                        elif (suit1 < suit2):
                                            self.assertTrue(card1 < card2)
                                        else:
                                            self.assertFalse(card1 < card2)
        # Verify the exceptions
        with self.assertRaises(NotImplementedError):
            PlayingCard('5', 'spades') < 5
        with self.assertRaises(NotImplementedError):
            PlayingCard('5', 'diamonds') < UnoCard('5', 'red')

    def testLE(self) -> None:
        for rank_i in range(1, len(PlayingCard._RANK_NAMES)):
            rank1: str = PlayingCard._RANK_NAMES[rank_i]
            with self.subTest(r1 = rank1):
                for suit1 in PlayingCard._SUITS:
                    with self.subTest(s1=suit1):
                        card1: PlayingCard = PlayingCard(rank1, suit1)

                        for rank_j in range(1, len(PlayingCard._RANK_NAMES)):
                            rank2: str = PlayingCard._RANK_NAMES[rank_j]
                            with self.subTest(r2=rank2):
                                for suit2 in PlayingCard._SUITS:
                                    with self.subTest(s2=suit2):
                                        card2: PlayingCard = PlayingCard(rank2, suit2)

                                        if (rank_i < rank_j):
                                            self.assertTrue(card1 <= card2)
                                        elif (rank_j < rank_i):
                                            self.assertFalse(card1 <= card2)
                                        elif (suit1 <= suit2):
                                            self.assertTrue(card1 <= card2)
                                        else:
                                            self.assertFalse(card1 <= card2)
        # Verify the exceptions
        with self.assertRaises(NotImplementedError):
            PlayingCard('5', 'spades') <= 5
        with self.assertRaises(NotImplementedError):
            PlayingCard('5', 'diamonds') <= UnoCard('5', 'red')

    def testGE(self) -> None:
        for rank_i in range(1, len(PlayingCard._RANK_NAMES)):
            rank1: str = PlayingCard._RANK_NAMES[rank_i]
            with self.subTest(r1 = rank1):
                for suit1 in PlayingCard._SUITS:
                    with self.subTest(s1=suit1):
                        card1: PlayingCard = PlayingCard(rank1, suit1)

                        for rank_j in range(1, len(PlayingCard._RANK_NAMES)):
                            rank2: str = PlayingCard._RANK_NAMES[rank_j]
                            with self.subTest(r2=rank2):
                                for suit2 in PlayingCard._SUITS:
                                    with self.subTest(s2=suit2):
                                        card2: PlayingCard = PlayingCard(rank2, suit2)

                                        if (rank_i < rank_j):
                                            self.assertFalse(card1 >= card2)
                                        elif (rank_j < rank_i):
                                            self.assertTrue(card1 >= card2)
                                        elif (suit1 < suit2):
                                            self.assertFalse(card1 >= card2)
                                        else:
                                            self.assertTrue(card1 >= card2)
        # Verify the exceptions
        with self.assertRaises(NotImplementedError):
            PlayingCard('5', 'spades') >= 5
        with self.assertRaises(NotImplementedError):
            PlayingCard('5', 'diamonds') >= UnoCard('5', 'red')

    def testGT(self) -> None:
        for rank_i in range(1, len(PlayingCard._RANK_NAMES)):
            rank1: str = PlayingCard._RANK_NAMES[rank_i]
            with self.subTest(r1 = rank1):
                for suit1 in PlayingCard._SUITS:
                    with self.subTest(s1=suit1):
                        card1: PlayingCard = PlayingCard(rank1, suit1)

                        for rank_j in range(1, len(PlayingCard._RANK_NAMES)):
                            rank2: str = PlayingCard._RANK_NAMES[rank_j]
                            with self.subTest(r2=rank2):
                                for suit2 in PlayingCard._SUITS:
                                    with self.subTest(s2=suit2):
                                        card2: PlayingCard = PlayingCard(rank2, suit2)

                                        if (rank_i < rank_j):
                                            self.assertFalse(card1 > card2)
                                        elif (rank_j < rank_i):
                                            self.assertTrue(card1 > card2)
                                        elif (suit1 <= suit2):
                                            self.assertFalse(card1 > card2)
                                        else:
                                            self.assertTrue(card1 > card2)
        # Verify the exceptions
        with self.assertRaises(NotImplementedError):
            PlayingCard('5', 'spades') > 5
        with self.assertRaises(NotImplementedError):
            PlayingCard('5', 'diamonds') > UnoCard('5', 'red')

    def testMakeDeck(self) -> None:
        deck: List[AbstractCard] = PlayingCard.makeDeck()
        self.assertEqual(len(deck), 52)
        for i in range(52):
            self.assertEqual(deck[i].suit(), PlayingCard._SUITS[i % 4])
            self.assertEqual(deck[i].rank(), (i // 4) + 1)


if __name__ == '__main__':
    unittest.main()