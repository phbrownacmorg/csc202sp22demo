from typing import Generic, List, TypeVar

T = TypeVar('T')

class Stack(Generic[T]):
    """Class to represent a stack.  This implementation
    is based on a Python list, where the end of the list is
    the top of the stack."""

    def __init__(self): # type: ignore
        """Create an empty stack."""
        self._items: List[T] = []

    # QUERY METHODS
    def empty(self) -> bool:
        """Check whether the stack is empty."""
        return (len(self._items) == 0)

    def peek(self) -> T:
        """Peek at the top of the stack, without removing the top item."""
        if self.empty():
            raise IndexError('Cannot peek at an empty stack')
        return self._items[-1]

    # MUTATOR METHODS
    def push(self, item: T) -> None:
        """Push the given ITEM onto the stack."""
        self._items.append(item)
        # Post:
        assert not self.empty()

    def pop(self) -> T:
        """Pop an item off the stack and return it."""
        if self.empty():
            raise IndexError('Cannot pop from empty stack')
        return self._items.pop()
    

    

