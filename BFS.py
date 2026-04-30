<<<<<<< HEAD
from collections import deque
def bfs(start,goal):
    visited = set([start])
    queue = deque([start])
    print(f"Starting node {start}")
    while queue:
        current_node=queue.popleft()
        print(current_node,end=" ")
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)



graph={
    'A':['B','C'],
    'B':['A','D','E'],
    'C':['A','F'],
    'D':['B'],
    'E':['B','F'],
    'F':['C','E']
}
=======
from collections import deque
def bfs(start,goal):
    visited = set([start])
    queue = deque([start])
    print(f"Starting node {start}")
    while queue:
        current_node=queue.popleft()
        print(current_node,end=" ")
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)



graph={
    'A':['B','C'],
    'B':['A','D','E'],
    'C':['A','F'],
    'D':['B'],
    'E':['B','F'],
    'F':['C','E']
}
>>>>>>> 59c8556ed6afbdb60124e6b12386f0a3daac85a3
bfs('A','E')