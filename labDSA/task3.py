from collections import deque

stack = []

stack.append(10)
stack.append(20)
stack.append(30)

print("Stack after push:", stack)

stack.pop()

print("Stack after pop:", stack)

queue = deque()

queue.append(10)
queue.append(20)
queue.append(30)

print("Queue after enqueue:", queue)

queue.popleft()

print("Queue after dequeue:", queue)