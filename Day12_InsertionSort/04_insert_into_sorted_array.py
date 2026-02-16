# Problem

# Insert element into sorted array. 

def insert_sorted(arr, value):
    arr.append(value)
    
    i = len(arr) - 2
    
    while i >= 0 and arr[i] > value:
        arr[i + 1] = arr[i]
        i -= 1
    
    arr[i + 1] = value
    
    return arr


arr = [1, 3, 5, 8]
print(insert_sorted(arr, 4))