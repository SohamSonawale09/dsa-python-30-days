# HashMap (Dictionary in Python)

# Stores key-value pairs
# Average Time Complexity -> O(1)

nums = [1, 1, 2, 3, 3, 3]

frequency = {}

for n in nums:
    frequency[n] = frequency.get(n, 0) + 1

print("Frequency Count:", frequency)

# When to Use HashMap:
# - Frequency counting
# - Duplicate checking
# - Fast lookup

# Important Problems:
# - Two Sum (HashMap)
# - Valid Anagram
# - Top K Frequent Elements

print("HashMap Revision Completed ✅")