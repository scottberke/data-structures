# Source:
# https://github.com/scottberke/data-structures/blob/master/basic_composites/graphs/adjacency_matrix_graph.py

class Node():
    def __init__(self, location,  edges):
        self.location = location
        self.edges = edges


class AdjacencyMatrix():
    def __init__(self, size):
        if size <= 0:
            raise AttributeError("Graph must have at least one node")
        self.size = size
        self.matrix = [ [None] * size for i in range(size) ]
        self.nodes = {}

    def add_nodes_from_array(self, nodes):
        if len(nodes) != self.size:
            raise AttributeError("Nodes do not match matrix size")

        for node_index in range(len(nodes)):
            new_node = Node(node_index, nodes[node_index])
            self.add_node(new_node)

    def add_node(self, node):
        if len(node.edges) != self.size:
            raise AttributeError("Node does not match matrix size")

        for edge_index in range(len(node.edges)):
            self.matrix[node.location][edge_index] = node.edges[edge_index]

        self.nodes[node.location] = node

    def get_node(self, node_location):
        return self.nodes[node_location]

    def __str__(self):
        matrix = ""
        for node in self.matrix:
            matrix += (str(node) + "\n")
        return matrix
