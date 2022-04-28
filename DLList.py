from typing import cast, Generic, List, Optional, Sized, TypeVar

T = TypeVar('T')

class _Node(Generic[T]):
    """Class to represent a node of a doubly-linked list."""

    def __init__(self, value: T):
        """Construct a node with data VALUE."""
        self._data: T = value
        self._next: Optional[_Node] = None
        self._prev: Optional[_Node] = None

    def __str__(self) -> str:
        """String representation of a _Node."""
        return '❬' + str(self._data) + '❭'

class DLList(Generic[T], Sized):
    """Class to represent a doubly-linked list.
    This implementation has a tail pointer."""

    def __init__(self): # type: ignore
        """Construct an empty doubly-linked list."""
        self._head: Optional[_Node[T]] = None
        self._tail: Optional[_Node[T]] = None
        assert self._invariant()
    
    def _invariant(self) -> bool:
        """Class invariant."""
        valid: bool = (self._head is None and self._tail is None) \
            or (self._head is not None and self._tail is not None)
        # Ideally, should check links.  But how to avoid an 
        # infinite loop if the links *aren't* right?
        return valid

    # Query methods
    def isEmpty(self) -> bool:
        """Query to tell if the list is empty."""
        # Pre:
        assert self._invariant()
        return self._head is None

    def __len__(self) -> int:
        """Find the length of the list."""
        # Pre:
        assert self._invariant()
        length: int = 0
        if not self.isEmpty():
            current: _Node = cast(_Node, self._head)
            length = 1
            while (current != self._tail):
                current = cast(_Node, current._next)
                length = length + 1
        return length

    def __str__(self) -> str:
        """String representation."""
        assert self._invariant()
        result: str = ''
        if self.isEmpty():
            result = '∅'
        else:
            result = ''
            current: _Node = cast(_Node, self._head)
            result = str(current)
            while (current != self._tail):
                current = cast(_Node, current._next)
                result = result + '⇆' + str(current)
        return result

    def search(self, value: T) -> bool:
        """Search for the given VALUE in the list, and return True if present."""
        found: bool = False
        if not self.isEmpty():
            current: _Node[T] = cast(_Node[T], self._head)
            if current._data == value:
                found = True
            while (not found) and (current != self._tail):
                current = cast(_Node[T], current._next)
                if current._data == value:
                    found = True
        return found

    # Mutator methods

    def add(self, item: T) -> None:
        newNode: _Node[T] = _Node[T](item)
        if self.isEmpty():
            self._head = newNode
            self._tail = newNode
        else:
            cast(_Node[T], self._tail)._next = newNode
            newNode._prev = self._tail
            self._tail = newNode
        # Post
        assert self._invariant()

    def pop(self, pos: int = -1) -> T:
        """Remove the item at index POS from the
            list and return its data.  POS defaults
            to the end of the list."""
        # Pre: -len(self) <= pos < len(self)
        if self.isEmpty():
            raise IndexError('Cannot pop from an empty list.')
        else:
            if pos < 0: # Handle negative values of pos; only happens once
                pos = len(self) + pos
            assert pos >= 0 # Otherwise, the precondition was violated

            value: T = cast(_Node[T], self._tail)._data
            if pos == 0 and self._head == self._tail: # Removing the only node from the list
                self._head = None
                self._tail = None
            elif pos == 0: # len(self) > 1
                value = self._head._data
                self._head = self._head._next
                self._head._prev = None
            elif pos == len(self) - 1: # Work from the tail
                newTail: _Node[T] = self._tail._prev # type: ignore
                newTail._next = None
                self._tail = newTail
            else:
                current: _Node[T] = self._head
                while pos > 0:
                    current = current._next
                    if current is None:
                        raise IndexError('pop: pos exceeds length of list.')
                    pos = pos - 1
                value = current._data
                current._prev._next = current._next
                current._next._prev = current._prev

            assert self._invariant()
            return value
