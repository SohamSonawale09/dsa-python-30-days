# Problem: Count leaf nodes in a binary tree
# Time Complexity: O(n)
# Space Complexity: O(n)

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def count_leaf_nodes(root):
    if root is None:
        return 0
    
    
    if root.left is None and root.right is None:
        return 1
    
    return count_leaf_nodes(root.left) + count_leaf_nodes(root.right)

# Create tree
#        1
#       / \
#      2   3
#     / \
#    4   5

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

leaf_count = count_leaf_nodes(root)
print("Total leaf nodes:", leaf_count)
