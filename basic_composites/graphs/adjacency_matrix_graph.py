class AdjacencyMatrix():
    def __init__(self, nodes):
        """
        Input:
            nodes (int) = Integer representing number of nodes for the matrix
        Output:
            AdjacencyMatrix
        Ex:
            AdjacencyMatrix(2) => AdjacencyMatrix
        """
        if nodes <= 0:
            raise AttributeError("Graph must have at least one node")
        self.nodes = nodes
        self.matrix = [ [None] * nodes for i in range(nodes) ]

    def add_edge(self, src, dest, weight=None):
        """
        Input:
            src (int) = Integer representing source node
            dest (int) = Integer representing destination node
            weight (int) = Integer representing weight from source to destination
                          Defaults to 0 if no weight provided
        Output:
            True if success
        """
        if src >= self.nodes or dest >= self.nodes:
            raise AttributeError("Edge beyond matrix size")

        self.matrix[src][dest] = weight
        return True

    def __str__(self):
        matrix = ""
        for node in self.matrix:
            matrix += (str(node) + "\n")
        return matrix
