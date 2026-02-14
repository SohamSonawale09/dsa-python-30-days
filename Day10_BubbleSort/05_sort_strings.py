# Problem

# Sort list of strings using bubble sort. 

def bubble_sort_strings(arr):
    n = len(arr)
    
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    return arr


arr = ["banana", "apple", "cherry"]
print(bubble_sort_strings(arr))