# Problem Statement 
# Given a binary tree,find its height (maximum depth).

# Problem: Find height of a binary tree
# Time Complexity: O(n)
# Space Complexity: O(n)

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def height(root):
    if root is None:
        return 0
    
    return 1 + max(height(root.left), height(root.right))

# Create tree manually
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


h = height(root)
print("Height of tree:", h)
