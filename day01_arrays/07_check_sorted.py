# check sorted
# Problem: Check if an array is sorted
# Description: Given an array of integers, check whether the array
# is sorted in non-decreasing (ascending) order.
# Time Complexity: O(n)
# Space Complexity: O(1)

l = [1, 2, 8, 4, 5]
found = False   # found means "order is broken"

for i in range(len(l) - 1):
    if l[i] > l[i + 1]:
        found = True
        break

if found:
    print("Array is not sorted")
else:
    print("Array is sorted")
