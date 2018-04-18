#!/usr/bin/env python
"""
An implementation of a basic graph
Author: Scott Berke
"""
class Node():
    def __init__(self, data=None, edges=None):
        """
        Input:
            data (Object) = Data representing the value/name of the node
            edges (Node)  = Node to be added as edge to self
        Output:
            Node
        """
        self.data = data
        if not edges:
            self.edges = []
        else:
            self.edges = edges

    def add_edge(self, node):
        """
        Input:
            node (Node) = Node to be added as edge to self
        Output:
            True if success
        """
        self.edges.append(node)
        return True

    def __str__(self):
        edges = [ edge.data for edge in self.edges ]

        return str({ self.data: edges })


class Graph():
    def __init__(self, nodes=[]):
        """
        Input:
            nodes [(nodes)] = Array containing nodes in self
        Output:
            Graph
        """
        self.nodes = nodes

    def add_node(self, node):
        """
        Input:
            node (Node) = Node to be added to self
        Output:
            True if success
        """
        self.nodes.append(node)
        return True

    def add_edge(self, src, dest):
        """
        Input:
            src (node) = Source node in self
            dest (node) = Destination node in self
        Output:
            True if node edge is succesfully added
            Raises ValueError if either node not in graph
        """
        try:
            src = self.fetch_node(src)
            dest = self.fetch_node(dest)
            src.add_edge(dest)
        except ValueError:
            raise ValueError("Node not in graph")

        return True

    def fetch_node(self, node):
        """
        Input:
            node (node) = Node to find in self
        Output:
            Node if success
            Raises ValueError if node not in self
        """
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
