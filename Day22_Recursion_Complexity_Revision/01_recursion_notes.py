# Recursion:
# A function calling itself

# Two Important Parts:
# 1. Base Case (Stopping condition)
# 2. Recursive Call

def factorial(n):
    if n == 1:     # Base case
        return 1
    return n * factorial(n-1)

print("Factorial of 5:", factorial(5))

# Used In:
# - Tree traversal
# - Divide & Conquer algorithms
# - Backtracking problems

print("Recursion Revision Completed ✅")