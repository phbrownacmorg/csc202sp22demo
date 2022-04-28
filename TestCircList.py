# Empty unit-testing class
# Peter Brown, 26 Jan 2017

import unittest
# import the module to test
from CircList import CircList

class TestCircList(unittest.TestCase):
    # All methods whose names start with "test"
    # will be treated as tests

    def setUp(self) -> None:
        self._empty: CircList[str] = CircList[str]()

        self._one: CircList[str] = CircList[str]()
        self._one.add("one")

        self._two: CircList[str] = CircList[str]()
        self._two.add('two')
        self._two.add('one')

    def test_empty_isEmpty(self) -> None:
        self.assertTrue(self._empty.isEmpty())
        
    def test_str_isEmpty(self) -> None:
        self.assertEqual(str(self._empty), "∅")

    def test_data_empty(self) -> None:
        with self.assertRaises(TypeError) as cm:
            self._empty._tail.data()
        self.assertEqual(cm.exception.args[0], 
            'Cannot get data from an empty list.')            

    def test_next_empty(self) -> None:
        with self.assertRaises(ValueError) as cm:
            self._empty._tail.next()
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
        self.assertFalse(self._empty.search('one'))

    def test_empty_one(self) -> None:
        self.assertFalse(self._one.isEmpty())
        
    def test_str_one(self) -> None:
        self.assertEqual(str(self._one), "❬one❭")

    def test_len_one(self) -> None:
        self.assertEqual(len(self._one), 1)

    def test_pop_one(self) -> None:
        self.assertEqual(self._one.pop(), 'one')
        self.assertTrue(self._one.isEmpty())

    def test_pop_one_n1(self) -> None:
        self.assertEqual(self._one.pop(-1), 'one')
        self.assertTrue(self._one.isEmpty())

    def test_search_one(self) -> None:
        self.assertTrue(self._one.search('one'))
        self.assertFalse(self._one.search('two'))

    def test_empty_two(self) -> None:
        self.assertFalse(self._two.isEmpty())
        
    def test_str_two(self) -> None:
        self.assertEqual(str(self._two), "❬one❭➞❬two❭")

    def test_len_two(self) -> None:
        self.assertEqual(len(self._two), 2)

    def test_pop_two_0(self) -> None:
        self.assertEqual(self._two.pop(), 'one')
        self.assertEqual(str(self._two), "❬two❭")

    def test_pop_two_n2(self) -> None:
        self.assertEqual(self._two.pop(-2), 'one')
        self.assertEqual(str(self._two), "❬two❭")
        self.assertEqual(len(self._two), 1)
        
    def test_append_empty(self) -> None:
        self._empty.append('three')
        self.assertEqual(len(self._empty), 1)
        self.assertEqual(str(self._empty), "❬three❭")

    def test_append_one(self) -> None:
        self._one.append('three')
        self.assertEqual(len(self._one), 2)
        self.assertEqual(str(self._one), "❬one❭➞❬three❭")

    def test_append_two(self) -> None:
        self._two.append('three')
        self.assertEqual(len(self._two), 3)
        self.assertEqual(str(self._two), "❬one❭➞❬two❭➞❬three❭")


if __name__ == '__main__':
    unittest.main()