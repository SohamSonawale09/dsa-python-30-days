# Merge Sort Simple Version

def merge_sort(arr):

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    result = []

    while left and right:

        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    result = result + left + right

    return result


arr = [5, 3, 8, 1]

print(merge_sort(arr))
