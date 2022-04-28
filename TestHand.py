# Empty unit-testing class
# Peter Brown, 26 Jan 2017

import unittest
from typing import List
# import the module to test
from AbstractCard import AbstractCard
from Hand import Hand
from PlayingCard import PlayingCard

class TestHand(unittest.TestCase):

    def setUp(self) -> None:
        """Function to be run before each test, to set up."""
        self._emptyHand: Hand = Hand()

        self._hand5: Hand = Hand()
        cards: List[AbstractCard] = PlayingCard.makeDeck()
        self._hand5.addMany(cards[10:0:-2])

    def test_len_empty(self) -> None:
        self.assertEqual(len(self._emptyHand), 0)

    def test_len_nonempty(self) -> None:
        self.assertEqual(len(self._hand5), 5)

    def test_add_one_mid(self) -> None:
        self._hand5.addCard(PlayingCard('2', 'diamonds'))
        self.assertEqual(len(self._hand5), 6)

    def test_add_one_bottom(self) -> None:
        self._hand5.addCard(PlayingCard('Ace', 'clubs'))
        self.assertEqual(len(self._hand5), 6)

    def test_add_one_top(self) -> None:
        self._hand5.addCard(PlayingCard('Jack', 'diamonds'))
        self.assertEqual(len(self._hand5), 6)

    def test_play_nonempty(self) -> None:
        c: AbstractCard = self._hand5.play(PlayingCard('2', 'hearts'))
        self.assertEqual(c.rank(), 2)
        self.assertEqual(c.suit(), 'hearts')
        self.assertEqual(len(self._hand5), 4)
        self.assertTrue(c not in self._hand5._cards)
 
    def test_play_empty(self) -> None:
        with self.assertRaises(IndexError):
            self._emptyHand.play(PlayingCard('2', 'hearts'))

if __name__ == '__main__':
    unittest.main()