# Tree Node
# Value
# Children:[]
# There is a limit to how many children you can have
# Binary Search Tree
# - Only two children max - left child and right child

"""
Binary search trees are a data structure that enforce an ordering over
the data they store. That ordering in turn makes it a lot more efficient
at searching for a particular piece of data in the tree.

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # take the current value of our node (self.value)
        # compare to the new value we want to insert

        # if new value < self.value
        # IF self.left is already taken by a node,
        # make that (left)  node, call insert
        # set the left to the new node with the new value

        # if new value >= self.value
        # IF self.right is already taken by a node
        # make that (right) node call insert
        # set the right child to the new node with new value

        pass

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        # compare the target to current value
        # if current value >= target
        found = False
        if self.value < target:
            # check the left subtree
            # if you cannot go left, return false
            if self.left is None:
                return False
            found = self.left.contains(target)

        # if current value >= target
        if self.value >= target:
            # check if right subtree contains target
            # if you cannot go right, return false
            if self.right is None:
                return False
            found = self.right.contains(target)

        return found
