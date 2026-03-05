# Problem

# You can climb 1 or 2 steps.
# Find total ways to reach step n. 

def climb_stairs(n):
    if n <= 2:
        return n

    a,b = 1,2
    for i in range(3,n+1):
        a,b = b,a+b

    return b 
n = 3
print(climb_stairs(n))