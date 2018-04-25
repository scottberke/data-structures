"""
An implementation of a stack using an array
Author: Scott Berke
"""
class Stack(list):
    def __init__(self, name=None):
        self.name = name
        pass

    def push(self, data):
        self.append(data)

    def pop(self):
        return super().pop()

    def size(self):
        return len(self)

    def is_empty(self):
        return not self
