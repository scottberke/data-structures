import pdb
class Node():
    def __init__(self, data=None):
        self.data = data
        self.edges = []

    def add_edge(self, node):
        self.edges.append(node)

    def __str__(self):
        edges = [ edge.data for edge in self.edges ]
        return str({ self.data: edges })


class Graph():
    def __init__(self, nodes=[]):
        self.nodes = nodes

    def add_node(self, node):
        self.nodes.append(node)

    def add_edge(self, src, dest):
        src.add_edge(dest)

    def __str__(self):
        graph = {}
        for node in self.nodes:
            graph[node.data] = node.edges

        return str(graph)
