print("inheritence.....")
class Parent:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(self.name," can speak")
class Child(Parent):
    def speak(self):
        print(self.name," is studying")

person = Parent("Sara")
person.speak()
person=Child("Ali")
person.speak()

#polymorphism
print("polymorphism....")
class  Animal:
    def speak(self):
        print("some sound")
class Dog(Animal):
    def speak(self):
        print("dog sound")
class Cat(Animal):
    def speak(self):
        print("cat sound")
animal = Dog()
animal.speak()
animal = Cat()
animal.speak()

