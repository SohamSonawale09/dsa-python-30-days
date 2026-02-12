graph = {
    1: [2, 3],
    2: [1, 4],
    3: [1],
    4: [2]
}

visited = set()

def dfs(node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        
        for neighbor in graph[node]:
            dfs(neighbor)

dfs(1)
