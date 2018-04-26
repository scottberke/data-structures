from data_structures.basic_composites.linked_lists.linked_list import *

# O(n)
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
