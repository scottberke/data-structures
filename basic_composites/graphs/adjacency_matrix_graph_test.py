import unittest
from io import StringIO
from contextlib import *
import random
from adjacency_matrix_graph import *

class AdjacencyMatrixTest(unittest.TestCase):
    # Helpers
    def matrix_helper(self):
        matrix = [  [0, 1, 2, 1, 2],
                    [1, 0, 1, 1, 2],
                    [1, 3, 0, 1, 3],
                    [1, 1, 2, 0, 1],
                    [1, 1, 1, 1, 0] ]
        return matrix

    # Tests
    def test_create_graph(self):
        num_nodes = random.randint(1,10)
        matrix = AdjacencyMatrix(num_nodes)
        self.assertIsInstance(
            matrix, AdjacencyMatrix
        )
        self.assertTrue(
            matrix.nodes == num_nodes
        )

    def test_create_graph_invalid_nodes(self):
        with self.assertRaises(AttributeError) as error:
            matrix = AdjacencyMatrix(0)

        self.assertEqual(
            str(error.exception),
            "Graph must have at least one node"
        )

    def test_add_edge(self):
        matrix = AdjacencyMatrix(5)
        nodes = self.matrix_helper()
        node = nodes[0] # [0, 1, 2, 1, 2]
        for index, weight in enumerate(node):
            matrix.add_edge(0, index, weight)

        self.assertEqual(
            matrix.matrix[0],
            node
        )

    def test_print_graph(self):
        # Create matrix and add edges
        matrix = AdjacencyMatrix(5)
        nodes = self.matrix_helper()
        for n_index, node in enumerate(nodes):
            for e_index, edge in enumerate(node):
                matrix.add_edge(n_index, e_index, nodes[n_index][e_index])

        # Build expected out
        expected = ""
        for node in nodes:
            expected += (str(node) + "\n")
        expected += "\n"

        # Capture output and assert
        out = StringIO()
        with redirect_stdout(out):
            print(matrix)

        self.assertEqual(
            out.getvalue(),
            expected
        )


if __name__ == "__main__":
    unittest.main()
