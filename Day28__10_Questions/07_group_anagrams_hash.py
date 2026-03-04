# Problem

# Group words that are anagrams. 

# Example
strs = ["eat","tea","tan","ate","nat","bat"] 

from collections import defaultdict

def group_anagrams(strs):
    d = defaultdict(list)

    for word in strs:
        key = "".join(sorted(word))
        d[key].append(word)

    return list(d.values()) 
print(group_anagrams(strs))