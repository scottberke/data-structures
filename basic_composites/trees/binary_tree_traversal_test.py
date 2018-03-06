import unittest
from io import StringIO
from contextlib import *

from binary_search_tree import *
from binary_tree_traversal import *

class BinaryTreeTraversalTest(unittest.TestCase):
    # Helpers
    def create_tree(self):
       # Lets create this tree:
       #         50
       #       /   \
       #     30    70
       #   /  \   /  \
       # 20   40 60  80
        nodes = [50, 30, 20, 40, 70, 60, 80]
        bst = BinarySearchTree()
        for node in nodes:
            bst.insert(node)
        return bst

    def test_in_order_traversal(self):
        bst = self.create_tree()
        # Expected node order as output should appear
        nodes_in_order = [20, 30, 40, 50, 60, 70, 80]
        n = "\n"
        expected = n.join(str(i) for i in nodes_in_order) + n
        # Capture output of in_order_traversal
        out = StringIO()
        with redirect_stdout(out):
            in_order_traversal(bst.root)
        self.assertEqual(
            out.getvalue(),
            expected
        )

    def test_pre_order_traversal(self):
        bst = self.create_tree()
        # Expected node order as output should appear
        nodes_in_order = [50, 30, 20, 40, 70, 60, 80]
        n = "\n"
        expected = n.join(str(i) for i in nodes_in_order) + n
        # Capture output of in_order_traversal
        out = StringIO()
        with redirect_stdout(out):
            pre_order_traversal(bst.root)
        self.assertEqual(
            out.getvalue(),
            expected
        )


    def test_post_order_traversal(self):
        bst = self.create_tree()
        # Expected node order as output should appear
        nodes_in_order = [20, 40, 30, 60, 80, 70, 50]
        n = "\n"
        expected = n.join(str(i) for i in nodes_in_order) + n
        # Capture output of in_order_traversal
        out = StringIO()
        with redirect_stdout(out):
            post_order_traversal(bst.root)
        self.assertEqual(
            out.getvalue(),
            expected
        )

if __name__ == "__main__":
    unittest.main()
