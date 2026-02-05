# problem: Traverse an array
# Approach: Loop throught the array and visit each element once 
# Time Complexity :O(n)
# Space Complexity: O(1)

l = [1,2,3,4,21,34,56,78]

# Traversal by value 
for X in l:
    print(X)
    
# Alternative traversal (index + value)
for i in range(len(l)):
    print(i,l[i])
     