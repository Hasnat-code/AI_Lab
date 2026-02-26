number = int(input("Enter a number to reverse: "))
reverse = 0

while number != 0:
    number1 = number % 10
    reverse = int(reverse * 10 + number1)
    number = number // 10

print("The reverse is", reverse)