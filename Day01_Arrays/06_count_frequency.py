# Problem: Count frequency of an element
# Description: Given an array of integers and a target value,
# count how many times the target appears in the array.
# Time Complexity: O(n)
# Space Complexity: O(1)


l = [1,2,3,4,3,2,3]
target_value = 3 
count = 0
for i in l:
    if i == target_value:
        count+=1
print(count)