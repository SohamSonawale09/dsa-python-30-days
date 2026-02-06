# Problem: Find the maximum and minimum element in an array
# Approach: Traverse the array once and compare elements using if conditions
# Time Complexity: O(n)
# Space Complexity: O(1)

l = [2,4,1,5,6,7]

max_val = l[0]
min_val = l[0] 

for i in l:
    if i > max_val:
        max_val = i 
    if i < min_val:
        min_val = i 
        
print("The max value is",max_val)
print("The min value is",min_val)