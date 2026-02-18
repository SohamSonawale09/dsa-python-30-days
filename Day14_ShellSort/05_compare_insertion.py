# Problem Statement:
# Compare Insertion Sort and Shell Sort by counting the number of operations performed.

def insertion_sort(arr):
    count = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
            count += 1

        arr[j+1] = key

    return count


def shell_sort(arr):
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

    return count


arr1 = [12, 34, 54, 2, 3]
arr2 = arr1.copy()

print("Insertion Sort operations:", insertion_sort(arr1))
print("Shell Sort operations:", shell_sort(arr2))
