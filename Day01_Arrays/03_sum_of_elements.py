# Problem: Find the sum of all elements in an array
# Description: Given an array of integers, calculate and return the sum
# of all its elements by traversing the array once.

ls = [2,3,4,5,6,74,12,34]
total = 0
for i in ls:
    total = total + i
print(total)