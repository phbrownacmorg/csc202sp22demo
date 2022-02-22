# Empty unit-testing class
# Peter Brown, 26 Jan 2017

import random
import unittest
from typing import List
# import the module to test
from AbstractCard import AbstractCard
from Deck import Deck
from PlayingCard import PlayingCard
from UnoCard import UnoCard

class TestDeck(unittest.TestCase):

    def setUp(self) -> None:
        """Function to be run before each test, to set up."""
        self._emptyDeck: Deck = Deck()

        self._deck52: Deck = Deck()
        self._deck52.add(PlayingCard.makeDeck())
        self._reference = self._deck52._cards[:]

        self._comboDeck = Deck()
        self._comboDeck.add(PlayingCard.makeDeck())
        self._comboDeck.add(UnoCard.makeSomeColorCards())

    def test_len_empty(self) -> None:
        self.assertEqual(len(self._emptyDeck), 0)

    def test_len_nonempty(self) -> None:
        self.assertEqual(len(self._deck52), 52)

    def test_add(self) -> None:
        self.assertEqual(len(self._comboDeck), 104)

    def test_polymorphism(self) -> None:
        """Demonstrate (not really test) polymorphism."""
        for c in self._comboDeck._cards:
            print(str(c))

    def test_deal_nonempty(self) -> None:
        c: AbstractCard = self._deck52.deal()
        self.assertEqual(str(c), 'King of spades') # We got the top card
        self.assertEqual(len(self._deck52), 51) # The deck shrank by 1

    def test_deal_empty(self) -> None:
        with self.assertRaises(IndexError) as cm:
            c: AbstractCard = self._emptyDeck.deal()
        err: IndexError = cm.exception
        self.assertEqual(err.args[0], 
            'Tried to deal from an empty deck.')

    def test_deal_complete(self) -> None:
        """Test deal by dealing *all* 52 cards from self._deck52."""
        for i in range(51, -1, -1):
            with self.subTest(i=i):
                c: AbstractCard = self._deck52.deal()
                # Did the length shrink by 1?
                self.assertEqual(len(self._deck52), i)
                # Did we get the right card?
                self.assertEqual(str(c), str(self._reference[i]))
    
    def testShuffle(self) -> None:
        # Make the test repeatable
        random.seed(4935)
        self._deck52.shuffle()
        # All the cards are still there
        self.assertEqual(len(self._deck52), 52)
        # No card is in its original position
        #    This is a probabilistic statement, which is why we fix the seed.
        for i in range(51, -1, -1):
            with self.subTest(i=i):
                self.assertNotEqual(str(self._deck52.deal()),
                                    str(self._reference[i]))



if __name__ == '__main__':
    unittest.main()