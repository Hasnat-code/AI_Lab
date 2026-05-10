graph = {}

n = int(input("Enter number of nodes: "))

for i in range(n):
    node = input("Enter node name: ")

    neighbors = input(f"Enter neighbors of {node}: ").split()

    graph[node] = neighbors

heuristic = {}

m = int(input("Enter number of heuristic values: "))

for i in range(m):
    node = input("Node: ")
    value = int(input("Heuristic value: "))

    heuristic[node] = value

start = input("Enter start node: ")
goal = input("Enter goal node: ")


def hill_climbing(graph, heuristic, start, goal):

    current = start

    path = [current]

    while current != goal:

        neighbors = graph.get(current, [])

        if not neighbors:
            break

        next_node = min(neighbors, key=lambda x: heuristic[x])

        if heuristic[next_node] >= heuristic[current]:
            break

        current = next_node

        path.append(current)

    print("\nPath:", path)

    print("Final Heuristic Value:", heuristic[current])

    if current == goal:
        print("Reached")
    else:
        print("Not Reached")


hill_climbing(graph, heuristic, start, goal)