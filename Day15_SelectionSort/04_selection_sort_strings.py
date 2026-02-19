# Problem Statement:

# Sort list of strings alphabetically using Selection Sort. 

def selection_sort_strings(arr):
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


arr = ["banana", "apple", "cherry"]
print(selection_sort_strings(arr))
