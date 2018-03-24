# Queues
## Description
A queue is similar to a stack in that it is a collection of data in a particular order. While a stack is LIFO, a queue is **FIFO or First In First Out**. A queue is analogous to a line one would wait in - You enter the line and are served in the order that you enter.

Typical operations performed on a queue are **enqueuing** and **dequeuing** which add items to the queue and remove items from the respectivly. Items are enqueued at the rear and dequeued at the front of the queue. Enqueuing and dequeuing are both constant time **O(1)** operations.

A queue can be implemented with an array or a linked list.      

### Common Uses
- Queues are used in breadth first search. Items to be searched are enqueued and dequeued at each level.
- Queues are often used for scheduling execution of processes.

### Pros
- Easy to implement
- Doesn't require pointers like linked lists if implemented with an array

### Cons
- Not appropriate for iteration

## Implementation
- [Queue Test Cases - Python](./queues_test.py)
- [Queue - Python](./queues.py)
