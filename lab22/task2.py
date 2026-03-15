class Calculator:

    def __init__(self):
        self.num1 = 0
        self.num2 = 0

    def get_numbers(self):
        self.num1 = float(input("Enter first number: "))
        self.num2 = float(input("Enter second number: "))

    def calculate(self):
        print("Sum:", self.num1 + self.num2)
        print("Difference:", self.num1 - self.num2)
        print("Product:", self.num1 * self.num2)
        print("Division:", self.num1 / self.num2)


obj = Calculator()
obj.get_numbers()
obj.calculate()