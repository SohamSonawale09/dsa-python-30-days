# Problem: Count character frequency in a string
# Time Complexity: O(n)
# Space Complexity: O(n)

s = "apple"

d = {}

for ch in s:
    if ch in d:
        d[ch] += 1
    else:
        d[ch] = 1

print(d)
