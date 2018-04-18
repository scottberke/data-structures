import unittest
from io import StringIO
from contextlib import *
from data_structures.basic_composites.trees.avl_tree import *


class AVLTreeTest(unittest.TestCase):
    # Helpers
    def create_avl_tree(self, nodes=None):
        if not nodes:
            nodes = [6, 3, 9, 15, 20, 25]
        # Balances to:
        #           15
        #          /   \
        #         6    20
        #       /  \  /  \
        #      3   9 X   25

        avl_tree = AVLTree()
        for node in nodes:
            avl_tree.insert(node)
        return avl_tree

    # Tests
    def test_avl_tree_create(self):
        avl_tree = AVLTree()
        self.assertIsInstance(
            avl_tree,
            AVLTree
        )

    def test_avl_tree_insert_nothin(self):
        avl_tree = self.create_avl_tree()

        with self.assertRaises(TypeError):
            avl_tree.insert()


    def test_avl_tree_insert_count(self):
        avl_tree = self.create_avl_tree()

        self.assertTrue(
            avl_tree.node_count == 6
        )

    def test_avl_tree_insert_correct_root(self):
        avl_tree = self.create_avl_tree()

        self.assertEqual(
            avl_tree.root.value,
            15
        )

    def test_avl_tree_insert_correct_height(self):
        avl_tree = self.create_avl_tree()

        self.assertTrue(
            avl_tree.root.height,
            2
        )

    def test_avl_tree_insert_find_found(self):
        avl_tree = self.create_avl_tree()

        self.assertEqual(
            avl_tree.find(25, avl_tree.root),
            25
        )

    def test_avl_tree_insert_find_not_found(self):
        avl_tree = self.create_avl_tree()

        self.assertFalse(
            avl_tree.find(99, avl_tree.root)
        )


    def test_avl_node_balance_factor(self):
        avl_tree = self.create_avl_tree()

        self.assertTrue(
            avl_tree.root.balance_factor in [-1, 0, 1]
        )





if __name__ == "__main__":
    unittest.main()
