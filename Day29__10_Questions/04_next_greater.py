# Problem

# Find the next greater number for each element. 

def next_greater(nums):
    result = [-1]*len(nums)

    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[j] > nums[i]:
                result[i] = nums[j]
                break

    return result 
nums = [2,1,2,4,3] 

print(next_greater(nums))