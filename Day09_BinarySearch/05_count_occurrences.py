# Problem: Count how many times a number appears in sorted array

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
target = 2

first = first_occurrence(arr, target)
last = last_occurrence(arr, target)

if first == -1:
    print(0)
else:
    print(last - first + 1)