from typing import cast, Generic, List, Optional, Sized, TypeVar

T = TypeVar('T')

class DLList(Generic[T], Sized):
    """Class to represent a doubly-linked list.
    This implementation has a tail pointer."""

    class Node:
        """Class to represent a node of a doubly-linked list."""

        def __init__(self):
            """Construct an empty node."""
            self._data = None
            self._next = None
            self._prev = None

    def __init__(self):
        """Construct an empty doubly-linked list."""
        self._head = None
        self._tail = None
    
    def _invariant(self) -> bool:
        valid: bool = (self._head is None and self._tail is None) \
            or (self._head is not None and self._tail is not None)
        # Ideally, should check links.  But how to avoid an 
        # infinite loop if the links *aren't* right?
        return valid

    # Query methods
    def isEmpty(self) -> bool:
        return self._head is None

    