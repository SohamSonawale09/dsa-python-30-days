# Problem

# Swap left and right of every node.

def invert_tree(root):
    if root:
        root.left, root.right = root.right, root.left
        invert_tree(root.left)
        invert_tree(root.right)
    return root