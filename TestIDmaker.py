# Test idmaker_files.py
# Peter Brown, 2022-02-03

from typing import List
import unittest
# import the module to test
from idmaker_files import *

class TestIDMaker(unittest.TestCase):

    # Called before each test.  If you have common setup steps,
    # put them here instead of repeating them.
    def setUp(self) -> None:
        self.names:List[List[str]] = readNames('namegenerator.csv')

    def test_readPeterBrown(self) -> None:
        # Using self.assertEqual to compare lists
        self.assertEqual(self.names[0], ['Brown', 'Peter', 'H.'])

    def test_readLauraFeitzinger(self) -> None:
        self.assertEqual(self.names[1], ['Feitzinger', 'Laura', ''])

    def test_readRedBaron(self) -> None:
        self.assertEqual(self.names[2], ['von Richthofen', 'Manfred', 'Albrecht'])

    def test_namesRead(self) -> None:
        # Using self.assertEqual() to compare integers
        self.assertEqual(len(self.names), 6806)
        # Multiple tests in a loop, with self.subTest() so
        # we can figure out which exact tests fail
        for i in range(len(self.names)):
            with self.subTest(i=i):
                self.assertEqual(len(self.names[i]), 3)

    # Check generic
    def test_makeIDPeterBrown(self) -> None:
        # Using self.assertEqual() to compare strings
        self.assertEqual(makeOneUserid(['Brown', 'Peter', 'H.']), 'phbrown001')

    # Check no middle name
    def test_makeID_LF(self) -> None:
        self.assertEqual(makeOneUserid(['Feitzinger', 'Laura', '']), 'lfeitzinger001')

    # Check removing spaces
    def test_makeID_RedBaron(self) -> None:
        self.assertEqual(makeOneUserid(['von Richthofen', 'Manfred', 'Albrecht']), 
                'mavonrichthofen001')

    # def check removing apostrophes
    def test_makeID_BrianOBrian(self) -> None:
        self.assertEqual(makeOneUserid(["O'Brian", "Brian", "Boru"]), 'bbobrian001')

if __name__ == '__main__':
    unittest.main()