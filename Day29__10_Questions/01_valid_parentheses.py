# Input: "()[]{}"
# Output: True 

def valid_parentheses(s):
    stack = []
    pairs = {')':'(', ']':'[', '}':'{'}

    for c in s:
        if c in pairs.values():
            stack.append(c)
        elif stack and stack[-1] == pairs[c]:
            stack.pop()
        else:
            return False

    return len(stack) == 0 
s = ()
print(valid_parentheses(s))