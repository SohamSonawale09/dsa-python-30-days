# Problem Statement:
# Use Shell Sort to sort a list of strings in alphabetical order.

def shell_sort_strings(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i

            while j >= gap and arr[j-gap] > temp:
                arr[j] = arr[j-gap]
                j -= gap

            arr[j] = temp
        gap //= 2

    return arr


arr = ["banana", "apple", "cherry"]
print(shell_sort_strings(arr))
