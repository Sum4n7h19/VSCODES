# Python Program to Print the Fibonacci sequence

stop = int(input('Enter a maximum value to stop fibonacci: '))

a = 0
b = 1
count = 0
while count < stop+1:
       print(a)
       nextValue = a + b
       # update values
       a = b
       b = nextValue
       count = count + 1