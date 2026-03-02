# 5 Product of Array Except Self 


def product_except_self(arr):
    result = []
    
    for i  in range(len(arr)):
        product = 1
        for j in range(len(arr)):
            if i != j:
                product = product * arr[j]
        result.append(product)
        
    return result
# Example
arr = [1,2,3,4]
print(product_except_self(arr))