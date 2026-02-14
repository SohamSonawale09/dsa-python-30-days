# Problem

# Stop early if already sorted. 

def bubble_sort_optimized(arr):
    n = len(arr)
    
    for i in range(n):
        swapped = False
        
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        if not swapped:
            break
    
    return arr


arr = [1, 2, 3, 4]
print(bubble_sort_optimized(arr))