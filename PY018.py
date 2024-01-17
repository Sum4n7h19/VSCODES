# Program to generate summation of number between two numbers

lowerValue = int(input('Enter lower value: '))
upperValue = int(input('Enter upper value: '))
sum = 0

for num in range(lowerValue, upperValue+1):
    sum = sum + num
print(sum)