class AdjacencyMatrix():
    def __init__(self, nodes):
        if nodes <= 0:
            raise AttributeError("Graph must have at least one node")
        self.nodes = nodes
        self.matrix = [ [None] * nodes for i in range(nodes) ]

    def add_edge(self, src, dest, weight=0):
        if src >= self.nodes or dest >= self.nodes:
            raise AttributeError("Edge beyond matrix size")

        self.matrix[src][dest] = weight

    def __str__(self):
        matrix = ""
        for node in self.matrix:
            matrix += (str(node) + "\n")
        return matrix
