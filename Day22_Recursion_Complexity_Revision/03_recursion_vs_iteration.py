# Recursion:
# Function calls itself
# Uses call stack

# Iteration:
# Uses loops (for / while)

# Example:

# Iteration
for i in range(3):
    print("Iteration:", i)

# Recursion
def recursive(n):
    if n == 0:
        return
    print("Recursion:", n)
    recursive(n-1)

recursive(3)

print("Concept Revised ✅")