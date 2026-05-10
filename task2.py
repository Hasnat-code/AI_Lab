import heapq

# Modified Graph from Task 2
graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('D', 4)],
    'C': [('E', 1), ('F', 6)],
    'E': [('G', 2)],
    'D': [], 'F': [], 'G': []
}

heuristics = {'A': 5, 'B': 6, 'C': 3, 'D': 7, 'E': 2, 'F': 1, 'G': 0}

def a_star_task2(graph, start, goal, h):
    pq = [(h[start], 0, start, [start])]
    
    while pq:
        f, g, current, path = heapq.heappop(pq)
        if current == goal:
            return path, g
        
        for neighbor, weight in graph.get(current, []):
            heapq.heappush(pq, (g + weight + h[neighbor], g + weight, neighbor, path + [neighbor]))

path, cost = a_star_task2(graph, 'A', 'G', heuristics)
print(f"Task 2 Results:")
print(f"Path: {path}")
print(f"Total Cost: {cost}")