# Empty unit-testing class
# Peter Brown, 26 Jan 2017

from typing import cast, List
import unittest
# import the module to test
from recursion import *

class TestRecursion(unittest.TestCase):
    
    # sumlist

    def test_sumlist_empty(self) -> None:
        self.assertEqual(sumlist(cast(List[float], [])), 0)

    def test_sumlist_one(self) -> None:
        self.assertEqual(sumlist(cast(List[float], [1])), 1)

    def test_sumlist_3(self) -> None:
        self.assertEqual(sumlist(cast(List[float], [1, 2, 3])), 6)
    
    def test_sumlist_9(self) -> None:
        self.assertEqual(sumlist(cast(List[float], [1, 2, 3, 4, 5, 6, 7, 8, 9])), 45)

    # strrev

    def test_strrev_empty(self) -> None:
        self.assertEqual(strrev(''), '')

    def test_strrev_T(self) -> None:
        self.assertEqual(strrev('T'), 'T')

    def test_strrev_Th(self) -> None:
        self.assertEqual(strrev('Th'), 'hT')

    def test_strrev_fox(self) -> None:
        self.assertEqual(strrev('The quick brown fox'), 'xof nworb kciuq ehT')

    # gcd

    def test_gcd_10_7(self) -> None:
        self.assertEqual(gcd(10, 7), 1)

    def test_gcd_10_10(self) -> None:
        self.assertEqual(gcd(10, 10), 10)
    
    def test_gcd_14_11(self) -> None:
        self.assertEqual(gcd(14, 11), 1)

    def test_gcd_20_42(self) -> None:
        self.assertEqual(gcd(20, 42), 2)

    def test_gcd_42_20(self) -> None:
        self.assertEqual(gcd(42, 20), 2)

    def test_gcd_20_100(self) -> None:
        self.assertEqual(gcd(20, 100), 20)

    def test_gcd_100_20(self) -> None:
        self.assertEqual(gcd(100, 20), 20)

    def test_gcd_36_8(self) -> None:    
        self.assertEqual(gcd(36, 8), 4)

    def test_gcd_8103_243(self) -> None:
        self.assertEqual(gcd(8103, 243), 3)

    def test_gcd_243_8100(self) -> None:
        self.assertEqual(gcd(243, 8100), 81)

    def test_gcd_23000_1(self) -> None:
        self.assertEqual(gcd(23000, 1), 1)

    def test_gcd_1_23000(self) -> None:    
        self.assertEqual(gcd(1, 23000), 1)

    def test_gcd_9781_0(self) -> None:
        self.assertEqual(gcd(9781, 0), 9781)

    def test_gcd_0_9781(self) -> None:
        self.assertEqual(gcd(0, 9781), 9781)

    def test_gcd_9781_n1(self) -> None:    
        self.assertEqual(gcd(9781, -1), 1)

    def test_gcd_n1_9781(self) -> None:
        self.assertEqual(gcd(-1, 9781), 1)

    def test_gcd_0_n1(self) -> None:
        self.assertEqual(gcd(0, -1), 1)

    def test_gcd_n243_n8100(self) -> None:
        self.assertEqual(gcd(-243, -8100), 81)

    # exp

    def test_exp_2_0(self) -> None:
        self.assertEqual(exp(2, 0), 1)

    def test_exp_2_1(self) -> None:
        self.assertEqual(exp(2, 1), 2)

    def test_exp_2_10(self) -> None:
        self.assertEqual(exp(2, 10), 1024)

    # Near to max recursion depth
    def test_exp_2_996(self) -> None:
        self.assertEqual(exp(2, 900), 8452712498170643941637436558664265704301557216577944354047371344426782440907597751590676094202515006314790319892114058862117560952042968596008623655407033230534186943984081346699704282822823056848387726531379014466368452684024987821414350380272583623832617294363807973376)

    # Make sure it handles a base that isn't 2
    def test_exp_3_5(self) -> None:
        self.assertEqual(exp(3, 5), 243)

    # Negative exponent
    def test_exp_2_n1(self) -> None:
        self.assertEqual(exp(2, -1), 0.5)

    # fastexp

    def test_fastexp_2_0(self) -> None:
        self.assertEqual(fastexp(2, 0), 1)

    def test_fastexp_2_1(self) -> None:
        self.assertEqual(fastexp(2, 1), 2)

    def test_fastexp_2_10(self) -> None:
        self.assertEqual(fastexp(2, 10), 1024)

    # Not near to max recursion depth with fastexp, but check it anyway
    def test_fastexp_2_996(self) -> None:
        self.assertEqual(fastexp(2, 900), 8452712498170643941637436558664265704301557216577944354047371344426782440907597751590676094202515006314790319892114058862117560952042968596008623655407033230534186943984081346699704282822823056848387726531379014466368452684024987821414350380272583623832617294363807973376)

    # Make sure it handles a base that isn't 2
    def test_fastexp_3_5(self) -> None:
        self.assertEqual(fastexp(3, 5), 243)

    # Negative exponent
    def test_fastexp_2_n1(self) -> None:
        self.assertEqual(fastexp(2, -1), 0.5)

    # baseconv

    def test_baseconv_single_digit(self) -> None:
        self.assertEqual(baseconv(1, 2), '1')

    def test_baseconv_num_eq_base(self) -> None:
        self.assertEqual(baseconv(2, 2), '10')

    def test_baseconv_256_10(self) -> None:
        self.assertEqual(baseconv(256, 10), '256')

    def test_baseconv_256_16(self) -> None:
        self.assertEqual(baseconv(256, 16), '100')

    def test_baseconv_256_2(self) -> None:
        self.assertEqual(baseconv(256, 2), '100000000')

    def test_baseconv_255_10(self) -> None:
        self.assertEqual(baseconv(255, 10), '255')

    def test_baseconv_255_16(self) -> None:
        self.assertEqual(baseconv(255, 16), 'ff')

    def test_baseconv_255_2(self) -> None:
        self.assertEqual(baseconv(255, 2), '11111111')

    # Check precondition: base too small
    def test_baseconv_255_0(self) -> None:
        with self.assertRaises(AssertionError):
            baseconv(255, 0)

    # Check precondition: base too big
    def test_baseconv_255_37(self) -> None:
        with self.assertRaises(AssertionError):
            baseconv(255, 37)

    # Fibonacci
    def test_slowfib(self) -> None:
        # Limited by speed. n == 40 is already a couple of minutes.
        maxfib = 15 
        fibs: List[int] = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34,
                55, 89, 144]
        for i in range(len(fibs), maxfib):
            fibs.append(fibs[i-1] + fibs[i-2])
        for i in range(len(fibs)):
            with self.subTest(i=i):
                self.assertEqual(slowfib(i), fibs[i])

    def test_fastfib(self) -> None:
        # Limited by recursion depth, not speed
        maxfib = 950 
        fibs: List[int] = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34,
                55, 89, 144]
        for i in range(len(fibs), maxfib):
            fibs.append(fibs[i-1] + fibs[i-2])
        for i in range(len(fibs)):
            with self.subTest(i=i):
                self.assertEqual(fib(i), fibs[i])

    def test_hanoi(self) -> None:
        move_tower(4, "A", "B", "C")

    # Graphical recursions

    def test_tree(self) -> None:
        draw_tree()

if __name__ == '__main__':
    unittest.main()