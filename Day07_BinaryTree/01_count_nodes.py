# Problem: Count total nodes in a binary tree
# Time Complexity: O(n)
# Space Complexity: O(n)

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def count_nodes(root):
    if root is None:
        return 0
    
    return 1 + count_nodes(root.left) + count_nodes(root.right)

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


total = count_nodes(root)
print("Total nodes:", total)
