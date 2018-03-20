import pdb
class LinkedList:
    def __init__(self, head=None):
        """
        Input:
            head (node) = Node that is the first element in the linked list
         Output:
            LinkedList
        """
        self.head = head
        self.tail = None

    def get(self, data):
        """
        O(n)
        Input:
            data = Value to search for in the linked list
        Output:
            Node = Node containing the data value if the value is in the
                        linked list
            False = False is returned if value doesnt exist in the linked list
        """
        current_node = self.head
        if current_node.data == data:
            return current_node

        while current_node.next:
            current_node = current_node.next
            if current_node.data == data:
                return current_node

        return False



    def append(self, data):
        """
        O(n) or O(1) if keeping track of tail
        Input:
            data = Value to append to the end of the linked list
        Output:
            Node = new node that was appended to the linked list
        """
        new_node = self.handle_data(data)

        if not self.head:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node

        self.tail = new_node

        return new_node



    def push(self, data):
        """
        O(1)
        Input:
            data = Value to add to the start of the linked list
        Output:
            Node = new node that was appended to the linked list
        """
        new_node = self.handle_data(data)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        return new_node



    def insert_after(self, after_node, data):
        """
        O(n)
        Input:
            after_node = data value of node to insert after
            data = Value to add to the start of the linked list
        Output:
            node = new node just inserted
        """
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
        if not new_node.next:
            self.tail = new_node
        else:
            new_node.next = next_node

        return new_node



    def delete_node(self, data):
        """
        O(n)
        Input:
            data || Node = Node or value of node to delete from the linked list
        Output:
            node = node that was just removed
        """
        current_node = self.head
        if type(data) == Node:
            if current_node == data:
                self.head = current_node.next
                return current_node

            while current_node.next != data:
                if not current_node.next:
                    raise ValueError("Node not in linked list")
                else:
                    current_node = current_node.next
        else:
            if current_node.data == data:
                self.head = current_node.next
                return current_node

            while current_node.next.data != data:
                if not current_node.next:
                    raise ValueError("Node not in linked list")
                else:
                    current_node = current_node.next

        current_node.next = current_node.next.next

        if not current_node.next:
            self.tail = current_node

        return current_node



    def print_list(self):
        """
        Input:
        Output:
            None = Nothing is returned. List data is printed
        """
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next



    def handle_data(self, data):
        """
        Input:
            data (Node or Value) = This is either value to be used in a node or
                            the node already containing data
        Output:
            Node
        """
        if type(data) is Node:
            return data
        else:
            return Node(data)

    # Helpers to allow linked list to be used as an iterable
    def items(self):
        current_node = self.head
        yield current_node
        while current_node.next:
            current_node = current_node.next
            yield current_node

class Node:
    def __init__(self, data):
        """
        Input:
            data (Object) = Data to be stored in linked list
        Output:
            Node
        """
        self.data = data
        self.next = None

    def next(self):
        return self.next
