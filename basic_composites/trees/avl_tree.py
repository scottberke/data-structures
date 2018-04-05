
class Node():
    def __init__(self, value):
        """
        Input:
            (object) = To be assigned as value for the node. Must be a comparable
        Output:
        """
        self.value = value
        self.balance_factor = 0
        self.height = 0
        self.left = None
        self.right = None

class AVLTree():
    def __init__(self):
        self.node_count = 0
        self.root = None

    def find(self, value, root):
        """
        Input:
            (object) = Value to search for
            (node) = Node to start searcing from
        Output:
        """
        # If we don't get a root then we're at a leaf or terminating point
        if not root:
            return False
        # Search left if values lower than root, otherwise search right
        if value < root.value:
            return self.find(value, root.left)
        elif value > root.value:
            return self.find(value, root.right)
        elif value == root.value:
            return root.value

    def insert(self, value):
        """
        Input:
            (object) = Value to insert into the AVL. Must be a comparable type
        Output:
            True || False = True if success on insert, False otherwise
        """
        # Only insert unique values into the tree
        if not self.find(value, self.root):
            # Root will bubble up as whats returned
            self.root = self.insert_node(self.root, value)
            # Keep track of node count
            self.node_count += 1
            return True

        return False

    def insert_node(self, root, value):
        """
        Input:
            (node) = Node under which the value should be inserted into the tree
            (object) = Value of new node to be inserted. Must be compbarable type
        Output:
            (node) = Node under which the new node was inserted
        """
        # If theres None type root passed in, return new node as root
        if not root:
            return Node(value)

        # Insert to the left if values < root, insert right otherwise
        if root.value > value:
            # Rerusively insert into correct side, setting child to new parent
            root.left = self.insert_node(root.left, value)
        else:
            root.right = self.insert_node(root.right, value)
        # Root needs to have stats updated
        self.update(root)
        # Root also needs to be balanced after inser
        return self.balance(root)

    def update(self, node):
        """
        Input:
            (node) = Node to have stats updated on
        Output:
            None
        """
        # Find children heights, default to -1 if none
        left_height = node.left.height if node.left else -1
        right_height = node.right.height if node.right else -1

        # Current nodes height is max of children + 1
        # +1 here balances out -1 default from above
        node.height = 1 + max(left_height, right_height)
        # Set current nodes balance factor
        node.balance_factor = right_height - left_height

    def balance(self, node):
        """
        Input:
            (node) = Root node to balance from
        Output:
            (node) = Node that was balanced last
        """
        # Left leaning subtree has -2 balance_factor
        if node.balance_factor == -2:
            # Left left case has negative child balance factor
            if node.left.balance_factor <= 0:
                return self.left_left_case(node)
            else:
                # Left right case has positive balance factor
                return self.left_right_case(node)
        # Right leaning subtree has +2 balance factor
        elif node.balance_factor == 2:
            # Right right case has positive balance factor
            if node.right.balance_factor >=0:
                return self.right_right_case(node)
            else:
                # Right left case has negative balance factor
                return self.right_left_case(node)
        # Balanced subtree since balance_factor in [-1, 0, 1]
        return node

    def left_left_case(self, node):
        """
        Input:
            (node) = node to be balanced
        Output:
            (node) = New root of tree/subtree after rotation
        """
        # Left leaning needs right rotation
        return self.right_rotation(node)

    def left_right_case(self, node):
        """
        Input:
            (node) = node to be balanced
        Output:
            (node) = New root of tree/subtree after rotation
        """
        # Left right needs left rotation followed by right rotation
        node.left = self.left_rotation(node.left)
        return self.left_left_case(node)

    def right_right_case(self, node):
        """
        Input:
            (node) = node to be balanced
        Output:
            (node) = New root of tree/subtree after rotation
        """
        # Right case needs left rotation
        return self.left_rotation(node)

    def right_left_case(self, node):
        """
        Input:
            (node) = node to be balanced
        Output:
            (node) = New root of tree/subtree after rotation
        """
        # Right left case needs right rotation followed by left rotation
        node.right = self.right_rotation(node.right)
        return self.right_right_case(node)

    def right_rotation(self, node):
        """
        Input:
            (node) = node to be balanced
        Output:
            (node) = New root of tree/subtree after rotation
        """
        # Grab pointer to roots left child
        node_left = node.left
        # Roots new left child is old lefts right child
        node.left = node_left.right
        # Old left child becomes parent of root
        node_left.right = node
        # Update both nodes stats
        self.update(node)
        self.update(node_left)
        # Return new root
        return node_left

    def left_rotation(self, node):
        """
        Input:
            (node) = node to be balanced
        Output:
            (node) = New root of tree/subtree after rotation
        """
        # Grab pointer to roots right child
        node_right = node.right
        # Roots new right child is old rights left child
        node.right = node_right.left
        # Old right child becomes parent of root
        node_right.left = node
        # Update both nodes stats
        self.update(node)
        self.update(node_right)
        # Return new root
        return node_right
