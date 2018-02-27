import pdb
class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def get(self, data):
        current_node = self.head
        while current_node.next:
            if current_node.data == data:
                return current_node
            current_node = current_node.next

        return False


    def append(self, data):
        new_node = self.handle_data(data)

        if not self.head:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node

    def push(self, data):
        new_node = self.handle_data(data)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_after(self, after_node, data):
        if not after_node or not data:
            raise ValueError("After node and data are required")

        new_node = self.handle_data(data)
        current_node = self.head

        while current_node.data != after_node:
            if not current_node.next:
                raise ValueError("After node not in linked list")
            else:
                current_node = current_node.next

        next_node = current_node.next
        current_node.next = new_node
        new_node.next = next_node

        return new_node

    def delete_node(self, data):
        current_node = self.head
        if current_node.data == data:
            self.head = current_node.next
            return current_node

        while current_node.next.data != data:
            if not current_node.next:
                raise ValueError("Node not in linked list")
            else:
                current_node = current_node.next

        current_node.next = current_node.next.next
        return current_node

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next


    def handle_data(self, data):
        if type(data) is Node:
            return data
        else:
            return Node(data)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def next(self):
        return self.next



l = LinkedList()
l.append('tacos')
l.append('tequila')
l.append('burritos')
l.push('salsa')
