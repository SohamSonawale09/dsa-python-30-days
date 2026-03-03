# 6 Subarray Sum Equals K 

def subarraySum(nums, k):
    count = 0
    total = 0
    seen = {0: 1}

    for num in nums:
        total += num

        if total - k in seen:
            count += seen[total - k]

        if total in seen:
            seen[total] += 1
        else:
            seen[total] = 1

    return count


print(subarraySum([1,1,1], 2))