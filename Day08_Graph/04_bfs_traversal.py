# Problem Statement
# Traverse graph level by level using queue.

from collections import deque

graph = {
    1 : [2,3],
    2 : [1,4],
    3: [1],
    4: [2]
} 

visited = set()
queue = deque([1])

while queue:
    node = queue.popleft()
    
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        
    for neighbor in graph[node]:
        queue.append(neighbor)