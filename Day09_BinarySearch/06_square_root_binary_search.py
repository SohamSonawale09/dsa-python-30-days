# Problem

# Find integer square root of a number. 
def sqrt_binary(n):
    left = 1
    right = n
    answer = 0

    while left <= right:
        mid = (left + right) // 2

        if mid * mid == n:
            return mid
        elif mid * mid < n:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

    return answer


print(sqrt_binary(20))