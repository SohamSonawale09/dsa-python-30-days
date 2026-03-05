# Problem

# Design a stack that can return the minimum element. 

class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        self.stack.pop()

    def get_min(self):
        return min(self.stack) 
    
st = MinStack()
st.push(10)
st.get_min()
print(st.get_min())