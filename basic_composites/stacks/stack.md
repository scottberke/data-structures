# Stacks
## Description
A stack is a data structure that adheres to LIFO or last in first out when it comes to storage and retrieval of elements. To add something to the stack you `push` it onto the top of the stack and to remove something you `pop` it off of the top.

Stacks can be thought of visually as a stack of cafeteria trays - the trays are placed on top of one another and when one is removed it is removed from the top. So when a patron removes a tray, they will be removing the last tray that was placed on the stack.

Stacks are often implemented as either an array or a linked list. Stacks are commonly used with memory or a call stack for active subroutines of a computer program to allow the program to keep track of where a subroutine should return control on completion.  

Both `push` and `pop` operations are O(1).

### Pros
- Easy to implement
- Doesn't require pointers like linked lists if implemented with an array

### Cons
- Not appropriate for iteration

## Implementation
[Stack With Array - Python](./stack_array.py)
[Stack With Array Test Cases - Python](./stack_array_test.py)
[Stack With Linked List - Python](./stack_linked_list.py)
[Stack With Linked List Test Cases - Python](./stack_linked_list_test.py)
