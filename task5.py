def check_existence(graph, start, goal):
    # Using a simple set for tracking visited nodes to find any valid path
    visited = set()
    stack = [start]
    
    while stack:
        node = stack.pop()
        if node == goal:
            return "Path Exists"
        if node not in visited:
            visited.add(node)
            # Add neighbors to stack
            neighbors = [edge[0] for edge in graph.get(node, [])]
            stack.extend(neighbors)
            
    return "Path Does Not Exist"

# Using graph from Task 2 as example
test_graph = {'A': [('B', 2)], 'B': [], 'C': [('D', 1)]}
print(f"Start: A, Goal: B -> {check_existence(test_graph, 'A', 'B')}")
print(f"Start: A, Goal: D -> {check_existence(test_graph, 'A', 'D')}")