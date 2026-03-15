numbers = list(map(int, input("Enter numbers separated by space: ").split()))

key = int(input("Enter number to search: "))

found = False

for n in numbers:
    if n == key:
        found = True
        break

if found:
    print("Found using Linear Search")
else:
    print("Not found using Linear Search")

numbers = sorted(numbers)

low = 0
high = len(numbers) - 1
found = False

while low <= high:
    mid = (low + high) // 2

    if numbers[mid] == key:
        found = True
        break
    elif numbers[mid] < key:
        low = mid + 1
    else:
        high = mid - 1

if found:
    print("Found using Binary Search")
else:
    print("Not found using Binary Search")