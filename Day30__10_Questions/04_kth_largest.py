# Problem

# Find kth largest number. 

nums = [3,2,1,5,6,4]
k = 2 
def kth_largest(nums,k):
    nums.sort(reverse=True)
    return nums[k-1]

print(kth_largest(nums,k))