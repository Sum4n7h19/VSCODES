# Python program to convert kilometers to miles
# 1 mile = 1.60934km

value = int(input("Enter value 1: To convert Km to Mile \nEnter value 2: To convert Mile to Km \n"))
if value==1:
    print("You have Selected :: Km to Mile Conversion")
    km = float(input("Enter Kilometer: "))
    km2mile = km / 1.609
    print(f"Equivalent value of {km} kms is {round(km2mile,2)} miles")
elif value==2:
    print("You have Selected :: Mile to Km Conversion")
    mile = float(input("Enter Mile: "))
    mile2km = mile * 1.609
    print(f"Equivalent value of {mile} miles is {round(mile2km,2)} Km")
else:
    print("You have entered invalid input")