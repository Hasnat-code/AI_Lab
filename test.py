Unit_Consumed=int(input("Enter the unit consumed: "))
if Unit_Consumed>=100:
    rateperunit=5
elif Unit_Consumed>100 and Unit_Consumed<=200:
    rateperunit=7

elif Unit_Consumed>200 and Unit_Consumed<=300:
    rateperunit=10
elif Unit_Consumed>300:
    rateperunit=15
total_Bill = Unit_Consumed * rateperunit
print("The unit consumed is : ", Unit_Consumed, " rate per unit: ", rateperunit, " total bill: ", total_Bill)


