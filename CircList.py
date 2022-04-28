from typing import cast, Generic, List, Optional, Sized, TypeVar
from LList import LList

T = TypeVar('T')

class CircList(Generic[T], Sized):
    """Class to represent a circular linked list.
    The list pointer points to the last item,
    not the first."""

    # Constructor

    def __init__(self):
        """Construct an empty CircList."""
        self._tail: LList[T] = LList[T]()
        assert self._invariant()

    # Internal method

    def _invariant(self) -> bool:
        """Class invariant."""
        valid = True
        # if not self._tail.isEmpty():
        #     # Are the links correct?
        #     current: LList[T] = self._tail
        #     current = current._next
        #     while valid and current != self._tail:
        #         valid = valid and (not current.isEmpty())

        #     if not current.next().isEmpty():
        #         current = current.next()

        #     valid = valid and 
        return valid

    # Query methods

    def isEmpty(self) -> bool:
        return self._tail.isEmpty()

    def __str__(self) -> str:
        """String representation of the list."""
        result: str = ''
        if self.isEmpty():
            result = '∅'
        else:
            current: LList[T] = self._tail
            while True:
                current = current.next()
                result = result + '❬' + str(current.data()) + '❭'
                if current == self._tail:
                    break
                else:
                    result = result + '➞'
        return result

    def __len__(self) -> int:
        """Find the length of the list."""
        result = 0
        if not self.isEmpty():
            current: LList[T] = self._tail.next()
            while True:
                result = result + 1
                if current == self._tail:
                    break
                else:
                    current = current.next()
        return result
    
    def search(self, item: T) -> bool:
        found = False
        if not self.isEmpty():
            current: LList[T] = self._tail.next()
            found = (item == current.data())
            while not found and current != self._tail:
                current = current.next()
                found = (item == current.data())
        return found

    # Mutator methods

    def add(self, item: T) -> None:
        """Add an item to the beginning of the list."""
        newNode = LList[T]()
        newNode._data = item
        if self.isEmpty():
            newNode._next = newNode
            self._tail = newNode
        else:
            newNode._next = self._tail._next
            self._tail._next = newNode

    def append(self, value: T) -> None:
        """Add an item to the end of the list."""
        self.add(value)
        # Only difference between append() and add()!
        self._tail = self._tail.next()

    def pop(self, pos: int = 0) -> T:
        """Remove and return the item at position POS from the list.
        Default is to remove the *first* item."""
                # Pre: -len(self) <= pos < len(self)
        if self.isEmpty():
            raise ValueError('Cannot pop from an empty list.')
        elif len(self) == 1:
            # Pos doesn't really matter when there's only one node
            value: T = self._tail.data()
            self._tail = LList[T]()
        else:
            if pos < 0: # Handle negative values of pos; only happens once
                pos = len(self) + pos
            assert pos >= 0 # Otherwise, the precondition was violated

            # Count down
            predecessor: LList[T] = self._tail
            victim: LList[T] = cast(LList[T], self._tail._next)
            assert victim == predecessor._next
            for i in range(pos):
                predecessor = victim
                victim = victim.next()
            # Do the actual popping
            value = victim.data()
            predecessor._next = victim._next
        return value

