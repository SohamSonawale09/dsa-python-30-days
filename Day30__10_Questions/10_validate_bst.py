# Problem

# Check if tree follows BST rules:

# Left < Root < Right 

def validate_bst(root, low=float('-inf'), high=float('inf')):
    if not root:
        return True
    if not (low < root.val < high):
        return False
    return (validate_bst(root.left, low, root.val) and
            validate_bst(root.right, root.val, high))