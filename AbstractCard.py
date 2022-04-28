import abc
from typing import Any, List, Tuple

# Subclasses must have @total_ordering
class AbstractCard(abc.ABC):
    """Abstract base class for playing cards that have 
    a rank, suit structure."""

    # Placeholder class constants
    _SUITS: Tuple[str,...] = ()
    _RANK_NAMES: Tuple[str, ...] = ()
    _BOTTOM_RANK: int = 0
    _TOP_RANK: int = 0

    def _invariant(self) -> bool:
        """Class invariant."""
        return (self._suit in self._SUITS and 
            self._BOTTOM_RANK <= self._rank <= self._TOP_RANK)

    def __init__(self, rank: str, suit: str):
        """Construct a PlayingCard from a rank and a suit."""
        # Pre:
        assert rank in self._RANK_NAMES and suit in self._SUITS
        self._suit: str = suit
        self._rank: int = self._RANK_NAMES.index(rank)
        # Post:
        assert self._invariant()

    def __str__(self) -> str:
        """Represent the card as a string."""
        # Pre:
        assert self._invariant()
        return (self.suit().capitalize() + ' ' + self.rankName().capitalize()).strip()
        # Post: return value is rank ' of ' suit

    def suit(self) -> str:
        """Get a card's suit."""
        # Pre:
        assert self._invariant()
        result: str = self._suit
        # Post:
        assert result == self._suit
        return result

    def rank(self) -> int:
        """Get a card's rank, as an integer."""
        # Pre:
        assert self._invariant()
        result: int = self._rank
        # Post:
        assert result == self._rank
        return result

    def rankName(self) -> str:
        """Get a card's rank, as a string."""
        # Pre:
        assert self._invariant()
        result: str = self._RANK_NAMES[self._rank]
        # Post:
        assert result == self._RANK_NAMES[self._rank]
        return result

    def __eq__(self, other:Any) -> bool:
        """Compare an AbstractCard to another object for equality.  Cards
        are defined as equal if their ranks and suits are the same.

        Cards can only be compared to objects of their own class.  So,
        for example, an UnoCard can't be compared to a PlayingCard."""
        # Pre:
        assert self._invariant()
        if type(self) != type(other):
            raise NotImplementedError("Cards of different types can't be compared")
        return bool(self.rank() == other.rank() and self.suit() == other.suit())
        # Post: return value is True iff other has the same class as self
        #   (or a subclass) and the ranks and suits are equal

    def __lt__(self, other:Any) -> bool:
        """Compare an AbstractCard to another object for ordering.  A card
        is defined as less than another card if its rank is less or if the
        ranks are equal and the suit alphabetizes before the other card's
        suit.

        Cards can only be compared to objects of their own class or a
        subclass.  So, for example, an UnoCard can't be compared to a
        PlayingCard."""
        # Pre:
        assert self._invariant()
        if type(self) != type(other):
            raise NotImplementedError("Cards of different types can't be compared")
        return bool((self.rank() < other.rank()) or (self.rank() == other.rank()
                                                     and self.suit() < other.suit()))

    @staticmethod
    @abc.abstractmethod
    def makeDeck() -> List['AbstractCard']:
        """Make a deck of whatever kind of card this is.
           Subclasses must override this method."""
        return []
