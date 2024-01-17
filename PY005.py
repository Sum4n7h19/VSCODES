# Python Program to Check if a Number is Positive, Negative or Zero
# Logic::: a > 0 = positive, a < 0 = Negative, a = 0 then Zero


value = float(input("Enter a Number ::: "))
if value > 0:
    print(f"{value} is Positive Number")
elif value < 0:
    print(f"{value} is Negative Number")
else:
    print(f"{value} is Zero Number")