# DFS -> go deep first
def dfs_example(n):
    if n == 0:
        return
    print(n)
    dfs_example(n-1)

dfs_example(3)


# BFS idea (queue concept)
from collections import deque

q = deque([1, 2, 3])

while q:
    print(q.popleft())

print("BFS & DFS Concept Revised ✅")