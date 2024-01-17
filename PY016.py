# Python Program to Display the multiplication Table
num = int(input("Enter a number which you want to generate multiplication table: "))

for value in range(1,11):
    print(f'{num}x{value}={num*value}\n')