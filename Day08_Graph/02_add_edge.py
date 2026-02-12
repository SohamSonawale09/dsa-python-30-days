# Write a function to add an edge between two nodes.

graph = {}

def add_edge(u,v):
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
        
    graph[u].append(v)
    graph[v].append(u)
    
add_edge(1,2)
add_edge(1,3)
add_edge(2,3) 

print(graph)