graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F']
}

# Heuristic values
heuristic = {
    'A': 6,
    'B': 4,
    'C': 3,
    'D': 5,
    'E': 2,
    'F': 0
}

start = 'A'
goal = 'F'


def hill_climbing(graph, heuristic, start, goal):

    current = start
    path = [current]

    while current != goal:

        neighbors = graph.get(current, [])

        # Stop if no neighbors
        if not neighbors:
            break

        # Select best neighbor
        next_node = min(neighbors, key=lambda x: heuristic[x])

        # Stop if no improvement
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