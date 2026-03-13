from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E', 'F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}


def bfs_graph(graph, start_node):
    visited = set([start_node])
    queue = deque([start_node])

    print("BFS Output Order:")
    while queue:
        current = queue.popleft()
        print(current, end=" ")

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


bfs_graph(graph, 'A')