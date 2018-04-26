import unittest
from practice_problems.graphs.route_between_nodes import *

class RouteBetweenNodesTest(unittest.TestCase):
    # Helpers
    def create_graph(self, nodes):
        matrix = AdjacencyMatrix(len(nodes))
        matrix.add_nodes_from_array(nodes)

        return matrix

    def matrix_w_path(self):
        nodes = [   [0, 1, 0, 0, 0],    # 0 -> Start
                    [1, 0, 1, 1, 0],
                    [0, 0, 0, 1, 1],
                    [0, 1, 0, 0, 1],
                    [1, 0, 0, 0, 0] ]   # 4 -> End
        return nodes

    def matrix_wo_path(self):
        nodes = [   [0, 1, 0, 0, 0],    # 0 -> Start
                    [0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 0],
                    [0, 1, 0, 0, 0],
                    [1, 0, 0, 0, 0] ]   # 4 -> End
        return nodes

    # Tests
    def test_route_between_nodes_found(self):
        graph = self.create_graph(self.matrix_w_path())
        start = 0
        end = 4
        path_found = breadth_first_search(graph, start, end)
        self.assertTrue(
            path_found
        )

    def test_route_between_nodes_not_found(self):
        graph = self.create_graph(self.matrix_wo_path())
        start = 0
        end = 4
        path_found = breadth_first_search(graph, start, end)
        self.assertFalse(
            path_found
        )

    def test_route_between_nodes_bad_start(self):
        graph = self.create_graph(self.matrix_w_path())
        start = 5
        end = 4
        with self.assertRaises(AttributeError):
            path_found = breadth_first_search(graph, start, end)

    def test_route_between_nodes_bad_end(self):
        graph = self.create_graph(self.matrix_w_path())
        start = 0
        end = 7
        with self.assertRaises(AttributeError):
            path_found = breadth_first_search(graph, start, end)


if __name__ == "__main__":
    unittest.main()
