from tree import *

class BinarySearchTree():
    def __init__(self, root=None):
        """
        Input:
            root (node) = Root node of the tree
        Output:
            BinarySearchTree
        """
        self.__root = root

    def insert_node(self, current_node, node):
        """
        Input:
            current_node (node) = Node to insert after
            node (node) = Node being inserted
        Output:
        """
        if node.data < current_node.data:
            if current_node.left:
                self.insert_node(current_node.left, node)
            else:
                current_node.left = node
        else:
            if current_node.right:
                self.insert_node(current_node.right, node)
            else:
                current_node.right = node

    def insert(self, data):
        """
        Input:
            data (Node) = Node to be inserted into the tree
        Output:
        """
        node = self.handle_data(data)
        if not self.__root:
            self.__root = node
        else:
            self.insert_node(self.__root, node)

    def find(self, data):
        """
        Input:
            data (Node) = Node to find in the tree
        Output:
            Node = Node being retrieved
        """
        return self.find_node(self.__root, data)

    def find_node(self, current_node, data):
        """
        Input:
            current_node (Node) = Node currently serving as root of tree or subtree
            data (Node) = Node to find in the tree
        Output:
        """
        if current_node.data == data:
            return current_node.data

        if current_node.data > data:
            if current_node.left:
                return self.find_node(current_node.left, data)
            else:
                return False
        else:
            if current_node.right:
                return self.find_node(current_node.right, data)
            else:
                return False

# TODO
# Deletion
# Verification

    @property
    def root(self):
        return self.__root

    @root.setter
    def root(self, data):
        if self.__root:
            raise AttributeError("Root node already exists. Overwriting root destroys tree")

        self.__root = self.handle_data(data)

    def handle_data(self, data):
        if type(data) == Node:
            return data
        else:
            node = Node(data)
            return node
