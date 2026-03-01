# Two Pointer:
# Use two indices to traverse array

# Mostly used when array is sorted

arr = [1, 2, 3, 4, 6]
target = 6

left = 0
right = len(arr) - 1

while left < right:
    current_sum = arr[left] + arr[right]

    if current_sum == target:
        print("Pair found:", arr[left], arr[right])
        break
    elif current_sum < target:
        left += 1
    else:
        right -= 1

print("Two Pointer Concept Revised ✅")