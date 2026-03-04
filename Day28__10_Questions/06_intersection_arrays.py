# Problem

# Find the common elements between two arrays. 

nums1 = [1,2,2,1]
nums2 = [2,2]

# Output → [2] 

def intersection(nums1, nums2):
    result = []

    for num in nums1:
        if num in nums2 and num not in result:
            result.append(num)

    return result


nums1 = [1,2,2,1]
nums2 = [2,2]

print(intersection(nums1, nums2))