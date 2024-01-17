# Python Program to Check Leap Year

'''
A leap year is a year that contains an additional day,
February 29th, making it 366 days long instead of the usual 365 days.
Leap years are necessary to keep our calendar in alignment with the Earth’s revolutions around the Sun.
A year is a leap year if the following conditions are satisfied: 

The year is multiple of 400.

The year is a multiple of 4 and not a multiple of 100
'''
years_list = [2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010]
for year in years_list:
    if (year%400 == 0) or (year%4 == 0 and year%100 != 0):
        print(f"{year} is Leap")
    else:
        print(f"{year} is Not Leap")