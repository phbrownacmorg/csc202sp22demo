from typing import Generic, List, TypeVar

T = TypeVar('T')

class Queue(Generic[T]):
    """List-based implementation of a queue."""

    def __init__(self): # type: ignore
        """Create an empty queue."""
        self._items: List[T] = []

    # QUERY METHODS
    def empty(self) -> bool:
        """Check whether the stack is empty."""
        return (len(self._items) == 0)

    def peek(self) -> T:
        """Peek at the head of the queue, without removing the first item."""
        if self.empty():
            raise IndexError('Cannot peek at an empty queue')
        return self._items[0]

    # MUTATOR METHODS
    def add(self, item: T) -> None:
        """Add the given ITEM to the queue."""
        self._items.append(item)
        # Post:
        assert not self.empty()

    def pop(self) -> T:
        """Pop an item off the queue and return it."""
        if self.empty():
            raise IndexError('Cannot pop from empty queue')
        return self._items.pop(0)
