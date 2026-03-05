# Problem

# Implement a queue using stack operations. 

class MyQueue:

    def __init__(self):
        self.stack = []

    def push(self,x):
        self.stack.append(x)

    def pop(self):
        return self.stack.pop(0)

    def peek(self):
        return self.stack[0]

    def empty(self):
        return len(self.stack)==0 
qu = MyQueue()

qu.push(20)
print(qu.peek())