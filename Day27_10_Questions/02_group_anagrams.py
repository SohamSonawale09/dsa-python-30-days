# 2 Group Anagrams
def groupAnagrams(strs):
    groups = {}
    
    for word in strs:
        key = "".join(sorted(word))   # sort word
        
        if key in groups:
            groups[key].append(word)
        else:
            groups[key] = [word]
    
    return list(groups.values())


print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))