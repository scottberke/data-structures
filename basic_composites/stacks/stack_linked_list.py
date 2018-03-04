import sys
sys.path.append('../../basic_composites/linked_lists')
from linked_list import *

class Stack(LinkedList):
    def __init__(self):
        super().__init__()
        self.size = 0

    def push(self, data):
        self.append(data)
        self.size += 1
        return self.tail

    def pop(self):
        if self.size == 0:
            return self
        else:
            self.size -= 1
            return self.delete_node(self.tail)

    def is_empty(self):
        return not self.head
