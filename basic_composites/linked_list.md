# Linked Lists
## Description:
Linked lists are similar to an array in that they act as a container for other values, however, unlike an array, they do not take up a contiguous block of memory. Instead, linked lists can be thought of as nodes with each node containing data and a reference to the next node. The reference to the next node is usually in the form of a pointer that points to another location in memory where the next node is.

This structure allows for easy and efficient insertion and deletion of elements from any position. In an array, if you insert or delete a specific location, you need to reorder the remaining elements in memory. In a linked list you only need to update the pointers to point to the new next node.

The ability to insert and delete quickly makes access less efficient since you have to traverse the entire linked list to find a specific node.

Linked lists can be both singly linked listed and doubly linked lists. A singly linked list has one pointer pointing to the next node while a doubly linked list has a pointer to the next node as well as a pointer to the previous node.

The 'head' of a linked list is the first node.


### Pros
- Dynamic size
- Easy insertion and deletion
### Cons
- Can't random access. Need to access all elements sequentially starting from begining
- Need to have space for pointer along with each element

[Linked List Implementation - Python](./linked_list.py)
[Linked List Test Cases - Python](./linked_list_test.py)
