# Problem: Two Sum using Hash Table
# Time Complexity: O(n)
# Space Complexity: O(n)

arr = [2, 7, 11, 15]
target = 9

seen = {}

for num in arr:
    remaining = target - num
    if remaining in seen:
        print("Pair exists:", remaining, "+", num, "=", target)
        break
    else:
        seen[num] = True
