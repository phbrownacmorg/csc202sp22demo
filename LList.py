from typing import cast, Generic, Optional, Sized, TypeVar

T = TypeVar('T')

class LList(Generic[T], Sized):
    """Class to represent a linked list, defined as follows:
    A linked list is either: (1) an empty list, or (2) a node,
    followed by a linked list.
    An empty list is defined as a node with both the data and
    the next pointer set to None."""

    def __init__(self): # type: ignore
        """Construct an empty list."""
        self._data: Optional[T] = None
        self._next: Optional[LList[T]] = None
        assert self._invariant()

    # Internal methods

    def _invariant(self) -> bool:
        """Class invariant.  Effectively, this asserts that either
        self is an empty list (_data and _next are both None) or
        self is a node within a list (neither _data nor _next is None)."""        
        return (self._data is None and self._next is None) or \
            (self._data is not None and self._next is not None)

    def _setData(self, data: T) -> None:
        """Mutator method to set the data in the current node."""
        self._data = data

    def _setNext(self, next): # type: (LList[T]) -> None
        """Mutator method to set the successor to the current node."""
        self._next = next

    # Query methods

    def isEmpty(self) -> bool:
        """Query method that returns True when the list is empty."""
        return self._next is None

    def data(self) -> T:
        """Query method that returns the data from the current node."""
        if self.isEmpty():
            raise TypeError('Cannot get data from an empty list.')
        else:
            return cast(T, self._data)

    def next(self) -> 'LList[T]':
        """Query method that returns the next node in the list."""
        if self.isEmpty():
            raise ValueError('Cannot find the next node of an empty list.')
        else:
            return cast(LList[T], self._next)

    def __str__(self) -> str:
        """String representation of the list."""
        if self.isEmpty():
            return "∅"
        else:
            return '❬' + str(self.data()) + '❭➞' + str(self._next)

    def __len__(self) -> int:
        """Find the length of the list."""
        if self.isEmpty():
            return 0
        else:
            return 1 + len(cast(Sized, self._next))

    # Mutator methods

    def add(self, item: T) -> None:
        """Add an item to the beginning of the list."""
        newNode: LList[T] = LList[T]()
        if not self.isEmpty():
            newNode._setData(self.data())
            newNode._setNext(self.next())
        self._setNext(newNode)
        self._setData(item)

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
        if pos == 0:
            item: T = self.data()
            # Order is important!
            self._data = nextNode._data
            self._next = nextNode._next
            return item
        else: # pos > 0
            return nextNode.pop(pos - 1)

    def search(self, item: T) -> bool:
        """Return True iff item ITEM is in the list."""
        if self.isEmpty():
            return False
        elif self.data() == item:
            return True
        else:
            return self.next().search(item)