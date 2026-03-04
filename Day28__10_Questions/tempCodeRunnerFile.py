nums = [1,1,1,2,2,3]
k = 2
# Output → [1,2] 

from collections import Counter

def top_k(nums,k):
    count = Counter(nums)
    return [x for x,_ in count.most_common(k)]

top_k(nums,k)