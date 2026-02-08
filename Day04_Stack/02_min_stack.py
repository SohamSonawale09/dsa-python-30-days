
# Problem Statement:
# Design a stack that supports the following operations in O(1) time:

# push(x)

# pop()

# top()

# getMin() → returns the minimum element in the stack 

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, x):
        self.stack.append(x)

        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self):
        x = self.stack.pop()
        if x == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]

s = MinStack()

s.push(-2)
s.push(0)
s.push(-3)

print(s.getMin())  

s.pop()

print(s.top())    
print(s.getMin())   
