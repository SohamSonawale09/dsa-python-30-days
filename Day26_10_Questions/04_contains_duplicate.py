# 4 Contains Duplicate 

def duplicate(arr):
    
    no_dup = set()
    
    for num in arr:
        if num in no_dup:
            return True
        no_dup.add(num)
    
    return False

#Example
arr = [1, 2, 3, 4, 5, 2, 2]  
print(duplicate(arr))