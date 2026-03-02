# 8 Move Zeroes

arr = [0,1,2,3,4,5]

def move(arr):
    pos = 0
    
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[pos],arr[i] = arr[i],arr[pos]
            pos+=1
            
    return arr

arr = [0,1,0,3,12]
print(move(arr))    