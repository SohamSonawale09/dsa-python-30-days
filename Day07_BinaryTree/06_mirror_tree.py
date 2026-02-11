# Problem: Mirror of Binary Tree
# Time Complexity: O(n)
# Space Complexity: O(n)

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def mirror(root):
    if root is None:
        return None
    
    root.left, root.right = root.right, root.left
    

    mirror(root.left)
    mirror(root.right)
    
    return root

from collections import deque

def level_order(root):
    if root is None:
        return
    
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.data, end=" ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Original tree (Level order):")
level_order(root)

mirror(root)

print("\nMirrored tree (Level order):")
level_order(root)
