from typing import cast, Generic, Optional, Sized, TypeVar
from LList import LList

T = TypeVar('T')

class LListTP(Generic[T], Sized):
    """Class to represent a linked list with a tail pointer."""

    def __init__(self):
        """Construct an empty LListTP."""
        self._head: LList[T] = LList[T]()
        self._tail: LList[T] = self._head
        assert self._invariant()

    # Internal methods
    def _invariant(self) -> bool:
        """Class invariant."""
        result: bool = self._head._invariant()
        result = result and self._tail._invariant()
        result = result and \
            ((self._tail.isEmpty() and self._tail == self._head)
            or (self._tail._next.isEmpty() and self._head._next.isEmpty() and self._tail == self._head)
            or (self._tail._next.isEmpty() and self._tail != self._head))

    # Query methods
    def isEmpty(self) -> bool:
        return (self._head.isEmpty())

    def __str__(self) -> str:
        return str(self._head)

    def __len__(self) -> int:
        return len(self._head)

    # Mutator methods

    def add(self, item: T) -> None:
        """Add an item to the beginning of the list."""
        self._head.add(item)

    def pop(self, pos: int = 0) -> T:
        """Remove and return the item at position POS from the list.
        Default is to remove the *first* item."""
        # Pre: -len(self) <= pos < len(self)
        if self.isEmpty():
            raise ValueError('Cannot pop from an empty list.')
        
        # Safe to cast because we know self is not empty
        nextNode: LList[T] = cast(LList[T], self.next())
        if pos < 0: # Handle negative values of pos; only happens once
            pos = len(self) + pos
        assert pos >= 0 # Otherwise, the precondition was violated


    def search(self, item: T) -> bool:
        return self._head.search(item)