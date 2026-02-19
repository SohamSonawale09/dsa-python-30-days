# Problem Statement:

# Count number of swaps performed in Selection Sort. 

arr = [64, 25, 12, 22, 11]
swaps = 0
n = len(arr)

for i in range(n):
    min_index = i

    for j in range(i + 1, n):
        if arr[j] < arr[min_index]:
            min_index = j

    if i != min_index:
        arr[i], arr[min_index] = arr[min_index], arr[i]
        swaps += 1

print(arr)
print("Swaps:", swaps)
