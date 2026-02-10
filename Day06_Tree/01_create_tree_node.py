# Problem: Create a Tree Node
# Description: Create a Node class for a binary tree
# Approach: Use a class with data, left, and right
# Time Complexity: O(1)
# Space Complexity: O(1)

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
