from typing import cast, List, Sequence
from AbstractCard import AbstractCard

class Hand:
    """Class to represent a hand of playing cards.
    The cards in the Hand are kept sorted in
    non-decreasing order."""

    def _invariant(self) -> bool: # O(n)
        """Class invariant."""
        valid: bool = True
        for i in range(len(self._cards) - 1):
            if self._cards[i] > self._cards[i+1]:
                valid = False
        return valid

    def __init__(self): # O(1)
        """Construct an empty Hand."""
        self._cards: List[AbstractCard] = []
        # Post:
        assert self._invariant()

    def __len__(self) -> int: # O(1)
        """Return the size of the hand."""
        return len(self._cards)
        # Post: the return value is the length of self._cards

    def addMany(self, more: Sequence[AbstractCard]) -> None: O(n * len(more))
        """Add the cards in MORE to the hand.  MORE does not need
        to be sorted."""
        for c in more: # O(len(more))
            self.addCard(c) # O(n)
        # Post
        assert self._invariant()
        # and len(self) == len(more) plus previous len(self)

    def addCard(self, card: AbstractCard) -> None: # O(n)
        """Add a given AbstractCard to the Hand,
        keeping Hand sorted."""
        i = 0
        # Find the correct place for the given card
        while i < len(self._cards) and self._cards[i] < card: # O(n)
            i = i + 1
        self._cards.insert(i, card) # O(n)
        # Post:
        assert self._invariant() and card in self._cards
        # and len(self) == old len(self) + 1
    
    def play(self, card: AbstractCard) -> AbstractCard: # O(n)
        """Play a given CARD, removing it from the Hand."""
        i: int = 0
        result: AbstractCard = None
        while i < len(self._cards) and self._cards[i] < card: # O(n)
            i = i + 1
        if (i < len(self._cards)) and self._cards[i] == card:
            result = self._cards.pop(i) # O(n)
        else:
            raise IndexError('Requested card could not be found')
        return result

    