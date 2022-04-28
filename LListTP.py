from typing import cast, Generic, Optional, Sized, TypeVar
from LList import LList

T = TypeVar('T')

class LListTP(Generic[T], Sized):
    """Class to represent a linked list with a tail pointer."""

    def __init__(self):
        """Construct an empty LListTP."""
        self._head: LList[T] = LList[T]() # Sentinel node
        self._tail: LList[T] = self._head
        assert self._invariant()

    # Internal methods
    def _invariant(self) -> bool:
        """Class invariant."""
        result: bool = self._head._invariant()
        result = result and self._tail._invariant()
        result = result and \
            ((self._tail.isEmpty() and self._tail == self._head)
            or (cast(LList[T], self._tail._next).isEmpty() and cast(LList[T], self._head._next).isEmpty() and self._tail == self._head)
            or (cast(LList[T], self._tail._next).isEmpty() and self._tail != self._head))
        return result

    # Query methods
    def isEmpty(self) -> bool:
        return (self._head.isEmpty())

    def __str__(self) -> str:
        return str(self._head)

    def __len__(self) -> int:
        return len(self._head)

    def search(self, item: T) -> bool:
        return self._head.search(item)

    # Mutator methods

    def add(self, item: T) -> None: # O(1)
        """Add an item to the beginning of the list."""
        self._head.add(item)

    def pop(self, pos: int = 0) -> T: # O(n)
        """Remove and return the item at position POS from the list.
        Default is to remove the *first* item."""
        # Pre: -len(self) <= pos < len(self)
        if self.isEmpty():
            raise ValueError('Cannot pop from an empty list.')
        
        if pos < 0: # Handle negative values of pos; only happens once
            pos = len(self) + pos
        assert pos >= 0 # Otherwise, the precondition was violated

        value: T = self._head.pop(pos) # O(n), but there's no gain to speeding it up

        # Reset the tail pointer, if required
        # If anything other than the last node was popped,
        #   the tail pointer is still valid.
        # If the last node was popped, the tail pointer
        #   is now pointing to the sentinel, so it's empty.
        if self._tail.isEmpty():
            self._tail = self._head
            if not self._head.isEmpty():
                while not self._tail.next().isEmpty():
                    self._tail = cast(LList[T], self._tail._next)
        return value

    def append(self, item: T) -> None: # O(1)
        # Make a new node
        newNode: LList[T] = LList[T]()
        newNode._data = item

        # Link in the new node
        if self._head.isEmpty():
            newNode._next = self._tail
            self._head = newNode
        else:
            newNode._next = self._tail._next
            self._tail._next = newNode

        # Update the tail pointer
        self._tail = newNode