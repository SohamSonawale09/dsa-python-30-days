# Problem

# Return index if target found, else position where it should be inserted. 

nums = [1,3,5,6]
target = 2 

def search_insert(nums, target):
    for i in range(len(nums)):
        if nums[i] >= target:
            return i
    return len(nums) 

print(search_insert(nums,target))