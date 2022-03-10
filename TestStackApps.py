# Empty unit-testing class
# Peter Brown, 26 Jan 2017

import unittest
# import the module to test
from stack_apps import match_delimiters

class TestStackApps(unittest.TestCase):
    # All methods whose names start with "test"
    # will be treated as tests
    def test_nothing(self) -> None:
        self.assertTrue(match_delimiters(''))

    def test_left_only(self) -> None:
        self.assertFalse(match_delimiters('('))

    def test_balanced_parens2(self) -> None:
        self.assertTrue(match_delimiters('()'))
        
    def test_out_of_order(self) -> None:
        self.assertFalse(match_delimiters(')('))

    def test_unmatched(self) -> None:
        self.assertFalse(match_delimiters('(]'))

    def test_textbook_examples(self) -> None:
        self.assertTrue(match_delimiters('(()()()())'))
        self.assertTrue(match_delimiters('(((())))'))
        self.assertTrue(match_delimiters('(()((())()))'))
        self.assertFalse(match_delimiters('((((((())'))
        self.assertFalse(match_delimiters('()))'))
        self.assertFalse(match_delimiters('(()()(()'))

    def test_mixed_delimiters(self) -> None:
        self.assertTrue(match_delimiters('([]{}<>)'))
        self.assertFalse(match_delimiters('([}{><])'))        

    def test_other_chars(self) -> None:
        self.assertTrue(match_delimiters('(foo [bar] {baz.}<oogba />)'))
        
if __name__ == '__main__':
    unittest.main()