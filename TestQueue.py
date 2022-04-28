# Empty unit-testing class
# Peter Brown, 26 Jan 2017

import unittest
# import the module to test
from CircQ import Queue

class TestQueue(unittest.TestCase):
    # All methods whose names start with "test"
    # will be treated as tests
    def setUp(self) -> None:
        self._empty: Queue[int] = Queue[int]()

        self._s: Queue[int] = Queue[int]()
        self._s.add(5)
        self._s.add(10)
        self._s.add(15)

    def test_empty(self) -> None:
        self.assertTrue(self._empty.empty())

    def test_add(self) -> None:
        self.assertFalse(self._s.empty())

    def test_pop_empty(self) -> None:
        with self.assertRaises(IndexError) as cm:
            self._empty.pop()
        exc = cm.exception
        self.assertEqual(exc.args[0], 'Cannot pop from empty queue')

    def test_pop_nonempty(self) -> None:
        self.assertEqual(self._s.pop(), 5)
        self.assertEqual(self._s.pop(), 10)
        self.assertEqual(self._s.pop(), 15)
        self.assertTrue(self._s.empty())

    def test_peek_empty(self) -> None:
        with self.assertRaises(IndexError) as cm:
            self._empty.peek()
        exc = cm.exception
        self.assertEqual(exc.args[0], 'Cannot peek at an empty queue')

    def test_peek_nonempty(self) -> None:
        self.assertEqual(self._s.peek(), 5)
        self.assertEqual(self._s.peek(), 5) # 5 was not removed
        self.assertEqual(self._s.pop(), 5)
        self.assertEqual(self._s.peek(), 10)
        self.assertEqual(self._s.peek(), 10) # 10 was not removed

if __name__ == '__main__':
    unittest.main()