# Empty unit-testing class
# Peter Brown, 26 Jan 2017

import unittest
from BST import BST
from typing import cast, List

class TestBST(unittest.TestCase):
    def setUp(self) -> None:
        self._1node:BST[int] = BST[int](34)     #  34

        self._3nodes:BST[int] = BST[int](34)    #     34
        self._3nodes.add(47)                    #    /  \
        self._3nodes.add(31)                    #  31    47

        self._7nodes:BST[int] = BST[int](34)    #       34
        self._7nodes.add(47)                    #      /  \
        self._7nodes.add(31)                    #    31    47
        self._7nodes.add(6)                     #   /      / \
        self._7nodes.add(15)                    #  6      42  70
        self._7nodes.add(70)                    #   \
        self._7nodes.add(42)                    #    15

    def test_contains1(self) -> None:
        self.assertTrue(34 in self._1node)
        self.assertFalse(31 in self._1node)
        self.assertFalse(47 in self._1node)
        
    def test_contains3(self) -> None:
        self.assertTrue(34 in self._3nodes)
        self.assertTrue(31 in self._3nodes)
        self.assertTrue(47 in self._3nodes)
        self.assertFalse(6 in self._3nodes)
        self.assertFalse(32 in self._3nodes)
        self.assertFalse(42 in self._3nodes)
        self.assertFalse(70 in self._3nodes)

    def test_contains6(self) -> None:
        self.assertTrue(34 in self._7nodes)
        self.assertTrue(31 in self._7nodes)
        self.assertTrue(47 in self._7nodes)
        self.assertTrue(6 in self._7nodes)
        self.assertTrue(15 in self._7nodes)
        self.assertTrue(70 in self._7nodes)
        self.assertTrue(42 in self._7nodes)
        self.assertFalse(3 in self._7nodes)
        self.assertFalse(14 in self._7nodes)
        self.assertFalse(16 in self._7nodes)
        self.assertFalse(32 in self._7nodes)
        self.assertFalse(41 in self._7nodes)
        self.assertFalse(43 in self._7nodes)
        self.assertFalse(69 in self._7nodes)
        self.assertFalse(71 in self._7nodes)

    def testSuccessor(self) -> None:
        self.assertEqual(self._3nodes.findSuccessor(), 47)

        self.assertEqual(cast(BST, self._7nodes.leftChild().leftChild()).findSuccessor(), 15)
        self.assertEqual(self._7nodes.findSuccessor(), 42)
        self.assertEqual(cast(BST, self._7nodes.rightChild()).findSuccessor(), 70)

    def testRemove_1node(self) -> None:
        with self.assertRaises(ValueError):
            self._1node.remove(31)
        with self.assertRaises(ValueError):
            self._1node.remove(34)

    def test_remove_3nodes_left(self) -> None:
        self._3nodes.remove(31)
        self.assertFalse(31 in self._3nodes)                    # 31 is no longer in the tree
        self.assertEqual(self._3nodes.data(), 34)               # Root should be 34
        self.assertEqual(self._3nodes.rightChild().data(), 47)  # Right child should be 47
        self.assertEqual(len(self._3nodes), 2)                  # That should be the whole tree

    def test_remove_3nodes_right(self) -> None:
        self._3nodes.remove(47)
        self.assertFalse(47 in self._3nodes)                    # 47 is no longer in the tree
        self.assertEqual(self._3nodes.data(), 34)               # Root should be 34
        self.assertEqual(self._3nodes.leftChild().data(), 31)   # Left child should be 31
        self.assertEqual(len(self._3nodes), 2)                  # That should be the whole tree

    def test_remove_3nodes_root(self) -> None:
        self._3nodes.remove(34)
        self.assertFalse(34 in self._3nodes)                    # 34 is no longer in the tree
        self.assertEqual(self._3nodes.data(), 47)               # Root should be 47
        self.assertEqual(self._3nodes.leftChild().data(), 31)   # Left child should be 31
        self.assertEqual(len(self._3nodes), 2)                  # That should be the whole tree

    def test_remove_7nodes_left(self) -> None:
        self._7nodes.remove(31)
        self.assertFalse(31 in self._7nodes)
        self.assertEqual(self._7nodes.data(), 34)               # Root should be 34
        self.assertEqual(self._7nodes.leftChild().data(), 6)    # Left child should be 31
        self.assertEqual(self._7nodes.inorder(), cast(List[int], [6, 15, 34, 42, 47, 70]))                  # That should be the whole tree

    def test_remove_7nodes_right(self) -> None:
        self._7nodes.remove(47)
        self.assertFalse(47 in self._7nodes)
        self.assertEqual(self._7nodes.data(), 34)               # Root should be 34
        self.assertEqual(self._7nodes.rightChild().data(), 70)  # Right child should be 70
        self.assertEqual(self._7nodes.inorder(), cast(List[int], [6, 15, 31, 34, 42, 70]))                  # That should be the whole tree

    def test_remove_7nodes_root(self) -> None:
        self._7nodes.remove(34)
        self.assertFalse(34 in self._7nodes)
        self.assertEqual(self._7nodes.data(), 42)               # Root should be 42
        self.assertEqual(self._7nodes.rightChild().data(), 47)  # Right child should be 47
        self.assertEqual(self._7nodes.inorder(), cast(List[int], [6, 15, 31, 42, 47, 70]))                  # That should be the whole tree


if __name__ == '__main__':
    unittest.main()
    
