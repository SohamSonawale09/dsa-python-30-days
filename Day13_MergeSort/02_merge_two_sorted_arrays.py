# Merge Two Sorted Arrays

def merge(arr1, arr2):

    result = []

    while arr1 and arr2:

        if arr1[0] < arr2[0]:
            result.append(arr1.pop(0))
        else:
            result.append(arr2.pop(0))

    return result + arr1 + arr2


print(merge([1,4,7], [2,3,6]))
