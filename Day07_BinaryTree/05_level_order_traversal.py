# Problem: Level Order Traversal (BFS)
# Time Complexity: O(n)
# Space Complexity: O(n)

from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def level_order(root):
    if root is None:
        return
    
    queue = deque([root])
    
    while queue:
        current = queue.popleft()
        print(current.data, end=" ")
        
        if current.left:
            queue.append(current.left)
        
        if current.right:
            queue.append(current.right)

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

level_order(root)
