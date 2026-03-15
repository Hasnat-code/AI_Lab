class NumberCheck:

    def __init__(self):
        self.num = 0

    def get_number(self):
        self.num = int(input("Enter a number: "))

    def check_numbers(self):
        if self.num % 2 == 0:
            print("Even numbers up to", self.num)
            for i in range(2, self.num + 1, 2):
                print(i)
        else:
            print("Odd numbers up to", self.num)
            for i in range(1, self.num + 1, 2):
                print(i)


obj = NumberCheck()
obj.get_number()
obj.check_numbers()