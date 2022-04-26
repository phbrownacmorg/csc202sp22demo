# Empty unit-testing class
# Peter Brown, 26 Jan 2017

from typing import List
import unittest
# import the module to test
from search import binsearch, seqsearch

class TestSearch(unittest.TestCase):

    def setUp(self) -> None:
        self._empty: List[str] = []
        self._five: List[str] = ['0', '2', '4', '6', '8']
        self._one: List[str] = self._five[:1]
        self._two: List[str] = self._five[:2]
        self._three: List[str] = self._five[:3]
        self._four: List[str] = self._five[:4]

    # All methods whose names start with "test"
    # will be treated as tests
    def test_seq_empty(self) -> None:
        with self.assertRaises(ValueError):
            seqsearch(self._empty, 'anything')

    def test_seq_1_only(self) -> None:
        self.assertEqual(seqsearch(self._one, '0'), 0)

    def test_seq_1_absent(self) -> None:
        with self.assertRaises(ValueError):
            seqsearch(self._one, 'anything')

    def test_seq_5(self) -> None:
        for i in range(len(self._five)):
            with self.subTest(i=i):
                self.assertEqual(seqsearch(self._five, str(2*i)), i)
        with self.assertRaises(ValueError):
            seqsearch(self._five, 'anything')

    def test_bin_empty(self) -> None:
        with self.assertRaises(ValueError):
            binsearch(self._empty, 'anything')

    def test_bin_1_only(self) -> None:
        self.assertEqual(binsearch(self._one, '0'), 0)

    def test_bin_1_absent(self) -> None:
        with self.assertRaises(ValueError):
            binsearch(self._one, 'anything')

    def test_bin_5(self) -> None:
        for i in range(len(self._five)):
            with self.subTest(i=i):
                self.assertEqual(binsearch(self._five, str(2*i)), i)

    def test_bin_5_absent(self) -> None:
        for i in range(len(self._five)+1):
            with self.subTest(i=i):    
                with self.assertRaises(ValueError):
                    binsearch(self._five, str(2*i - 1))
    
    def test_bin_4(self) -> None:
        for i in range(len(self._four)):
            with self.subTest(i=i):
                self.assertEqual(binsearch(self._four, str(2*i)), i)
        
    def test_bin_4_absent(self) -> None:
        for i in range(len(self._four)+1):
            with self.subTest(i=i):    
                with self.assertRaises(ValueError):
                    binsearch(self._four, str(2*i - 1))




if __name__ == '__main__':
    unittest.main()