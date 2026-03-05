# Problem

# Compare two strings after applying backspace (#). 

def backspace_compare(s,t):
    def build(string):
        stack=[]
        for c in string:
            if c == "#":
                if stack:
                    stack.pop()
            else:
                stack.append(c)
        return "".join(stack)

    return build(s) == build(t) 

s = "ab#c"
t = "ad#c"

print(backspace_compare(s,t))