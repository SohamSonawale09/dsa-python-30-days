# Problem

# Sort in descending order.

def quick_sort_desc(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    
    left = []
    right = []
    
    for i in arr[1:]:
        if i >= pivot:
            left.append(i)
        else:
            right.append(i)
    
    return quick_sort_desc(left) + [pivot] + quick_sort_desc(right)


arr = [5, 3, 8, 1]
print(quick_sort_desc(arr))