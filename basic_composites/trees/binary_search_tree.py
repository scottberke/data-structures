class Node():
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BinarySearchTree():
    def __init__(self, root=None):
        self.__root = root

    def insert_node(self, current_node, node):
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
        node = self.handle_data(data)
        if not self.__root:
            self.__root = node
        else:
            self.insert_node(self.__root, node)

    def find(self, data):
        return self.find_node(self.__root, data)

    def find_node(self, current_node, data):
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
