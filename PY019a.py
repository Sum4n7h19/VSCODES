# Python program to swap two variables with temporary variable

a = 'Juice'
b = 'Water'
temp = ''
print('Before swaping')
print(f'a is {a}')
print(f'b is {b}')

temp = a
a = b
b = temp
print('After swaping using temporary variable')
print(f'a is {a}')
print(f'b is {b}')
