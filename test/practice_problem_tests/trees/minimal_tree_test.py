import unittest
import math
import random

from practice_problems.trees.minimal_tree import *

class MinimalTreeTest(unittest.TestCase):
    # Helpers
    def minimal_tree_height(self, nodes):
        # Minimal height of a tree is log(n + 1) where n is the number of nodes
        min_height = math.ceil(math.log2(nodes + 1))
        return min_height

    def check_tree_height(self, tree):
        # Grab root
        root = tree.root
        # Not sure why but scoping requires I declare global here and in #traverse_tree
        global max_height
        max_height = 0

        def traverse_tree(node, count):
            # This just basically counts nodes seen until it reaches a leaf
            # max_height is updated if larger max_height is found
            global max_height
            if node:
                count += 1
                traverse_tree(node.left, count)
                traverse_tree(node.right, count)
            else:
                if count > max_height:
                    max_height = count

        traverse_tree(root, 0)
        return max_height


    # Tests
    def test_minimal_tree_simple_3(self):
        arr = [1, 2, 3]
        tree = MinTree(arr)

        self.assertEqual(
            self.minimal_tree_height(len(arr)),
            self.check_tree_height(tree)
        )

    def test_minimal_tree_simple_7(self):
        arr = [1, 2, 3, 4, 5, 6, 7]
        tree = MinTree(arr)

        self.assertEqual(
            self.minimal_tree_height(len(arr)),
            self.check_tree_height(tree)
        )


    def test_minimal_tree_simple_arbitrary(self):
        size = random.randrange(100)
        arr = sorted(random.sample(range(1, 100), size))
        tree = MinTree(arr)
        # pdb.set_trace()
        self.assertEqual(
            self.minimal_tree_height(len(arr)),
            self.check_tree_height(tree)
        )

    def test_minimal_tree_simple_empty(self):
        arr = []
        tree = MinTree(arr)

        self.assertEqual(
            self.minimal_tree_height(len(arr)),
            self.check_tree_height(tree)
        )



if __name__ == "__main__":
    unittest.main()
