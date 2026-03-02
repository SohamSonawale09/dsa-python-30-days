# 7 Search in Rotated Sorted Array 

def search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

  
        if arr[left] <= arr[mid]:
            if target >= arr[left] and target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
  
        else:
            if target > arr[mid] and target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


arr = [4, 5, 6, 7, 0, 1, 2]
print(search(arr, 0))