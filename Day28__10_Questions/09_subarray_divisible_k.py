# Problem

# Count subarrays whose sum is divisible by k. 

nums = [4,5,0,-2,-3,1]
k = 5
# Output → 7 

def subarray_divisible(nums,k):
    count = {0:1}
    total = 0
    res = 0

    for n in nums:
        total += n
        r = total % k

        if r in count:
            res += count[r]

        count[r] = count.get(r,0) + 1

    return res 
print(subarray_divisible(nums,k))