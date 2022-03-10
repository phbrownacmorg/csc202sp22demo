# Empty unit-testing class
# Peter Brown, 26 Jan 2017

import unittest
# import the module to test
from Stack import Stack

class TestStack(unittest.TestCase):
    # All methods whose names start with "test"
    # will be treated as tests
    def setUp(self) -> None:
        self._empty: Stack[int] = Stack[int]()

        self._s: Stack[int] = Stack[int]()
        self._s.push(5)
        self._s.push(10)

    def test_empty(self) -> None:
        self.assertTrue(self._empty.empty())

    def test_push(self) -> None:
        self.assertFalse(self._s.empty())

    def test_pop_empty(self) -> None:
        with self.assertRaises(IndexError) as cm:
            self._empty.pop()
        exc = cm.exception
        self.assertEqual(exc.args[0], 'Cannot pop from empty stack')

    def test_pop_nonempty(self) -> None:
        self.assertEqual(self._s.pop(), 10)
        self.assertEqual(self._s.pop(), 5)
        self.assertTrue(self._s.empty())

    def test_peek_empty(self) -> None:
        with self.assertRaises(IndexError) as cm:
            self._empty.peek()
        exc = cm.exception
        self.assertEqual(exc.args[0], 'Cannot peek at an empty stack')

    def test_peek_nonempty(self) -> None:
        self.assertEqual(self._s.peek(), 10)
        self.assertEqual(self._s.peek(), 10) # 10 was not removed
        self.assertEqual(self._s.pop(), 10)
        self.assertEqual(self._s.peek(), 5)
        self.assertEqual(self._s.peek(), 5) # 5 was not removed


        with self.assertRaises(IndexError) as cm:
            self._empty.peek()
        exc = cm.exception
        self.assertEqual(exc.args[0], 'Cannot peek at an empty stack')


if __name__ == '__main__':
    unittest.main()