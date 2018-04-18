import unittest
from data_structures.basic_composites.trees.tree import *

class TreeNodeTest(unittest.TestCase):
    def test_create_node(self):
        node = Node()
        self.assertIsInstance(
            node, Node
        )

    def test_node_has_attrs(self):
        node = Node()
        self.assertTrue(
            node.left == None and node.right == None and node.data == None
        )

    def test_node_children(self):
        root_data = "tacos"
        left_data = "tequila"
        right_data = "whiskey"

        root = Node(root_data)
        root.left = Node(left_data)
        root.right = Node(right_data)

        self.assertTrue(
            root.data == root_data and \
            root.left.data == left_data and \
            root.right.data == right_data
        )

    def test_node_only_two_children(self):
        root_data = "tacos"
        left_data = "tequila"
        right_data = "whiskey"
        overwrite_left = "salsa"

        root = Node(root_data)
        root.left = Node(left_data)
        root.right = Node(right_data)

        self.assertTrue(
            root.left.data == left_data
        )
        root.left = Node(overwrite_left)
        self.assertTrue(
            root.left.data == overwrite_left
        )


if __name__ == "__main__":
    unittest.main()
