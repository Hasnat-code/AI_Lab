graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E', 'F'],
    'E': ['G']
}

# Heuristic values
heuristic = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 8,
    'E': 2,
    'F': 5,
    'G': 0
}

start = 'A'
goal = 'G'


def hill_climbing(graph, heuristic, start, goal):

    current = start
    path = [current]

    while current != goal:

        neighbors = graph.get(current, [])

        # Stop if no neighbors
        if not neighbors:
            break

        # Choose node with smallest heuristic value
        next_node = min(neighbors, key=lambda x: heuristic[x])

        # Stop if no better node exists
        if heuristic[next_node] >= heuristic[current]:
            break

        current = next_node
        path.append(current)

    print("Path:", path)
    print("Final Node:", current)
    print("Final Heuristic Value:", heuristic[current])

    if current == goal:
        print("Goal Reached")
    else:
        print("Goal Not Reached")


hill_climbing(graph, heuristic, start, goal)