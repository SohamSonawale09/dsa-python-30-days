# Problem

# Find longest substring with at most k different characters. 

s = "eceba"
k = 2
# Output → 3 

def longest_k_distinct(s,k):
    count = {}
    left = 0
    max_len = 0

    for right in range(len(s)):
        count[s[right]] = count.get(s[right],0) + 1

        while len(count) > k:
            count[s[left]] -= 1
            if count[s[left]] == 0:
                del count[s[left]]
            left += 1

        max_len = max(max_len,right-left+1)

    return max_len 
print(longest_k_distinct(s,k))