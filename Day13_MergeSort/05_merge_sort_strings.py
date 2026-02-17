# Merge Sort Strings 

def merge_sort_strings(arr):

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort_strings(arr[:mid])
    right = merge_sort_strings(arr[mid:])

    result = []

    while left and right:

        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    return result + left + right


print(merge_sort_strings(["banana","apple","cherry"]))
