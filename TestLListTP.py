# Empty unit-testing class
# Peter Brown, 26 Jan 2017

import unittest
# import the module to test
from LListTP import LListTP

class TestLListTP(unittest.TestCase):
    # All methods whose names start with "test"
    # will be treated as tests

    def setUp(self) -> None:
        self._empty: LListTP[int] = LListTP[int]()

        self._one: LListTP[int] = LListTP[int]()
        self._one.add(1)

        self._two: LListTP[int] = LListTP[int]()
        self._two.add(2)
        self._two.add(1)

    def test_empty_isEmpty(self) -> None:
        self.assertTrue(self._empty.isEmpty())
        
    def test_str_isEmpty(self) -> None:
        self.assertEqual(str(self._empty), "∅")

    def test_data_empty(self) -> None:
        with self.assertRaises(TypeError) as cm:
            self._empty._head.data()
        self.assertEqual(cm.exception.args[0], 
            'Cannot get data from an empty list.')            

    def test_next_empty(self) -> None:
        with self.assertRaises(ValueError) as cm:
            self._empty._head.next()
        self.assertEqual(cm.exception.args[0], 
            'Cannot find the next node of an empty list.')

    def test_len_empty(self) -> None:
        self.assertEqual(len(self._empty), 0)

    def test_pop_empty(self) -> None:
        with self.assertRaises(ValueError) as cm:
            self._empty.pop()
        self.assertEqual(cm.exception.args[0],
                        'Cannot pop from an empty list.')

    def testSearchEmpty(self) -> None:
        self.assertFalse(self._empty.search(1))

    def test_empty_one(self) -> None:
        self.assertFalse(self._one.isEmpty())
        
    def test_str_one(self) -> None:
        self.assertEqual(str(self._one), "❬1❭➞∅")

    def test_data_one(self) -> None:
        self.assertEqual(self._one._head.data(), 1)

    def test_next_one(self) -> None:
        self.assertEqual(str(self._one._head.next()), "∅")

    def test_len_one(self) -> None:
        self.assertEqual(len(self._one), 1)

    def test_pop_one(self) -> None:
        self.assertEqual(self._one.pop(), 1)
        self.assertTrue(self._one.isEmpty())

    def test_pop_one_n1(self) -> None:
        self.assertEqual(self._one.pop(-1), 1)
        self.assertTrue(self._one.isEmpty())

    def test_search_one(self) -> None:
        self.assertTrue(self._one.search(1))
        self.assertFalse(self._one.search(2))

    def test_empty_two(self) -> None:
        self.assertFalse(self._two.isEmpty())
        
    def test_str_two(self) -> None:
        self.assertEqual(str(self._two), "❬1❭➞❬2❭➞∅")

    def test_data_two(self) -> None:
        self.assertEqual(self._two._head.data(), 1)

    def test_next_two(self) -> None:
        self.assertEqual(str(self._two._head.next()), "❬2❭➞∅")

    def test_len_two(self) -> None:
        self.assertEqual(len(self._two), 2)

    def test_pop_two_0(self) -> None:
        self.assertEqual(self._two.pop(), 1)
        self.assertEqual(str(self._two), "❬2❭➞∅")

    def test_pop_two_n2(self) -> None:
        self.assertEqual(self._two.pop(-2), 1)
        self.assertEqual(str(self._two), "❬2❭➞∅")

    def test_pop_two_1(self) -> None:
        self.assertEqual(self._two.pop(1), 2)
        self.assertEqual(str(self._two), "❬1❭➞∅")

    def test_pop_two_n1(self) -> None:
        self.assertEqual(self._two.pop(-1), 2)
        self.assertEqual(str(self._two), "❬1❭➞∅")

    def test_search_two(self) -> None:
        self.assertTrue(self._two.search(1))
        self.assertTrue(self._two.search(2))
        self.assertFalse(self._two.search(3))

    def test_append_empty(self) -> None:
        self._empty.append(3)
        self.assertEqual(len(self._empty), 1)
        self.assertEqual(self._empty._tail.data(), 3)

    def test_append_one(self) -> None:
        self._one.append(3)
        self.assertEqual(len(self._one), 2)
        self.assertEqual(self._one._tail.data(), 3)

    def test_append_two(self) -> None:
        self._two.append(3)
        self.assertEqual(len(self._two), 3)
        self.assertEqual(self._two._tail.data(), 3)


if __name__ == '__main__':
    unittest.main()