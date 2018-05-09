# Considering the input is sorted, this should build the tree in O(log n) time
# since each insertion divides the input in half 

class Node():
    def __init__(self, val):
        """
        Input:
            val (int) = Integer representing node value
        Output:
            Node
        """
        self.val = val
        self.left = None
        self.right = None

class MinTree():
    def __init__(self, arr):
        """
        Input:
            arr ([int]) = Sorted unique set of integers to build tree with
        Output:
            MinTree
        """
        if arr:
            # Since arr is sorted our root will be the mid element
            root_index = len(arr) // 2
            self.root = Node(arr[root_index])
            # After setting root, build left and right side with correspnding halves
            self.build_tree(arr[:root_index], self.root)
            self.build_tree(arr[root_index+1:], self.root)
        else:
            self.root = None

    def build_tree(self, arr, root):
        """
        Input:
            arr ([int]) = Sorted unique set of integers to build tree with
            root (node) = Root to start building tree from
        Output:
            None
        """
        # No more nodes to insert if the arr is empty
        if not arr:
            return

        root_index = len(arr) // 2
        node = Node(arr[root_index])
        # Figure out which side the child root goes on
        if node.val > root.val:
            root.right = node
        else:
            root.left = node
        # Continue building tree with remaining arr
        self.build_tree(arr[:root_index], node)
        self.build_tree(arr[root_index+1:], node)
