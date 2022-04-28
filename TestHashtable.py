# Empty unit-testing class
# Peter Brown, 26 Jan 2017

import unittest
# import the module to test
from Hashtable import letterhash, Hashtable

class TestNothing(unittest.TestCase):
    # All methods whose names start with "test"
    # will be treated as tests

    def setUp(self) -> None:
        self._empty = Hashtable()

        self._one = Hashtable()
        self._one.put('Peter Brown', '864-596-9156')

        self._four = Hashtable()
        self._four.put('Joe Barrera', '864-596-9128')
        self._four.put('Peter Brown', '864-596-9156')
        self._four.put('Amanda Mangum', '864-596-9127')
        self._four.put('Jessica Sorrells', '864-596-9149')

    def test_hash_a(self) -> None:
        self.assertEqual(letterhash('a'), 1)

    def test_hash_empty(self) -> None:
        self.assertEqual(letterhash(''), 0)
        
    def test_hash_Peter(self) -> None:
        # 16 + 5 (421) + 20 (10966)
        #  + 5 (285121) + 18 (7413164)
        self.assertEqual(letterhash('Peter'), 7413164)
        self.assertEqual(letterhash('peter'), 7413164)

    def test_hash_ab_ba(self) -> None:
        self.assertEqual(letterhash('ab'), 28)
        self.assertEqual(letterhash('ba'), 53)

    def test_hashfn_empty(self) -> None:
        self.assertEqual(self._empty._hash(''), 0)
        self.assertEqual(self._empty._hash('a'), 1)
        self.assertEqual(self._empty._hash('ab'), 1)
        self.assertEqual(self._empty._hash('ba'), 2)
        self.assertEqual(self._empty._hash('Peter Brown'), 0)
        self.assertEqual(self._empty._hash('Jessica Sorrells'), 1)
        self.assertEqual(self._empty._hash('Amanda Mangum'), 1)
        self.assertEqual(self._empty._hash('Joe Barrera'), 1)

    def test_table_size(self) -> None:
        self.assertEqual(len(self._empty._table), 3)
        self.assertEqual(len(self._one._table), 3)
        self.assertEqual(len(self._four._table), 3)

    def test_get_empty(self) -> None:
        self.assertEqual(self._empty.get('Joe Barrera'), None)

    def test_get_one(self) -> None:
        self.assertEqual(self._one.get('Joe Barrera'), None)
        self.assertEqual(self._one.get('Peter Brown'), '864-596-9156')

    def test_get_four(self) -> None:
        self.assertEqual(self._four.get('Boone Hopkins'), None)
        self.assertEqual(self._four.get('Peter Brown'), '864-596-9156')
        self.assertEqual(self._four.get('Joe Barrera'), '864-596-9128')
        self.assertEqual(self._four.get('Amanda Mangum'), '864-596-9127')
        self.assertEqual(self._four.get('Jessica Sorrells'), '864-596-9149')

    def test_put_four(self) -> None:
        with self.assertRaises(ValueError):
            self._four.put('Peter Brown', '201-744-9317')

if __name__ == '__main__':
    unittest.main()