numbers = []

for i in range(5):
    num = int(input("Enter a number: "))
    numbers.append(num)

total = 0

for n in numbers:
    total += n

average = total / len(numbers)

print("Sum:", total)
print("Average:", average)

t = tuple(numbers)
print("Tuple:", t)