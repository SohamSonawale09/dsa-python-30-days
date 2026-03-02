# 9 Rotate Array

def rotate(arr, k):
    n = len(arr)
    k = k % n   
    
    arr = arr[-k:] + arr[:-k]
    return arr


# Example
arr = [1, 2, 3, 4, 5, 6, 7]
k = 3
print(rotate(arr, k))