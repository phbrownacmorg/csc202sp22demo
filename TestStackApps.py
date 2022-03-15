# Empty unit-testing class
# Peter Brown, 26 Jan 2017

import unittest
# import the module to test
from stack_apps import match_delimiters
from stack_apps import convert_bases

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

    def test_convert_0(self) -> None:
        self.assertEqual(convert_bases(0, 16), '0')

    def test_convert_1000(self) -> None:
        self.assertEqual(convert_bases(1000, 10), '1000')

    def test_convert_255h(self) -> None:
        self.assertEqual(convert_bases(255, 16), 'ff')

    def test_convert_256h(self) -> None:
        self.assertEqual(convert_bases(256, 16), '100')

    def test_convert_256b(self) -> None:
        self.assertEqual(convert_bases(256, 2), '100000000')

    def test_convert_n256d(self) -> None:
        self.assertEqual(convert_bases(-256, 10), '-256')

    def test_convert_n255o(self) -> None:
        self.assertEqual(convert_bases(-255, 8), '-377')

if __name__ == '__main__':
    unittest.main()