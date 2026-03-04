# Problem

# Replace number with sum of squares of digits until:

# number becomes 1 → happy

# or loop occurs → not happy 

def happy_number(n):
    seen = set()

    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(i)**2 for i in str(n))

    return n == 1 
print(happy_number(19))