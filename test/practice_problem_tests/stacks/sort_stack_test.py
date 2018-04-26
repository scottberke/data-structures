import unittest
from practice_problems.stacks.sort_stack import *
import random

class SortStackTest(unittest.TestCase):
    def test_sort_stack_simple(self):
        stack = Stack()
        items = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        # pushes items on so 1 is bottom, 9 is top
        for item in items:
            stack.push(item)

        sorted_stack = sort_stack(stack)
        # check from index 0 on of sorted items
        for item in items:
            self.assertTrue(
                    # Grab top from sorted_stack
                    item == sorted_stack.pop()
                )

    def test_sort_stack_simple_diff_order(self):
        stack = Stack()
        items = [2, 1, 3, 4, 6, 5, 7, 8, 9]
        for item in items:
            # Pushes items on so 1 is bottom, 9 is top
            stack.push(item)
        # Sort stack
        sorted_stack = sort_stack(stack)
        # Sort items
        items = sorted(items)
        # Check from index 0 on of sorted items
        for item in items:
            # Grab top from sorted_stack
            sorted_item = sorted_stack.pop()
            self.assertTrue(
                    item == sorted_item
                )

    def test_sort_stack_simple_w_dups(self):
        stack = Stack()
        items = [2, 1, 3, 4, 4, 5, 5, 9, 8]
        for item in items:
            # Pushes items on so 1 is bottom, 9 is top
            stack.push(item)
        print(stack)
        # Sort stack
        sorted_stack = sort_stack(stack)
        print(sorted_stack)
        # Sort items
        items = sorted(items)
        # Check from index 0 on of sorted items
        for item in items:
            # Grab top from sorted_stack
            sorted_item = sorted_stack.pop()
            self.assertTrue(
                    item == sorted_item
                )

    def test_sort_stack_large_stack(self):
        stack = Stack()
        items = random.sample(range(1,1000), 100)
        print(items)
        for item in items:
            # Pushes items on so 1 is bottom, 9 is top
            stack.push(item)
        # Sort stack
        sorted_stack = sort_stack(stack)
        print(sorted_stack)
        # Sort items
        items = sorted(items)
        print(items)
        # Check from index 0 on of sorted items
        for item in items:
            # Grab top from sorted_stack
            sorted_item = sorted_stack.pop()
            # print(sorted_item)
            self.assertTrue(
                    item == sorted_item
                )

if __name__ == "__main__":
    unittest.main()
