# Problem
# Given an array and a target, find two numbers whose sum equals the target and return their indices. 

nums = [2,7,11,15]
target = 9
# Output → [0,1] 

def two_sum(nums, target):
    seen = {}

    for i in range(len(nums)):
        need = target - nums[i]

        if need in seen:
            return [seen[need], i]

        seen[nums[i]] = i 
print(two_sum(nums,target))