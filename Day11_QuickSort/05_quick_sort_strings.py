# Quick Sort on Strings 

def quick_sort_strings(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    
    left = []
    right = []
    
    for word in arr[1:]:
        if word <= pivot:
            left.append(word)
        else:
            right.append(word)
    
    return quick_sort_strings(left) + [pivot] + quick_sort_strings(right)


arr = ["banana", "apple", "cherry"]
print(quick_sort_strings(arr))