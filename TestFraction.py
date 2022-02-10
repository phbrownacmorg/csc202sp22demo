# Empty unit-testing class
# Peter Brown, 26 Jan 2017

import unittest
from Fraction import Fraction

class TestFraction(unittest.TestCase):
    def test_2_3(self) -> None:
        self.assertTrue(Fraction(2, 3)._invariant())

    def test_reduction_4_6(self) -> None:
        self.assertEqual(str(Fraction(4, 6)), '2/3')

    def test_reduction_m4_6(self) -> None:
        self.assertEqual(str(Fraction(-4, 6)), '-2/3')

    def test_reduction_4_m6(self) -> None:
        self.assertEqual(str(Fraction(4, -6)), '-2/3')

    def test_reduction_m4_m6(self) -> None:
        self.assertEqual(str(Fraction(-4, -6)), '2/3')

    def test_reduction_25_5(self) -> None:
        self.assertEqual(str(Fraction(25, 5)), '5/1')

    def test_reduction_7_49(self) -> None:
        self.assertEqual(str(Fraction(7, 49)), '1/7')

    def test_add_3_5_1_5(self) -> None:
        self.assertEqual(str(Fraction(3, 5) + Fraction(1, 5)), '4/5')

    def test_add_1_3_1_2(self) -> None:
        self.assertEqual(str(Fraction(1, 3) + Fraction(1, 2)), '5/6')

    def test_add_1_3_m1_2(self) -> None:
        self.assertEqual(str(Fraction(1, 3) + Fraction(-1, 2)), '-1/6')

    def test_eq_2_3_2_3(self) -> None:
        self.assertEqual(Fraction(2, 3), Fraction(2, 3))

    # Mismatch in numerators
    def test_eq_2_3_1_3(self) -> None:
        self.assertFalse(Fraction(2, 3) == Fraction(1, 3))

    # Mismatch in denominators
    def test_eq_2_3_2_5(self) -> None:
        self.assertFalse(Fraction(2, 3) == Fraction(2, 5))

    # Mismatch in both
    def test_eq_2_3_1_5(self) -> None:
        self.assertFalse(Fraction(2, 3) == Fraction(1, 5))

    # make sure NotImplementedError gets raised properly
    def test_eq_Frac_str(self) -> None:
        with self.assertRaises(NotImplementedError):
            b: bool = (Fraction(2, 3) == '2/3')

if __name__ == '__main__':
    unittest.main()