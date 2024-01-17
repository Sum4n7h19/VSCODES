# Write a program to calculate Compound interest
# CI = P( 1 + r/n)^nt - P
'''P is the principal amount
r is the rate of interest(decimal obtained by dividing rate by 100)
n is the number of times the interest is compounded annually
t is the overall tenure.'''

p = int(input('Enter principal amount: '))
r= float(input('Enter rate of interest: '))
t = int(input('Enter the overall tenure: '))

Amount = p* (pow((1 + r / 100), t))
ci = Amount - p
print(f"Compound interest is {ci}")