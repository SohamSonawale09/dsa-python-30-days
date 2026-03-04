# Problem

# Find the longest sequence of consecutive numbers.  

nums = [100,4,200,1,3,2]
# Output → 4 

def longest_consecutive(nums):
    s = set(nums)
    longest = 0

    for n in s:
        if n-1 not in s:
            length = 1
            while n+length in s:
                length += 1
            longest = max(longest,length)

    return longest 

print(longest_consecutive(nums))