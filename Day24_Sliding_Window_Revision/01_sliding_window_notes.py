# Sliding Window:
# Used for subarray / substring problems

# Instead of checking all subarrays,
# we move a window step by step.

# Example Idea:
arr = [1, 2, 3, 4, 5]

window_sum = sum(arr[0:3])
print("First window sum:", window_sum)

# Move window forward
window_sum += arr[3] - arr[0]
print("Next window sum:", window_sum)

print("Sliding Window Concept Revised ✅")