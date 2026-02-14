# Problem

# Sort array in ascending order. 
def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    return arr


arr = [5, 3, 8, 1]
print(bubble_sort(arr))