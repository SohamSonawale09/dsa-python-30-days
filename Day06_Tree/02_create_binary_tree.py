# Problem: Create a simple binary tree
# Description: Manually create nodes and connect them to form a binary tree
# Approach: Create Node objects and assign left and right children
# Time Complexity: O(1)
# Space Complexity: O(1)

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

print("Root:", root.data)
print("Left child of root:", root.left.data)
print("Right child of root:", root.right.data)
