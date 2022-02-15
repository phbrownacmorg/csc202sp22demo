# Class to represent a common playing card.

from typing import Tuple

class PlayingCard:
    """Class to represent a playing card (the usual kind).
    A PlayingCard is immutable, and is defined in terms
    of its rank and suit.  This class ignores jokers."""

    _SUITS: Tuple[str,...] = ('clubs', 'diamonds', 'hearts', 'spades')

    # Rank names.  Assume aces are low.
    _RANK_NAMES: Tuple[str, ...] = ('', 'Ace', '2', '3', '4', '5', '6', '7',
            '8', '9', '10', 'Jack', 'Queen', 'King')
    _BOTTOM_RANK: int = 1 # Assumes aces are low
    _TOP_RANK: int = len(_RANK_NAMES) - 1 # Assumes aces low

    def _invariant(self) -> bool:
        """Class invariant."""
        return (self._suit in self._SUITS and 
            self._BOTTOM_RANK <= self._rank <= self._TOP_RANK)

    def __init__(self, rank: str, suit: str):
        """Construct a PlayingCard from a rank and a suit."""
        # Pre:
        assert rank.capitalize() in self._RANK_NAMES and \
            suit.lower() in self._SUITS
        self._suit: str = suit.lower()
        self._rank: int = self._RANK_NAMES.index(rank.capitalize())
        # Post:
        assert self._invariant()

    def __str__(self) -> str:
        # Pre:
        assert self._invariant()
        return self._RANK_NAMES[self._rank] + ' of ' + self._suit
        # Post: return value is rank ' of ' suit    