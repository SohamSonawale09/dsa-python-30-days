# Problem Statement:
# Given two strings s and t, return True if they are equal when both are typed into empty text editors.

def backspaceCompare(s, t):
    def build(text):
        stack = []
        for ch in text:
            if ch == '#':
                if stack:
                    stack.pop()
            else:
                stack.append(ch)
        return stack

    return build(s) == build(t)


print(backspaceCompare("ab#c", "ad#c"))  # True
print(backspaceCompare("a#c", "b"))      # False
