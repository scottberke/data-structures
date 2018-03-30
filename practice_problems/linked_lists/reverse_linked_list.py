import sys
sys.path.append('../../basic_composites/linked_lists')
from linked_list import *

# O(n) where n is the length of the linked list
def reverse_linked_list(linked_list):
    # Grab head as the starting node
    current_node = linked_list.head
    # Iterate until head has found it's way to the end
    while current_node.next:
        # Grab current node's next neighbor
        swap_node = current_node.next
        # Move current node into the swap nodes place by point to its next neighbor
        current_node.next = swap_node.next
        # Point the swap node next neighbor to the lists head
        swap_node.next = linked_list.head
        # Update linked list head to the swap node 
        linked_list.head = swap_node

    return linked_list
