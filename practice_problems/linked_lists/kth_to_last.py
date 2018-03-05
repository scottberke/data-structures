import sys
sys.path.append('../../basic_composites/linked_lists')
from linked_list import *

from collections import *

def find_kth(linked_list, kth):
    first = linked_list.head
    second = linked_list.head

    for i in range(kth):
        first = first.next

    while first.next:
        first = first.next
        second = second.next

    return second.next.data

# Brute Force - keep track of nodes position in dict while traversing
# O(n) - space required for nodes and hash so not a good solution
# def find_kth(linked_list, kth):
#     ref_key = 0
#     reference = { ref_key: linked_list.head }
#     current_node = linked_list.head.next
#     while current_node.next:
#         ref_key += 1
#         reference[ref_key] = current_node
#         current_node = current_node.next
#         if not current_node.next:
#             ref_key += 1
#             reference[ref_key] = current_node
#
#     kth_pos = ref_key + 1 - kth
#     return reference[kth_pos].data

# Brute Force - Figure out the size then traverse back to kth
# O(n + n) == O(n) - No extra space required but seems uglier than the two pointers
# method above
# def find_kth(linked_list, kth):
#     counter = 1
#     current_node = linked_list.head
#     while current_node.next:
#         counter += 1
#         current_node = current_node.next
#
#
#     current_node = linked_list.head
#     while counter > kth:
#         counter -= 1
#         current_node = current_node.next
#
#     return current_node.data
