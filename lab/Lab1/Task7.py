fruits = ["Apple","Orange","grape"]
print(fruits)
fruits.append("banana")
print(fruits)
fruits.remove("banana")
print(fruits)
print(fruits[0])
print("orange "in fruits)
for fruit in fruits:
    print(fruit)
#tuples
number = (10,20,30)
value =number[0]
print(value)
value +=number[1]
print(value)
print("queue........")
queue = []
queue.append(10)
queue.append(20)
queue.append(30)
print("Queue:", queue)
queue.pop(0)
print("Queue after pop", queue)

print ("stack..")
stack = []
stack.append(10)
stack.append(20)
stack.append(30)
print("Stack:", stack)
stack.pop()
print("Stack after pop:", stack)

