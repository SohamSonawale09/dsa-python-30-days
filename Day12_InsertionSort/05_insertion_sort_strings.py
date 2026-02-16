# Problem

# Sort list of strings. 

def insertion_sort_strings(arr):
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key
    
    return arr


arr = ["banana", "apple", "cherry"]
print(insertion_sort_strings(arr))