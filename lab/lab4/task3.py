from collections import deque


def bfs_graph():
    graph = {}
    # enter number of nodes
    n = int(input("Enter the number of nodes: "))

    # Enter edges for each node
    for _ in range(n):
        node = input("Enter node name: ")
        neighbors = input(f"Enter neighbors for {node} (space separated): ").split()
        graph[node] = neighbors

    start_node = input("Enter the starting node: ")


    visited = set([start_node])
    queue = deque([start_node])

    print("BFS Traversal:")
    while queue:
        current = queue.popleft()
        print(current, end=" ")
        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


bfs_graph()