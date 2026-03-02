def find_min(arr):
    left = 0
    right = len(arr) - 1
    
    while left < right:
        mid = (left + right) //2
        
        if arr[mid] > arr[right]:
            left = mid + 1
        else:
            rigth = mid
    return arr[left]

arr = [8,9,1,2,3,4,5]
print(find_min(arr))