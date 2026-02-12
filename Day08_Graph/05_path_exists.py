graph = {
    1: [2, 3],
    2: [1, 4],
    3: [1],
    4: [2]
}

visited = set()

def path_exists(start, end):
    if start == end:
        return True
    
    visited.add(start)
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            if path_exists(neighbor, end):
                return True
    
    return False

print(path_exists(1, 4))  
