# 6 Find Minimum in Rotated Sorted Array 

# arr = [8, 9, 1, 2, 3, 4, 5] 


# def minimum(arr):
#     minimim_value = arr[0]
#     for i in arr:
#         if i < minimim_value:
            
#             minimim_value = i
#     return (minimim_value)
    
# print(minimum(arr)) 

# using binary search 

def find_min(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        mid = (left + right) // 2

        if arr[mid] > arr[right]:
            left = mid + 1
        else:
            right = mid

    return arr[left]


arr = [8, 9, 1, 2, 3, 4, 5]
print(find_min(arr))