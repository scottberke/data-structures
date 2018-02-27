class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def add(self, data):
        new_node = Node(data)
        if not self.head:
            head = new_node
        else:
            current_node = self.head
            while current_node:
                current_node = current_node.next()
            current_node = new_node

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def next(self):
        return self.next
