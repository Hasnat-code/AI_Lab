Year=int(input("Enter the Year: "))
if Year%4==0 and Year%100!=0 or Year%400==0:
    print("The year ,Year, is leap year")
