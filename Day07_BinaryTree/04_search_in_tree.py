# Problem: Search a value in a binary tree
# Time Complexity: O(n)
# Space Complexity: O(n)

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def search(root, target):
    if root is None:
        return False
    
    if root.data == target:
        return True
    
    return search(root.left, target) or search(root.right, target)

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

target = 5
result = search(root, target)

print("Value found?" , result)
