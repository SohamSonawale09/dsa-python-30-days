# Problem

# Count shifts during sorting 

def insertion_sort_count(arr):
    count = 0
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            count += 1
            j -= 1
        
        arr[j + 1] = key
    
    print("Total count:", count)
    return arr


arr = [5, 3, 8, 1]
print(insertion_sort_count(arr))