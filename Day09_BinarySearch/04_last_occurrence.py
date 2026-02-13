# Problem
# Find the last occurrence of target. 

def last_occurrence(arr, target):
    left = 0
    right = len(arr) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            result = mid
            left = mid + 1
        elif target < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return result


arr = [1, 2, 2, 2, 3]
print(last_occurrence(arr, 2))