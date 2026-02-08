# Problem: Valid Parentheses
# Time Complexity: O(n)
# Space Complexity: O(n)

def isValid(s: str) -> bool:
    stack = []
    brackets = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in brackets:
            if not stack or stack[-1] != brackets[char]:
                return False
            stack.pop()
        else:
            stack.append(char)

    return not stack
print(isValid("()"))
print(isValid("()[]{}"))
print(isValid("(]"))
print(isValid("([)]"))
print(isValid("{[]}"))
