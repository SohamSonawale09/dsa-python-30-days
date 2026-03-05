# Problem

# For each day, find how many days until a warmer temperature. 

def daily_temperatures(arr):
    result = [0]*len(arr)

    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[j] > arr[i]:
                result[i] = j-i
                break

    return result 

arr = [73,74,75,71,69,72,76,73] 
print(daily_temperatures(arr))