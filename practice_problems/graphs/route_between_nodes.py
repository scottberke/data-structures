import sys
sys.path.append('../../basic_composites/graphs')
from adjacency_matrix_graph import *
from collections import deque


# Container for nodes to track path
class NodeContainer():
    def __init__(self, node, position, path=None):
        self.position = position
        self.node = node
        if not path:
            self.path = []
        else:
            self.path = path

# BFS search on matrix from source to destination
def breadth_first_search(matrix, src, dest):
    if src < 0 or src >= len(matrix.matrix) or dest >= len(matrix.matrix) or dest < 0:
        raise AttributeError("Invalid nodes")

    start = matrix.matrix[src]
    start_container = NodeContainer(start, src)

    queue = deque()
    queue.append(start_container)

    while queue:
        node_container = queue.pop()
        current_node = node_container.node
        for index, edge in enumerate(current_node):
            if edge and index not in node_container.path:
                new_node_container = NodeContainer(matrix.matrix[index], index, node_container.path + [node_container.position])
                queue.appendleft(new_node_container)

                if index == dest:
                    return True

    return False
