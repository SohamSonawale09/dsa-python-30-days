# Problem
# Given a sorted array and a target value, return its index.
# If not found, return -1. 

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return -1


arr = [1, 3, 5, 7, 9]
print(binary_search(arr, 7))