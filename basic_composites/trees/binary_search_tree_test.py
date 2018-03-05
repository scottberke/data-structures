import unittest
from binary_search_tree import *

class TreeNodeTest(unittest.TestCase):
    def test_create_bst(self):
        bst = BinarySearchTree()
        self.assertIsInstance(
            bst, BinarySearchTree
        )

    def test_set_root_node_with_node(self):
        bst = BinarySearchTree()
        bst.root = Node("tacos")
        self.assertIsInstance(
            bst.root, Node
        )

    def test_set_root_node_with_data(self):
        bst = BinarySearchTree()
        bst.root = "tacos"
        self.assertIsInstance(
            bst.root, Node
        )

    def test_overwriting_root_node(self):
        bst = BinarySearchTree()
        bst.root = "tacos"
        with self.assertRaises(AttributeError):
            bst.root = Node("tequila")

    def test_insert_left(self):
        bst = BinarySearchTree()
        bst.root = "tacos"
        lower_val = "aaaa"
        bst.insert(lower_val)
        self.assertTrue(
            bst.root.left.data == lower_val
        )

    def test_insert_right(self):
        bst = BinarySearchTree()
        bst.root = "tacos"
        higher_val = "zzzz"
        bst.insert(higher_val)
        self.assertTrue(
            bst.root.right.data == higher_val
        )

    def test_find_node(self):
        bst = BinarySearchTree()
        bst.root = "nnn"
        nodes = "ddd aaa bbb eee ccc ooo sss ttt qqq rrr zzz".split()
        for node in nodes:
            bst.insert(node)

        found = bst.find("ccc")
        self.assertTrue(
            found == "ccc"
        )

    def test_find_node_higher(self):
        bst = BinarySearchTree()
        bst.root = "nnn"
        nodes = "ddd aaa bbb eee ccc ooo sss ttt qqq rrr zzz".split()
        for node in nodes:
            bst.insert(node)

        found = bst.find("qqq")
        self.assertTrue(
            found == "qqq"
        )

    def test_find_node_missing(self):
        bst = BinarySearchTree()
        bst.root = "nnn"
        nodes = "ddd aaa bbb eee ccc ooo sss ttt qqq rrr zzz".split()
        for node in nodes:
            bst.insert(node)

        found = bst.find("ggg")
        self.assertTrue(
            found == False
        )

if __name__ == "__main__":
    unittest.main()
