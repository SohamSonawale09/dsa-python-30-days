# Two sum problem 
def two_sum(arr,target):
    arr1 = {}
    
    for i in range(len(arr)):
        value = target - arr[i]
        
        if value in arr1:
            return [arr1[value],i]
        
        arr1[arr[i]] = i

# Example
arr = [5, 3, 10, 2, 8]
target = 13

print(two_sum(arr, target))    