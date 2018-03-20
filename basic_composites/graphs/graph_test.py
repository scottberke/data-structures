import unittest
from io import StringIO
from contextlib import *
from graph import *

class GraphTest(unittest.TestCase):
    # Helpers

    # Tests
    def test_create_graph(self):
        graph = Graph()
        self.assertIsInstance(
            graph, Graph
        )

    def test_add_node(self):
        graph = Graph()
        node = Node(0)
        graph.add_node(node)

        self.assertTrue(
            node in graph.nodes
        )

    def test_fetch_node(self):
        graph = Graph()
        node = Node(0)
        graph.add_node(node)

        self.assertEqual(
            graph.fetch_node(node),
            node
        )

    def test_fetch_node_not_in_graph(self):
        graph = Graph()
        node = Node(0)
        with self.assertRaises(ValueError) as error:
            graph.fetch_node(node)

        self.assertEqual(
            str(error.exception),
            "Node not in graph"
        )

    def test_add_edge(self):
        # Create graph and nodes
        graph = Graph()
        first_node = Node(0)
        second_node = Node(1)
        # Add nodes to graph
        graph.add_node(first_node)
        graph.add_node(second_node)
        # Add edge between first_node and second_node
        graph.add_edge(first_node, second_node)
        # Second node should be in first nodes edges
        self.assertTrue(
            second_node in first_node.edges
        )

    def test_add_edge_w_src_node_not_in_graph(self):
        graph = Graph()
        src_node = Node(0)
        dest_node = Node(1)
        graph.add_node(dest_node)
        with self.assertRaises(ValueError) as error:
            graph.add_edge(src_node, dest_node)

        self.assertEqual(
            str(error.exception),
            "Node not in graph"
        )

    def test_add_edge_w_dest_node_not_in_graph(self):
        graph = Graph()
        src_node = Node(0)
        dest_node = Node(1)
        graph.add_node(src_node)
        with self.assertRaises(ValueError) as error:
            graph.add_edge(src_node, dest_node)

        self.assertEqual(
            str(error.exception),
            "Node not in graph"
        )

    def test_print_graph(self):
        # Create graph and nodes
        graph = Graph()
        first_node = Node(0)
        second_node = Node(1)
        # Add nodes to graph
        graph.add_node(first_node)
        graph.add_node(second_node)
        # Add edge between first_node and second_node
        graph.add_edge(first_node, second_node)
        # Expected print output includes return
        expected = str({0: [1]}) + "\n"

        # Capture output and assert
        out = StringIO()
        with redirect_stdout(out):
            print(first_node)
        self.assertEqual(
            out.getvalue(),
            expected
        )


class NodeTest(unittest.TestCase):
    # Helpers

    # Tests
    def test_create_node(self):
        node = Node()
        self.assertIsInstance(
            node, Node
        )

    def test_add_edge(self):
        # Create nodes
        first_node = Node(0)
        second_node = Node(1)
        # Add second_node as edge to first_node
        first_node.add_edge(second_node)
        # Second node should be in first nodes edges
        self.assertTrue(
            second_node in first_node.edges
        )

    def test_print_node(self):
        # Create nodes and add second as edge to first
        first_node = Node(0)
        second_node = Node(1)
        first_node.add_edge(second_node)
        # Expected print output includes return
        expected = str({0: [1]}) + "\n"
        # Capture output and assert
        out = StringIO()
        with redirect_stdout(out):
            print(first_node)
        self.assertEqual(
            out.getvalue(),
            expected
        )

if __name__ == "__main__":
    unittest.main()
