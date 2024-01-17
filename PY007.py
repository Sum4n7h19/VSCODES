# Python Program to Check Leap Year

'''
A leap year is a year that contains an additional day,
February 29th, making it 366 days long instead of the usual 365 days.
Leap years are necessary to keep our calendar in alignment with the Earth’s revolutions around the Sun.
A year is a leap year if the following conditions are satisfied: 

The year is multiple of 400.

The year is a multiple of 4 and not a multiple of 100
'''
year = int(input("Enter a Year to Check Leap or Not ::: "))
if (year%400 == 0) or (year%4 == 0 and year%100 != 0):
    print("Leap")
else:
    print("Not Leap")