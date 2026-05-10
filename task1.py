import heapq

# Graph representation from Task 1
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 1)],
    'D': [], 'E': [], 'F': []
}

# Defining an admissible heuristic (estimated cost to F)
heuristics = {'A': 3, 'B': 4, 'C': 1, 'D': 5, 'E': 2, 'F': 0}

def a_star(graph, start, goal, h):
    pq = [(h[start], 0, start, [start])]  # (priority, cost, current_node, path)
    
    while pq:
        f, g, current, path = heapq.heappop(pq)
        
        if current == goal:
            return path, g
        
        for neighbor, weight in graph.get(current, []):
            new_g = g + weight
            new_f = new_g + h[neighbor]
            heapq.heappush(pq, (new_f, new_g, neighbor, path + [neighbor]))

path, cost = a_star(graph, 'A', 'F', heuristics)
print(f"Task 1 Path: {path}, Total Cost: {cost}")