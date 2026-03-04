# Problem

# Find the index of the first non-repeating character. 

s = "leetcode"
# Output → 0 

def first_unique_char(s):
    count = {}

    for c in s:
        count[c] = count.get(c,0) + 1

    for i,c in enumerate(s):
        if count[c] == 1:
            return i

    return -1 
print(first_unique_char(s))