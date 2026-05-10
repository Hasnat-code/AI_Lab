import _heapq
import heapq
from collections import deque
def bfs(graph, start):
    visited=set()
    queue=[start]
    while queue:
        node=queue.pop()
        if node not in visited:
            print(node,end=" ")
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
def dfs(graph, start):
    visited=set()
    stack=[start]
    while stack:
        node=stack.pop()
        if node not in visited:
            print(node,end=" ")
            visited.add(node)
            for neighbor in graph[node]:
                stack.append(neighbor)

def ucs(graph1,start,goal):
    visited=set()
    priority_queue=[(0,start)]
    while priority_queue:
        cost , node = heapq.heappop(priority_queue)
        if node not in visited:
            print(node ,  cost)
            visited.add(node)
            if node==goal:
                return
            for neihbour ,weight in graph1[node]:
                heapq.heappush(priority_queue,(cost+weight,neihbour))


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}
graph1 = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 1)],
    'D': [],
    'E': [],
    'F': []
}
bfs(graph,"A")
dfs(graph,"A")

ucs(graph1,"A","E")
l=[1,2,3,4,5,5,5,5]
print(l)
s={1,2,3,3,4,4,4}
print(s)
t=1,2
print(t)
t1="String","ali","ali"
print(t1)
d={
    "name":"ali"

}
d["name"]="hasnat"
print(d)

def insertnumber(ds,number):
    ds.append(number)
    print(number)
def removernumber(ds,number):
    ds.remove(number)
    print(number)
def searchnumber(ds,number):
    if number in ds:
        index=ds.index[number]
        return index
    else:
        return -1
def updatenumber(ds,number,number1):
    if number in ds:
        index=ds.index(number)
        ds[index]=number1
    else:
        print("numbern not found..")
product=[]
insertnumber(product,1)
def ucsgraph(graph,start,goal):
    visited=set()
    pq=heapq.heappush[(0,start)]
    while pq:
        cost,node=heapq.heappop(pq)
        if node not in visited:
            print(node,end=" ")
            visited.add(node)
            if node==goal:
                return
            for neighbor ,weight in graph[node]:
                heapq.heappush(pq,(cost+weight,neighbor))
graphforucs = {}
n = int(input("Enter number of nodes: "))
for _ in range(n):
    node = input("Enter node name: ")
    graphforucs[node] = []
    e = int(input(f"  How many edges from '{node}'? "))
    for _ in range(e):
        neighbor = input("    Neighbor node: ")
        weight   = int(input("    Edge weight:   "))
        graphforucs[node].append((neighbor, weight))

start = input("Enter starting node: ")
ucs(graphforucs, start)