# Problem

# Find maximum value in every window of size k. 

def sliding_window(nums,k):
    result = []

    for i in range(len(nums)-k+1):
        result.append(max(nums[i:i+k]))

    return result 
nums = [1,3,-1,-3,5,3,6,7]
k = 3 
print(sliding_window(nums,k))