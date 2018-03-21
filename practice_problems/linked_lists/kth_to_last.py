import sys
sys.path.append('../../basic_composites/linked_lists')
from linked_list import *

# TODO:
# Implement recursive version

# O(n + n) = O(n)
# two pointers seems to be a more elegant solution
def find_kth(linked_list, kth):
    first = linked_list.head
    second = linked_list.head

    for i in range(kth):
        first = first.next

    while first.next:
        first = first.next
        second = second.next

    return second.next.data

# Brute Force - Figure out the size then traverse back to kth
# O(n + n) == O(n) - No extra space required but seems uglier than the two pointers
# method above
def find_kth_single(linked_list, kth):
    counter = 1
    current_node = linked_list.head
    while current_node.next:
        counter += 1
        current_node = current_node.next


    current_node = linked_list.head
    while counter > kth:
        counter -= 1
        current_node = current_node.next

    return current_node.data
