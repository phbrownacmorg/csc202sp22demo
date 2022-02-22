from typing import List, Tuple
from AbstractCard import AbstractCard

class UnoCard(AbstractCard):
    """Class to represent an Uno card."""

    _SUITS: Tuple[str, ...] = ('red', 'yellow', 'green', 'blue', 'wild')
    _COLOR_SUITS: Tuple[str, ...] = _SUITS[:4]
    _RANK_NAMES: Tuple[str, ...] = ('0', '1', '2', '3', '4', 
                                    '5', '6', '7', '8', '9',
                                    'skip', 'reverse', 'draw 2',
                                    '', 'draw 4')
    _COLOR_RANKS: Tuple[str, ...] = _RANK_NAMES[:-2]
    _WILD_RANKS: Tuple[str, ...] = _RANK_NAMES[-2:]
    _TOP_RANK: int = len(_RANK_NAMES) - 1

    def _invariant(self) -> bool:
        """Class invariant."""
        return ( # Color card
            (self._suit in self._COLOR_SUITS and 
            self._BOTTOM_RANK <= self._rank <= self._TOP_RANK - 2) or
            # Wild card
            (self._suit == 'wild' and 
            self._TOP_RANK - 1 <= self._rank <= self._TOP_RANK))

    def __init__(self, rank: str, suit: str):
        """Construct an UnoCard from the given rank and suit."""
        # Pre:
        assert ((rank.lower() in UnoCard._COLOR_RANKS and 
                suit.lower() in UnoCard._COLOR_SUITS) or
                (rank.lower() in UnoCard._WILD_RANKS and 
                suit.lower() == 'wild'))
        super().__init__(rank.lower(), suit.lower())

    def __str__(self) -> str:
        """Represent the card as a string."""
        return super().__str__().strip()

    @staticmethod
    def makeDeck() -> List[AbstractCard]:
        """Make and return an Uno deck."""
        # Temporary
        return []

    # Ignore for the purposes of Lab 3!
    @staticmethod
    def makeSomeColorCards() -> List[AbstractCard]:
        """Make and return a List containing a single copy of all the color cards."""
        # Pre: none
        result: List[AbstractCard] = []
        for rank in UnoCard._COLOR_RANKS:
            for suit in UnoCard._COLOR_SUITS:
                result.append(UnoCard(rank, suit))
        return result