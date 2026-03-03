# 10 Squares of a Sorted Array 

def sortedSquares(nums):
    result = []

    for num in nums:
        result.append(num * num)

    result.sort()
    return result


print(sortedSquares([-4,-1,0,3,10]))