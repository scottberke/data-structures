
class Node():
    def __init__(self, value, balance_factor=0, height=0, left=None, right=None):
        self.value = value
        self.balance_factor = balance_factor
        self.height = height
        self.left = left
        self.right = right

class AVLTree():
    def __init__(self):
        self.node_count = 0
        self.root = None

    def find(self, value, root):
        if not root:
            return False

        if value < root.value:
            return self.find(value, root.left)
        elif value > root.value:
            return self.find(value, root.right)
        elif value == root.value:
            return root.value


    def insert(self, value):
        if not self.find(value, self.root):
            self.root = self.insert_node(self.root, value)
            self.node_count += 1
            return True

        return False

    def insert_node(self, root, value):
        if not root:
            return Node(value)

        if root.value > value:
            root.left = self.insert_node(root.left, value)
        else:
            root.right = self.insert_node(root.right, value)

        self.update(root)
        return self.balance(root)

    def update(self, node):
        left_height = node.left.height if node.left else -1
        right_height = node.right.height if node.right else -1

        node.height = 1 + max(left_height, right_height)
        node.balance_factor = right_height - left_height

    def balance(self, node):
        # Left leaning subtree
        if node.balance_factor == -2:
            if node.left.balance_factor <= 0:
                return self.left_left_case(node)
            else:
                return self.left_right_case(node)
        # Right leaning subtree
        elif node.balance_factor == 2:
            if node.right.balance_factor >=0:
                return self.right_right_case(node)
            else:
                return self.right_left_case(node)
        # Balanced subtree since balance_factor in [-1, 0, 1]
        return node

    def left_left_case(self, node):
        return self.right_rotation(node)

    def left_right_case(self, node):
        node.left = self.left_rotation(node.left)
        return self.left_left_case(node)

    def right_right_case(self, node):
        return self.left_rotation(node)

    def right_left_case(self, node):
        node.right = self.right_rotation(node.right)
        return self.right_right_case(node)

    def right_rotation(self, node):
        node_left = node.left
        node.left = node_left.right
        node_left.right = node

        self.update(node)
        self.update(node_left)
        return node_left

    def left_rotation(self, node):
        node_right = node.right
        node.right = node_right.left
        node_right.left = node

        self.update(node)
        self.update(node_right)
        return node_right
