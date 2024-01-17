# Write a program to calculate GST
# GST for gold is 3%
from datetime import date
today = date.today()

grams = float(input("Enter total gold in grams: "))
goldPrice = int(input(f"Enter gold rate per gram as on {today}: "))
totalPrice = grams*goldPrice
print(f'Total price for gold:{totalPrice}')
gst= (totalPrice/100)*3
print(f'GST for {totalPrice} is: {gst}')
grandTotal = totalPrice + gst
print(f'Total invoice amount: {grandTotal}')