import unittest
import random

from data_structures.basic_composites.trees.tree import *
from practice_problems.trees.check_balanced import *

class CheckBalancedTest(unittest.TestCase):
    # Helpers
    def create_tree(self, nodes, balanced=True):
        """
        Helper method to take an array and turn it into a binary tree
        Input:
            nodes (arr) = array of values to be used for the tree nodes
        Ouput:
            Node = root node of the tree
        """
        if not nodes:
            return

        mid_point = 2 if balanced else 0

        root_index = len(nodes) // mid_point if mid_point else mid_point
        root_val = nodes[root_index]
        root = Node(root_val)

        root.left = self.create_tree(nodes[:root_index])
        root.right = self.create_tree(nodes[root_index + 1:])

        return root


    # Tests
    def test_checked_balanced_tree_simple_true(self):
        nodes = [1, 2, 3]
        tree = self.create_tree(nodes, balanced=True)
        self.assertTrue(
            check_balanced(tree)
        )

    def test_checked_balanced_tree_simple_false(self):
        nodes = [1, 2, 3]
        tree = self.create_tree(nodes, balanced=False)
        self.assertFalse(
            check_balanced(tree)
        )

    def test_check_balanced_tree_empty(self):
        nodes = []
        tree = self.create_tree(nodes)

        self.assertTrue(
            check_balanced(tree)
        )

    def test_check_balanced_tree_arbitrary_true(self):
        nodes = list(range(1, random.randrange(0, 30)))
        tree =  self.create_tree(nodes, balanced=True)

        self.assertTrue(
            check_balanced(tree)
        )

    def test_check_balanced_tree_arbitrary_false(self):
        nodes = list(range(0, random.randrange(5, 50)))
        tree =  self.create_tree(nodes, balanced=False)

        self.assertFalse(
            check_balanced(tree)
        )


if __name__ == "__main__":
    unittest.main()
