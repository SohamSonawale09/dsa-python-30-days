# linear search 
# Problem: Linear Search
# Description: Given an array of integers and a target value, check whether
# the target exists in the array by examining each element one by one.
# Time Complexity: O(n)
# Space Complexity: O(1)

l = [1,3,45,6,7,8,9]
target_value = 9

found = False
for i in l:

    if i == target_value:
        found = True
        break
if found:
    print("The target value is present")
else:
    print("The target value is not present")