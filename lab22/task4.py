class AreaCalculator:

    def calculate_area(self, shape, value1, value2=None):

        if shape == "circle":
            area = 3.1416 * value1 * value1
            print("Area of Circle:", area)

        elif shape == "rectangle":
            area = value1 * value2
            print("Area of Rectangle:", area)

        else:
            print("Invalid Shape")


shape = input("Enter shape (circle/rectangle): ")

obj = AreaCalculator()

if shape == "circle":
    radius = float(input("Enter radius: "))
    obj.calculate_area("circle", radius)

elif shape == "rectangle":
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    obj.calculate_area("rectangle", length, width)