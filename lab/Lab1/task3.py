age=int(input("Enter your age: "))
nationality=input("Enter your nationality: ")
if nationality=="Pakistani":
    if age>=18:
        print("You are eligible for vote")
    else:
        print("You are not eligible for vote due to age")
else:
    print("You are not eligible for vote due to nationality")