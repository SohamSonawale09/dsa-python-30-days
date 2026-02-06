# Problem: Reverse an array
# Description: Reverse the elements of the array using an extra list
# Time Complexity: O(n)
# Space Complexity: O(n)

l = [1,2,45,6,7,0,9]
l1 = []
while l:
    l1.append(l.pop())
print(l1)