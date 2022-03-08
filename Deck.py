import random
from typing import List
from AbstractCard import AbstractCard


class Deck:
    """Class to represent a deck of cards."""

    def _invariant(self) -> bool: # O(n)
        """Class invariant."""
        valid: bool = True
        for c in self._cards: # type: AbstractCard
            if not isinstance(c, AbstractCard):
                valid = False
        return valid

    def __init__(self): # O(1)
        """Construct an empty deck of cards."""
        self._cards: List[AbstractCard] = []
        # Post:
        assert self._invariant()

    def __len__(self) -> int: # O(1)
        """Return the size of the deck."""
        return len(self._cards)
        # Post: the return value is the length of self._cards

    def add(self, more: List[AbstractCard]) -> None: # O(len(more))
        # Pre: the added cards are actually AbstractCards
        self._cards.extend(more[:])
        # Post:
        assert self._invariant() and (len(self) >= len(more))

    def deal(self) -> AbstractCard: # O(1)
        """Remove and return the top card from the deck."""
        if len(self._cards) == 0:
            raise IndexError('Tried to deal from an empty deck.')
        return self._cards.pop()
        # Post: self._invariant and len(self._cards) is one less

    def dealRandom(self) -> AbstractCard:
        """Deal a card from a random location in the Deck."""
        

    def shuffle(self) -> None: # O(n)
        """Shuffle the deck."""
        # Pre: class invariant
        # Go through the deck, swapping each card with a
        #   randomly-chosen card from somewhere else in the deck.
        for i in range(len(self._cards)): # O(n)
            r: int = random.randint(0, len(self._cards) - 1) # O(1)
            self._cards[i], self._cards[r] = self._cards[r], self._cards[i] # O(1)
        # Post: deck is shuffled