import unittest

from stack_linked_list import *

class StackLinkedListTest(unittest.TestCase):
    def test_stack_new(self):
        stack = Stack()
        self.assertTrue(
            type(stack) == Stack
        )

    def test_stack_push(self):
        stack = Stack()
        data = 'tacos'
        stack.push(data)
        self.assertTrue(
            data == stack.head.data
        )

    def test_stack_pop(self):
        stack = Stack()
        data = 'tacos'
        node = stack.push(data)
        popped = stack.pop()

        self.assertTrue(
            popped == node and stack.is_empty()
        )

    def test_stack_size(self):
        datas = "tacos tequila whiskey cheese".split()
        stack = Stack()
        for i in datas:
            stack.push(i)

        self.assertEqual(
            stack.size,
            len(datas)
        )

    def test_stack_is_empty(self):
        stack = Stack()
        self.assertTrue(
            stack.is_empty()
        )

        data = 'tacos'
        stack.push(data)
        self.assertFalse(
            stack.is_empty()
        )

if __name__ == "__main__":
    unittest.main()
