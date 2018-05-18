
def check_balanced(tree):
    """
    Input:
        tree (Node) = Root node of a tree
    Output:
        Bool = True or False if the tree is balanced or not
    """
    if not tree:
        return True

    return (get_height(tree.left) - get_height(tree.right) in [-1, 0, 1])


def get_height(tree, height=0):
    """
    Input:
        tree (Node) = Root node of a tree
        height (int) = Int representing height at current root
    Output:
        int = height of root node passed in
    """
    if not tree:
        return height

    return max(get_height(tree.left, height + 1), get_height(tree.right, height + 1))
