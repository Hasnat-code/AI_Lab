from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}


def bfs_to_list(graph, start_node):
    visited = set([start_node])
    queue = deque([start_node])
    traverse_order = []  # List to store results

    while queue:
        current = queue.popleft()
        traverse_order.append(current)  #

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    print(f"BFS Traversal: {traverse_order}")


bfs_to_list(graph, 'A')