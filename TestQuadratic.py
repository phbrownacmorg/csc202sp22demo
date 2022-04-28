# Empty unit-testing class
# Peter Brown, 26 Jan 2017

import unittest
from quadratic import *

class TestNothing(unittest.TestCase):

    def test_Generic(self) -> None:
        root1, root2 = roots(1, 0, 0)
        # assertAlmostEqual to compare floats
        self.assertAlmostEqual(root1, 0)
        self.assertAlmostEqual(root2, 0)

    def testIrrational(self) -> None:
        root1, root2 = roots(0.5, 2, 1)
        self.assertAlmostEqual(root1, -0.1464466)
        self.assertAlmostEqual(root2, -0.8535534)
        
if __name__ == '__main__':
    unittest.main()