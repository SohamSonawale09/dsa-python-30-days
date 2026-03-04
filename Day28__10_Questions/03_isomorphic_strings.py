# Problem

# Check if two strings follow the same character mapping. 

s = "egg"
t = "add"
# Output → True 

def isomorphic(s,t):
    map1 = {}
    map2 = {}

    for a,b in zip(s,t):
        if map1.get(a,b) != b or map2.get(b,a) != a:
            return False
        map1[a] = b
        map2[b] = a

    return True 

print(isomorphic(s,t))