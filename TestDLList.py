# Empty unit-testing class
# Peter Brown, 26 Jan 2017

import unittest
# import the module to test
from DLList import DLList, _Node

class TestDLList(unittest.TestCase):
    # All methods whose names start with "test"
    # will be treated as tests

    def setUp(self) -> None:
        self._empty: DLList[str] = DLList[str]()

        self._one: DLList[str] = DLList[str]()
        self._one.add('one')

        self._two: DLList[str] = DLList[str]()
        self._two.add('one')
        self._two.add('two')

        self._three: DLList[str] = DLList[str]()
        self._three.add('one')
        self._three.add('two')
        self._three.add('three')

    def test_isEmpty(self) -> None:
        self.assertTrue(self._empty.isEmpty())
        self.assertFalse(self._one.isEmpty())
        self.assertFalse(self._two.isEmpty())
        self.assertFalse(self._three.isEmpty())

    def test_str(self) -> None:
        self.assertEqual(str(self._empty), '∅')
        self.assertEqual(str(self._one), '❬one❭')
        self.assertEqual(str(self._two), '❬one❭⇆❬two❭')
        self.assertEqual(str(self._three), '❬one❭⇆❬two❭⇆❬three❭')

    def test_len(self) -> None:
        self.assertEqual(len(self._empty), 0)
        self.assertEqual(len(self._one), 1)
        self.assertEqual(len(self._two), 2)
        self.assertEqual(len(self._three), 3)

    def test_pop_empty(self) -> None:
        with self.assertRaises(IndexError):
            self._empty.pop()

    def test_pop_one(self) -> None:
        self.assertEqual(self._one.pop(), 'one')
        self.assertTrue(self._one.isEmpty())

    def test_pop_one_0(self) -> None:
        self.assertEqual(self._one.pop(0), 'one')
        self.assertTrue(self._one.isEmpty())

    def test_pop_one_1(self) -> None:
        with self.assertRaises(IndexError):
            self._one.pop(1)

    def test_pop_two(self) -> None:
        self.assertEqual(self._two.pop(), 'two')
        self.assertEqual(str(self._two), '❬one❭')

    def test_pop_two_n2(self) -> None:
        self.assertEqual(self._two.pop(-2), 'one')
        self.assertEqual(str(self._two), '❬two❭')

    def test_pop_two_0(self) -> None:
        self.assertEqual(self._two.pop(0), 'one')
        self.assertEqual(str(self._two), '❬two❭')

    def test_pop_three(self) -> None:
        self.assertEqual(self._three.pop(), 'three')
        self.assertEqual(str(self._three), '❬one❭⇆❬two❭')

    def test_pop_three_n2(self) -> None:
        self.assertEqual(self._three.pop(-2), 'two')
        self.assertEqual(str(self._three), '❬one❭⇆❬three❭')

    def test_pop_three_0(self) -> None:
        self.assertEqual(self._three.pop(0), 'one')
        self.assertEqual(str(self._three), '❬two❭⇆❬three❭')

    def test_search(self) -> None:
        self.assertFalse(self._empty.search('one'))
        self.assertTrue(self._one.search('one'))
        self.assertFalse(self._one.search('two'))
        self.assertTrue(self._two.search('one'))
        self.assertTrue(self._two.search('two'))
        self.assertFalse(self._two.search('three'))
        self.assertTrue(self._three.search('one'))
        self.assertTrue(self._three.search('two'))
        self.assertTrue(self._three.search('three'))
        self.assertFalse(self._three.search('four'))


if __name__ == '__main__':
    unittest.main()