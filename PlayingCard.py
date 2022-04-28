# Class to represent a common playing card.

from typing import List, Tuple
from AbstractCard import AbstractCard

class PlayingCard(AbstractCard):
    """Class to represent a playing card (the usual kind).
    A PlayingCard is immutable, and is defined in terms
    of its rank and suit.  This class ignores jokers."""

    _SUITS: Tuple[str,...] = ('clubs', 'diamonds', 'hearts', 'spades')

    # Rank names.  Assume aces are low.
    _RANK_NAMES: Tuple[str, ...] = ('', 'Ace', '2', '3', '4', '5', '6', '7',
            '8', '9', '10', 'Jack', 'Queen', 'King')
    _BOTTOM_RANK: int = 1 # Assumes aces are low
    _TOP_RANK: int = len(_RANK_NAMES) - 1 # Assumes aces low

    def __init__(self, rank: str, suit: str):
        """Construct a PlayingCard from a rank and a suit."""
        # Pre:
        assert rank.capitalize() in self._RANK_NAMES and \
            suit.lower() in self._SUITS
        super().__init__(rank.capitalize(), suit.lower())

    def __str__(self) -> str:
        # Pre:
        assert self._invariant()
        return self._RANK_NAMES[self._rank] + ' of ' + self._suit
        # Post: return value is rank ' of ' suit

    @staticmethod
    def makeDeck() -> List[AbstractCard]:
        """Make a deck of PlayingCards."""
        deck: List[AbstractCard] = []
        for rank in PlayingCard._RANK_NAMES[1:]:
            for suit in PlayingCard._SUITS:
                deck.append(PlayingCard(rank, suit))
        return deck