
# Problem Statement:
# You are given two arrays:

# nums1 (a subset of nums2)

# nums2
# For each element in nums1, find the next greater element in nums2.
 
def nextGreaterElement(nums1, nums2):
    stack = []
    store = {}

    for n in nums2:
        # if current number is bigger than stack top
        while stack and n > stack[-1]:
            store[stack.pop()] = n
        stack.append(n)

    # remaining elements have no greater value
    for n in stack:
        store[n] = -1

    # build answer for nums1
    return [store[n] for n in nums1]

nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]

print(nextGreaterElement(nums1, nums2))
