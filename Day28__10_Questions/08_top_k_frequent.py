# Problem

# Return the k most frequent numbers in the array.


nums = [1,1,1,2,2,3]
k = 2
# Output → [1,2] 

def top_k(nums, k):
    freq = {}

    # count frequency
    for n in nums:
        freq[n] = freq.get(n, 0) + 1

    # sort by frequency
    sorted_nums = sorted(freq, key=freq.get, reverse=True)

    return sorted_nums[:k]


nums = [1,1,1,2,2,3]
k = 2

print(top_k(nums, k))