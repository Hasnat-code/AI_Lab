class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print("Name:", self.name)
        print("Age:", self.age)


student1 = Student("Ali", 20)
student2 = Student("Sara", 21)

student1.show_info()
print()
student2.show_info()