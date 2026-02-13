# Problem
# Find the first occurrence of a number in sorted array with duplicates. 

def first_occurrence(arr, target):
    left = 0
    right = len(arr) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            result = mid
            right = mid - 1
        elif target < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return result


arr = [1, 2, 2, 2, 3]
print(first_occurrence(arr, 2))