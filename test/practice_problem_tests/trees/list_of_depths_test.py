import unittest
import math
import random

from data_structures.basic_composites.trees.tree import *
from practice_problems.trees.list_of_depths import *

class ListOfDepthsTest(unittest.TestCase):
    # Helpers
    def create_tree(self, nodes):
        """
        Helper method to take an array and turn it into a binary tree
        Input:
            nodes (arr) = array of values to be used for the tree nodes
        Ouput:
            Node = root node of the tree
        """
        if not nodes:
            return

        root_index = len(nodes) // 2
        root_val = nodes[root_index]
        root = Node(root_val)

        root.left = self.create_tree(nodes[:root_index])
        root.right = self.create_tree(nodes[root_index + 1:])

        return root

    def expected_levels_in_tree(self, num_of_nodes):
        """
        Helper to calculate number of levels in binary tree based on the number
        of nodes in the tree.
        The minimum height of a binary tree with n nodes is log(n + 1)

        Input:
            num_of_nodes (int) = Number of nodes in the binary tree
        Output:
            int = Number of levels in binary tree
        """
        return math.ceil(math.log2(num_of_nodes + 1))

    # Tests
    def test_linked_list_depths_empty_tree(self):
        nodes = []
        tree = self.create_tree(nodes)
        tree_levels_as_linked_lists_array = list_of_depths(tree)

        self.assertFalse(
            tree_levels_as_linked_lists_array
        )

    def test_list_of_depths_simple_3_nodes(self):
        nodes = [1, 2, 3]
        tree = self.create_tree(nodes)
        tree_levels_as_linked_lists_array = list_of_depths(tree)

        self.assertEqual(
            len(tree_levels_as_linked_lists_array),
            self.expected_levels_in_tree(len(nodes))
        )

        for index, linked_list in enumerate(tree_levels_as_linked_lists_array):
            self.assertEqual(
                linked_list.size,
                2**index
            )

    def test_list_of_depths_simple_4_nodes(self):
        nodes = [1, 2, 3, 4]
        tree = self.create_tree(nodes)
        tree_levels_as_linked_lists_array = list_of_depths(tree)
    
        self.assertEqual(
            len(tree_levels_as_linked_lists_array),
            self.expected_levels_in_tree(len(nodes))
        )
        # Verify that each linked list has the expected size
        self.assertEqual(
            tree_levels_as_linked_lists_array[0].size,
            1
        )

        self.assertEqual(
            tree_levels_as_linked_lists_array[1].size,
            2
        )

        self.assertEqual(
            tree_levels_as_linked_lists_array[2].size,
            1
        )

    def test_list_of_depths_arbitrary_nodes(self):
        nodes = list(range(1, random.randrange(0, 30)))
        tree = self.create_tree(nodes)
        tree_levels_as_linked_lists_array = list_of_depths(tree)

        self.assertEqual(
            len(tree_levels_as_linked_lists_array),
            self.expected_levels_in_tree(len(nodes))
        )

        # Exclude the last linked list since I'm not sure how to calculate the
        # number of expected nodes in an incomplete binary tree at the last level
        for index, linked_list in enumerate(tree_levels_as_linked_lists_array[:-1]):
            self.assertEqual(
                linked_list.size,
                2**index
            )


if __name__ == "__main__":
    unittest.main()
