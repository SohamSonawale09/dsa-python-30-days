# Problem: Count frequency of elements in a list using dictionary
# Time Complexity: O(n)
# Space Complexity: O(n)

l = [1, 2, 2, 3, 3, 3]

d = {}

for i in l:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

print(d)