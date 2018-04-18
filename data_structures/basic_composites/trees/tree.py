"""
An implementation of a basic node used to form a binary tree
Author: Scott Berke
"""

class Node():
    def __init__(self, data=None, left=None, right=None):
        """
        Input:
            data (node) = Data for root Node
            left (node) = Node to be inserted to the left
            right (node) = Node to be inserted to the right
        Output:
        """
        self.data = data
        self.left = left
        self.right = right
