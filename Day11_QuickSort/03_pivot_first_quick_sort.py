# Quick Sort using First Element as Pivot 

def quick_sort_pivot_first(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    
    smaller = [x for x in arr[1:] if x <= pivot]
    larger = [x for x in arr[1:] if x > pivot]
    
    return quick_sort_pivot_first(smaller) + [pivot] + quick_sort_pivot_first(larger)


arr = [10, 7, 8, 9, 1, 5]
print(quick_sort_pivot_first(arr))