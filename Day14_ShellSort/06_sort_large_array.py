# Problem Statement:
# Sort the following large array using Shell Sort.

def shell_sort(arr):
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


arr = [23, 12, 1, 8, 34, 54, 2, 3, 99, 17, 45, 6]
print(shell_sort(arr))
