
class Node():
    def __init__(self, data=None, edges=None):
        self.data = data
        if not edges:
            self.edges = []
        else:
            self.edges = edges

    def add_edge(self, node):
        self.edges.append(node)
        return True

    def __str__(self):
        edges = [ edge.data for edge in self.edges ]

        return str({ self.data: edges })


class Graph():
    def __init__(self, nodes=[]):
        self.nodes = nodes

    def add_node(self, node):
        self.nodes.append(node)
        return True

    def add_edge(self, src, dest):
        src.add_edge(dest)
        try:
            src = self.fetch_node(src)
            dest = self.fetch_node(dest)
            src.add_edge(dest)
        except ValueError:
            raise ValueError("Node not in graph")

        return True
        try:
            index = self.nodes.index(node)
            return self.nodes[index]
        except ValueError:
            raise ValueError("Node not in graph")

    def __str__(self):
        graph = {}

        for node in self.nodes:
            graph[node.data] = node.edges

        return str(graph)
