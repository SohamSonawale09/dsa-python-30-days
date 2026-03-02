# 10 Longest Substring Without Repeating Characters 

def longest_substring(s):
    chars = set()
    start = 0
    max_len = 0

    for end in range(len(s)):

        while s[end] in chars:
            chars.remove(s[start])
            start += 1

        chars.add(s[end])
        max_len = max(max_len, end - start + 1)

    return max_len


s = "abcabcbb"
print(longest_substring(s))