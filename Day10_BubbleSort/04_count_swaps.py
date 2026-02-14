# Problem

# Count swaps during sorting. 

def bubble_sort_count_swaps(arr):
    n = len(arr)
    swaps = 0
    
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
    
    print("Total swaps:", swaps)
    return arr


arr = [5, 3, 8, 1]
print(bubble_sort_count_swaps(arr))