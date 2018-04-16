# TODO: Bubble up and down with starting index as apposed to defaulting to end/root
class MinHeap(list):
    def __init__(self):
        pass

    def peek(self):
        """
        Returns the root node of the heap with keeping structure intact

        Input:
        Output:
            (object) = Value at root of the heap
        """
        return self[0]

    def insert(self, item):
        """
        Adds item to the heap and then rebalances the heap so heap properties
        are kept intact

        Input:
            (object) = Object to be inserted into the heap
        Output:
        """
        self.append(item)
        self.bubble_up()

    def poll(self):
        """
        Removes the root node from the heap and rebalances the heap so heap
        properties are kept intact

        Input:
        Output:
            (object) = Value that was at the root node
        """
        if len(self):
            self[0], self[-1] = self[-1], self[0]
        polled = self.pop()
        self.bubble_down()
        return polled

    def children(self, node_index):
        """
        Returns an array of the provided nodes children indices.
        Children nodes of an index are at:
        2*node_index + 1 and 2*node_index + 2

        Input:
            (int) = Int of the node that you would like to see children indices of
        Output:
            [(int)] = Array of integers that represent the indices of children nodes
        """
        children = []
        # Children of node @ 2*node_index + 1 and 2*node_index + 2
        for i in [1, 2]:
            child_index = (2 * node_index) + i
            if child_index < len(self):
                children.append(child_index)
        return children

    def bubble_up(self):
        """
        Used to rebalance the heap when a node is added to the last position
        in the heap. Checks if a parent node is larger than the node in question
        and swaps the two nodes until the heap properties are intact for the heap

        Input:
        Output:
        """
        node_index = len(self) - 1
        parent_index = (node_index - 1)//2
        while self[node_index] < self[parent_index] and node_index > 0:
            self[node_index], self[parent_index] =  self[parent_index], self[node_index]
            node_index -= 1
            parent_index = (node_index - 1)//2

    def bubble_down(self):
        """
        Used to rebalance the heap when a node is added to the top of the heap
        during an operation like poll(). Checks if a parent node is larger than
        children node and swaps the two nodes until the heap properties
        are intact for the heap. The smaller of children nodes is always chosen
        for the swap. If the children nodes are equal, left node is the tie breaker

        Input:
        Output:
        """
        node_index = 0
        while True:
            children = self.children(node_index)
            if not children:
                break

            if len(children) == 2:
                if children[0] == children[1]:
                    swap_node = children[0]
                else:
                    swap_node = min(children)
            else:
                swap_node = min(children)
            if self[node_index] > self[swap_node]:
                self[node_index], self[swap_node] = self[swap_node], self[node_index]
                node_index = swap_node
            else:
                break

    def size(self):
        """
        Used to determine the number of nodes in heap
        Input:
        Output:
            (int) = Number of nodes in self
        """
        return len(self)

    def heapify(self, nodes_arr):
        """
        Consumes an array of comparable objects and adds them to self
        Input:
            [(object)] = Array of comparable objects to be added to the heap
        Output:
        """
        for node in nodes_arr:
            self.insert(node)

    def find(self, value):
        """
        Used to find the indices of a given value in self
        Input:
            (object) = Value of item to find in the heap
        Output:
            [(int)] = Array of indices of where the value is in self
        """
        return [ index for index, val in enumerate(self) if val == value ]


    def is_empty(self):
        """
        Used to check if self is empty

        Input:
        Output:
            (bool) = True if self is empty, False if self is not empty
        """
        return not self

    def __getitem__(self, key):
        """
        Overwrites normal array access so that leaf nodes return none instead of
        index errors
        Input:
            (int) = Index of the node to be returned
        Output:
            (object || None) = If there is a node at that index, that node value
                                will be returned. None if there is no node at index
        """
        try:
            return super().__getitem__(key)
        except IndexError:
            return None
