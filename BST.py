from typing import cast, List, Optional, TypeVar
from BinTree import BinTree

T = TypeVar('T') # Must support comparisons

class BST(BinTree[T]):
    """Class to represent a binary search tree.
    This class does not represent the empty tree;
    that is, a binary search tree must *always*
    have at least one node."""

    def __init__(self, data: T, parent: Optional['BST[T]'] = None):
        """Create a BST node with the given DATA and PARENT.
        Note that DATA cannot be None."""
        super().__init__(data)
        self._parent: Optional[BST[T]] = parent
        assert self._invariant()

    def _invariant(self) -> bool:
        """Class invariant."""
        valid: bool = super()._invariant()
        valid = valid and self._data is not None
        if self.hasLeftChild():
            # Must be a BST, not just a BinTree
            valid = valid and isinstance(self.leftChild(), BST)

            # Child's parent link is correct
            valid = valid and self == self.leftChild().parent()
            
            # Maximum value in the left subtree < this node's data
            maxLeftNode: BST[T] = self.leftChild()
            while maxLeftNode.hasRightChild():
                maxLeftNode = maxLeftNode.rightChild()
            valid = valid and maxLeftNode.data() < self.data() # type: ignore

            # Left subtree is a BST
            valid = valid and self.leftChild()._invariant()
            
        if self.hasRightChild():
            # Must be a BST, not just a BinTree
            valid = valid and isinstance(self.rightChild(), BST)

            # Child's parent link is correct
            valid = valid and self == self.rightChild().parent()

            # Minimum value in the right subtree > this node's data
            minRightNode: BST[T] = self.rightChild()
            while minRightNode.hasLeftChild():
                minRightNode = minRightNode.leftChild()
            valid = valid and minRightNode.data() > self.data() # type: ignore

            # Right subtree is a BST
            valid = valid and self.rightChild()._invariant()
        return valid

    # Query methods are all the same as in BinTree, except...
    def isRoot(self) -> bool:
        """If the node has no parent, it's the root."""
        return self._parent is None

    def parent(self) -> 'BST[T]':
        """Return the node's parent."""
        # Pre:
        assert not self.isRoot()
        return cast(BST[T], self._parent)

    def __contains__(self, value: T) -> bool:
        """Boolean method to figure out whether or not a given VALUE is
        in the tree rooted at SELF.  This method overloads the 'in'
        operator."""
        inTree: bool = False
        if value == self.data():
            inTree = True
        elif value < self.data(): # type: ignore
            if self.hasLeftChild():
                inTree = value in cast(BST[T], self.leftChild())
            # If no left child, inTree will stay False
        elif value > self.data(): # type: ignore
            if self.hasRightChild():
                inTree = value in cast(BST[T], self.rightChild())
            # If no right child, inTree will stay False
        return inTree

    def findSuccessor(self) -> T:
        """Find the value held by this node's successor in an
        inorder traversal.  Note that the only time we care about this
        is if this node has a right child.

        If a node N has a right child C, then the successor of N (call
        it S) is somewhere in N's right subtree.  We know that the
        value of S > the value of N (write that S > N), and that S
        holds the *least* value in the tree for which S > N.  If S is
        *not* in N's right subtree, then S must be above N in the
        tree.  Now, for S to be above N in the tree, then N has to be
        the greatest node in S's left subtree.  But if N has a right
        child C, then C > N *and* C is in S's left subtree, so N can't
        be the greatest node in S's left subtree.  Therefore, if N has
        a right child, S is *not* above N, which means S is in N's right
        subtree.  In fact, since S is the smallest node in the tree for
        which S > N, S must be the smallest node in N's right subtree.

        Note also that S cannot have two children if it is the smallest
        node in N's right subtree.  If S had two children, it would have
        to have a left child L, with L < S.  But L is still in N's right
        subtree, so then S wouldn't be the smallest node in N's right
        subtree.  So S has at most one child (it may have a right child)."""
        # Pre:
        assert self.hasRightChild()
        # The successor node S is named succNode here
        succNode: BST[T] = self.rightChild()
        # Follow down S's left subtree to find the smallest node in N's
        # right subtree
        while succNode.hasLeftChild():
            succNode = succNode.leftChild()
          
        # Now, we want the value rather than the node.
        return succNode.data()
    
    # Mutator methods
    def add(self, value: T) -> None:
        """Add a value to the tree, inserting in its proper place."""
        if value < self.data(): # type: ignore
            if self.hasLeftChild(): # Recursive 
                cast(BST[T], self.leftChild()).add(value)
            else:
                self._left = BST[T](value, self)
        elif value > self.data(): # type: ignore
            if self.hasRightChild(): # Recursive 
                cast(BST[T], self.rightChild()).add(value)
            else:
                self._right = BST[T](value, self)
        # Elif value == self.data(), don't re-insert it.
        assert self._invariant()

    def remove(self, value: T) -> None:
        """Function to remove the given VALUE from the tree.
        The tricky part here is making sure to preserve the
        BST property of the tree.  Raise a ValueError if VALUE
        is not present."""
        if value < self.data(): # type: ignore
            # Check the left subtree, if it exists
            if self.hasLeftChild():
                cast(BST[T], self.leftChild()).remove(value)
            else: # No subtree, value isn't here
                raise ValueError('Value ' + str(value) + ' not in tree')
        elif value > self.data(): # type: ignore
            # Check the right subtree, if it exists
            if self.hasRightChild():
                cast(BST[T], self.rightChild()).remove(value)
            else: # No subtree, value isn't here
                raise ValueError('Value ' + str(value) + ' not in tree')
        else: # value == self.data(), remove this node
            # Simple case: this node has no children
            # Just remove it.
            if (not self.hasLeftChild()) and (not self.hasRightChild()):
                if self.isRoot():
                    raise ValueError('Cannot delete the last node in the tree.')
                elif self == self.parent().leftChild():
                    self.parent()._left = None
                elif self == self.parent().rightChild():
                    self.parent()._right = None
            # Slightly less simple case: this node has one child
            # Copy up this node's child in place of this node
            elif (not self.hasLeftChild()) or (not self.hasRightChild()):
                if self.hasLeftChild():
                    child: BST[T] = self.leftChild()
                else:
                    child = self.rightChild()
                # Copy the data from the child up to this node
                self._data = child._data
                self._left = child._left
                self._right = child._right
            # Two children.  This one's complicated.
            # Copy this node's successor to this node, and remove
            #     the successor from this node's right subtree
            else: 
                successor: T = self.findSuccessor()
                self._data = successor
                # Remove it from the right subtree
                self.rightChild().remove(successor)
                
                    
                 


def main(args:List[str]) -> int:
    # Do nothing, successfully

    # Conventional return value indicating successful completion
    return 0

if __name__ == '__main__':
    import sys
    main(sys.argv)
