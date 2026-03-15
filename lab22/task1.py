class Person:

    def __init__(self):
        self.name = ""
        self.age = 0

    def get_data(self):
        self.name = input("Enter your name: ")
        self.age = int(input("Enter your age: "))

    def display(self):
        print(f"Hello {self.name}, you are {self.age} years old!")


obj = Person()
obj.get_data()
obj.display()