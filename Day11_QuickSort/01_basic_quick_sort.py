# Problem

# Sort array using Quick Sort. 

# Basic Quick Sort (Ascending)

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    
    left = []
    right = []
    
    for i in arr[1:]:
        if i <= pivot:
            left.append(i)
        else:
            right.append(i)
    
    return quick_sort(left) + [pivot] + quick_sort(right)


arr = [5, 3, 8, 1]
print(quick_sort(arr))