from typing import Generic, List, TypeVar
from Stack import Stack

T = TypeVar('T')

class Queue(Generic[T]):
    """Implementation of a queue based on two stacks."""

    def __init__(self): # type: ignore
        """Create an empty queue."""
        self._inbox: Stack[T] = Stack[T]()
        self._outbox: Stack[T] = Stack[T]()

    # QUERY METHODS
    def empty(self) -> bool:
        """Check whether the stack is empty."""
        return (self._inbox.empty() and self._outbox.empty())

    def peek(self) -> T:
        """Peek at the head of the queue, without removing the first item."""
        if self.empty():
            raise IndexError('Cannot peek at an empty queue')
        if self._outbox.empty():
            while not self._inbox.empty():
                self._outbox.push(self._inbox.pop())
        return self._outbox.peek()

    # MUTATOR METHODS
    def add(self, item: T) -> None: # O(1)
        """Add the given ITEM to the queue."""
        self._inbox.push(item)
        # Post:
        assert not self.empty() # O(1)

    def pop(self) -> T: # O(1)
        """Pop an item off the queue and return it."""
        if self.empty():
            raise IndexError('Cannot pop from empty queue')
        if self._outbox.empty(): # O(n), but only happens 1/n of the time
            while not self._inbox.empty():
                self._outbox.push(self._inbox.pop())
        return self._outbox.pop() # O(1)
