# Problem

# Find an element greater than neighbors.

nums = [1,2,3,1]

def find_peak(nums):
    for i in range(1,len(nums)-1):
        if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
            return i
    return 0 
print(find_peak(nums))