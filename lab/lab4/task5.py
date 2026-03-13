from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}


def bfs_search(graph, start_node, target):
    visited = set([start_node])
    queue = deque([start_node])

    while queue:
        current = queue.popleft()

        if current == target:
            return True  #found

        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return False


search_target = input("Enter node to search: ")
if bfs_search(graph, 'A', search_target):
    print("Node Found..")
else:
    print("Node Not Found...")