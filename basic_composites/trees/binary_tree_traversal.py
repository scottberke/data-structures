
def in_order_traversal(node):
    if node:
        in_order_traversal(node.left)
        print(node.data)
        in_order_traversal(node.right)

def post_order_traversal(node):
    if node:
        print(node.data)
        post_order_traversal(node.left)
        post_order_traversal(node.right)
