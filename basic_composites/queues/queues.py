class Queue(list):
    def __init__(self):
        pass

    def enqueue(self, data):
        self.insert(0, data)

    def dequeue(self):
        return self.pop()

    def is_empty(self):
        return not self

    def peek(self):
        return self[-1]    
