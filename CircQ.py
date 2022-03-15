from typing import cast, Generic, List, Optional, TypeVar

T = TypeVar('T')

class Queue(Generic[T]):
    """List-based implementation of a circular queue.
    In order to distinguish between an empty queue and
    a full one, empty entries hold None.  Thus, the
    queue can't store an actual None."""

    def __init__(self, capacity: int = 2):
        """Create an empty queue with initial 
        capacity CAPACITY.  The default value for CAPACITY
        is deliberately set low."""
        self._capy: int = capacity # Capacity of the queue
        self._items: List[Optional[T]] = [None] * self._capy
        self._head: int = 0
        self._tail: int = 0
        # Post
        assert self._invariant()

    # Internal methods
    def _invariant(self) -> bool:
        """Class invariant."""
        valid: bool = (self._capy == len(self._items) > 0)
        # Head and tail are within the proper range
        valid = valid and (0 <= self._head < self._capy)
        valid = valid and (0 <= self._tail < self._capy)
        # Item at self._head is not None unless the queue is empty
        valid = valid and (self._items[self._head] is not None 
                    or (self._head == self._tail)) 
        # Item at self._tail is None unless the queue is full
        valid = valid and (self._items[self._tail] is None 
                    or (self._tail == self._head))
        return valid

    def _resize(self) -> None:
        """Double the capacity of the circular queue."""
        temp: List[T] = []
        while not self.empty():
            temp.append(self.pop())
        # Reset the head and tail pointers
        self._head = 0
        self._tail = 0
        self._capy = 2 * self._capy
        for i in range(len(temp)):
            self.add(temp[i])
        assert self._invariant()

    # QUERY METHODS
    def empty(self) -> bool:
        """Check whether the stack is empty."""
        # Pre:
        assert self._invariant()
        return (self._items[self._head] is None)

    def peek(self) -> T:
        """Peek at the head of the queue, without removing the first item."""
        # Pre:
        assert self._invariant()
        if self.empty():
            raise IndexError('Cannot peek at an empty queue')
        return cast(T, self._items[self._head])

    # MUTATOR METHODS
    def add(self, item: T) -> None:
        """Add the given ITEM to the queue."""
        if self._items[self._tail] is not None:
            self._resize()
        self._items[self._tail] = item
        self._tail = self._tail + 1
        if self._tail == self._capy:
            self._tail = 0
        # Post:
        assert not self.empty() and self._invariant()

    def pop(self) -> T:
        """Pop an item off the queue and return it."""
        if self.empty():
            raise IndexError('Cannot pop from empty queue')
        item: T = cast(T, self._items[self._head])
        self._items[self._head] = None
        self._head = self._head + 1
        if self._head == self._capy:
            self._head = 0
        return item
