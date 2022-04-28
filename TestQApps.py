# Empty unit-testing class
# Peter Brown, 26 Jan 2017

import unittest
# import the module to test
from q_apps import is_palindrome


class TestQApps(unittest.TestCase):
    # All methods whose names start with "test"
    # will be treated as tests
    def test_nothing(self) -> None:
        self.assertTrue(is_palindrome(''))

    def test_I(self) -> None:
        self.assertTrue(is_palindrome('I'))

    def test_eye(self) -> None:
        self.assertTrue(is_palindrome('eye'))

    def test_ABBA(self) -> None:
        self.assertTrue(is_palindrome('ABBA'))

    def test_Hannah(self) -> None:
        self.assertTrue(is_palindrome('Hannah'))

    def test_Nathan(self) -> None:
        self.assertFalse(is_palindrome('Nathan'))

    def test_adam(self) -> None:
        self.assertTrue(is_palindrome("Madam, I'm Adam."))

    def test_panama(self) -> None:
        self.assertTrue(is_palindrome('A man, a plan, a canal: Panama!'))

    def test_ab(self) -> None:
        self.assertFalse(is_palindrome('ab'))

    def test_alba(self) -> None:
        self.assertFalse(is_palindrome('Alba'))

if __name__ == '__main__':
    unittest.main()