# Python Program to Find the Factorial of a Number
# If input is 5 then 5x4x3x2x1 output 120

num = int(input("Enter the factorial number: "))
product = 1

for i in range(1,num+1):
    product = i * product
print(product)