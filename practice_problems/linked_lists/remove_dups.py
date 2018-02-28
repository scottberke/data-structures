import sys
sys.path.append('../../basic_composites/linked_lists')
from linked_list import *

def remove_dups(linked_list):
    # Set for unique node data
    ref_node_data = { linked_list.head.data }
    # Previous node will start as head
    prev_node = linked_list.head
    # Current node will start as second node
    current_node = prev_node.next
    while current_node.next:
        # If the nodes not unique, remove it
        if current_node.data in ref_node_data:
            prev_node.next = current_node.next
        else:
            # Otherwise, add unique node data and advance
            ref_node_data.add(current_node.data)
            prev_node = prev_node.next
        current_node = current_node.next
    # Make sure tail node is checked
    if current_node.data in ref_node_data:
        prev_node.next = None

    return linked_list

# First Implementation: Uses extra space so not as efficient as it should be
# def remove_dups(linked_list):
#     # Set to hold data
#     ref_node_data = set()
#     # Empty linked list
#     dedupped = LinkedList()
#     # Start node
#     current_node = linked_list.head
#     # Iterate until the end
#     while current_node.next:
#         # Unique node found
#         if current_node.data not in ref_node_data:
#             # Add to reference set
#             ref_node_data.add(current_node.data)
#             # Update head
#             linked_list.head = current_node.next
#             # Add to dedupped linked list
#             dedupped.append(current_node)
#             # Clear current nodes next
#             current_node.next = None
#             # New current node
#             current_node = linked_list.head
#         else:
#             # Update current node
#             current_node = current_node.next
#     # Add last node to dedupped
#     if current_node.data not in ref_node_data: dedupped.append(current_node)
#     return dedupped
