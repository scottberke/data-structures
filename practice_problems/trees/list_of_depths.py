
class LinkedListNode():
    def __init__(self, tree_node):
        self.tree_node = tree_node
        self.next = None

class LinkedList():
    def __init__(self, head=None):
        if head:
            self.head = self.append(head)
        else:
            self.head = None

        self.size = 0

    def append(self, node):
        if self.head:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = node
        else:
            self.head = node

        self.size += 1



def list_of_depths(tree):
    """
    Consumes a tree and turns each level of the tree into a linked list

    Input:
        tree (tree) = Tree to traverse
    Output:
        arr = Array of linked lists where each linked list is a level of the tree
    """
    if not tree:
        return []

    levels_as_linked_lists = []
    current_tree_node = tree
    level = LinkedList()
    level.append(LinkedListNode(current_tree_node))

    while level.size:
        levels_as_linked_lists.append(level)
        # The last linked list in the array is the previous level so each node
        # in the linked list points to the next level down
        parents = levels_as_linked_lists[-1]
        level = LinkedList()
        current_node = parents.head

        while current_node:
            child_left = current_node.tree_node.left
            child_right = current_node.tree_node.right

            if child_left:
                new_node = LinkedListNode(child_left)
                level.append(new_node)

            if child_right:
                new_node = LinkedListNode(child_right)
                level.append(new_node)

            current_node = current_node.next


    return levels_as_linked_lists
