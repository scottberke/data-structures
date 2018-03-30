class MinHeap(list):
    def __init__(self):
        pass

    def peek(self):
        return self[0]

    def insert(self, item):
        self.append(item)
        self.bubble_up()

    def poll(self):
        if len(self):
            self[0], self[-1] = self[-1], self[0]
        polled = self.pop()
        self.bubble_down()
        return polled

    def children(self, node_index):
        children = []
        # Children of node @ 2*node_index + 1 and 2*node_index + 2
        for i in range(1,3):
            child_index = (2*node_index) + i
            if child_index < len(self):
                children.append(child_index)
        return children

    def bubble_up(self):
        node_index = len(self) - 1
        while self[node_index] < self[node_index - 1] and node_index > 0:
            self[node_index], self[node_index - 1] =  self[node_index - 1], self[node_index]
            node_index -= 1

    def bubble_down(self):
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

# TODO: size()
# TODO: find()
# TODO: heapify()
# TODO: is_empty()

    def __getitem__(self, key):
        try:
            return super().__getitem__(key)
        except IndexError:
            return None
