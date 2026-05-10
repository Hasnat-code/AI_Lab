import heapq

def user_input_astar():
    n = int(input("Enter number of nodes: "))
    graph = {}
    
    print("Enter edges (Source Destination Cost). Type 'done' to finish:")
    while True:
        line = input()
        if line.lower() == 'done': break
        u, v, w = line.split()
        if u not in graph: graph[u] = []
        graph[u].append((v, int(w)))

    print("Enter heuristics (Node Value):")
    h = {}
    for _ in range(n):
        node, val = input().split()
        h[node] = int(val)

    start = input("Start node: ")
    goal = input("Goal node: ")

    pq = [(h[start], 0, start, [start])]
    while pq:
        f, g, curr, path = heapq.heappop(pq)
        if curr == goal:
            print(f"Shortest Path: {path}")
            return
        for neighbor, weight in graph.get(curr, []):
            heapq.heappush(pq, (g + weight + h.get(neighbor, 0), g + weight, neighbor, path + [neighbor]))

user_input_astar()