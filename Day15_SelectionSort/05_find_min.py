# Problem Statement:

# Print minimum element found in each pass of Selection Sort. 

arr = [64, 25, 12, 22, 11]
n = len(arr)

for i in range(n):
    min_index = i

    for j in range(i + 1, n):
        if arr[j] < arr[min_index]:
            min_index = j

    print("Minimum found:", arr[min_index])

    arr[i], arr[min_index] = arr[min_index], arr[i]

print(arr)
