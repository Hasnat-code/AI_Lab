graph = {}

n = int(input("Enter number of nodes: "))

# Input edges
for i in range(n):
    node = input("Enter node name: ")

    neighbors = input(f"Enter neighbors of {node} separated by space: ").split()

    graph[node] = neighbors

# Input heuristic values
heuristic = {}

m = int(input("Enter number of heuristic entries: "))

for i in range(m):
    node = input("Node: ")
    value = int(input("Heuristic value: "))

    heuristic[node] = value

# Start and Goal
start = input("Enter start node: ")
goal = input("Enter goal node: ")


def hill_climbing(graph, heuristic, start, goal):

    current = start

    print("\nPath:")

    while current != goal:

        print(current, end=" -> ")

        neighbors = graph.get(current, [])

        if not neighbors:
            break

        next_node = min(neighbors, key=lambda x: heuristic[x])

        # Stop if no improvement
        if heuristic[next_node] >= heuristic[current]:
            break

        current = next_node

    print(current)

    if current == goal:
        print("Goal Reached")
    else:
        print("Goal Not Reached")


hill_climbing(graph, heuristic, start, goal)