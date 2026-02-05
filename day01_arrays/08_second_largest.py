# Problem: Find the second largest element in an array
# Description: Given an array of integers, find the second largest
# distinct element present in the array.
# Time Complexity: O(n)
# Space Complexity: O(1)

l = [1, 2, 3, 9, 10, 5]

largest = l[0]
second_largest = l[0]

for i in l:
    if i > largest:
        second_largest = largest
        largest = i
    elif i < largest and i > second_largest:
        second_largest = i

print("Second largest:", second_largest)
