import sys
sys.path.append('../../basic_composites/stacks')
from stack_array import *


def sort_stack(stack):
    # Create holding stack
    sorted_stack = Stack()
    # Push top item from stack into sorted stack
    sorted_stack.push(stack.pop())

    while not stack.is_empty():
        # Grab top items from both stacks
        unsorted_item = stack.pop()
        sorted_item = sorted_stack.pop()
        # While our unsorted is > sorted, keep popping from sorted over to stack
        while unsorted_item > sorted_item and not sorted_stack.is_empty():
            stack.push(sorted_item)
            sorted_item = sorted_stack.pop()
        # We've found where our items should go, place them into the sorted stack
        sorted_stack.push(max(sorted_item, unsorted_item))
        sorted_stack.push(min(unsorted_item, sorted_item))

    return sorted_stack
