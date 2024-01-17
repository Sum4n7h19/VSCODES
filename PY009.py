# Write a program to calculate Simple interest
# simple Interst = principal amount * time * rate of interest / 100

p =int(input('Enter Principal amount: '))
t = int(input('Enter time in Years: '))
r = float(input('Enter rate of interest: '))

si = (p*t*r)/100
print(f"Simple interest is {si}")
