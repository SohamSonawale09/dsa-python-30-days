# Problem Statement:
# Implement Shell Sort and count the number of swaps (or shifts) performed during sorting.

def shell_sort_count(arr):
    n = len(arr)
    gap = n // 2
    count = 0

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i

            while j >= gap and arr[j-gap] > temp:
                arr[j] = arr[j-gap]
                j -= gap
                count += 1

            arr[j] = temp
        gap //= 2

    print("Total swaps:", count)
    return arr


arr = [12, 34, 54, 2, 3]
print(shell_sort_count(arr))
