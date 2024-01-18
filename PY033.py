#Write a function to perform simple calculator using if-elif-else.

# Function defination
def calc(num1,num2,operator):
    if operator == 'Sum':
        print(num1 + num2)
    elif operator == 'Sub':
        print(num1 - num2)
    elif operator == 'Prod':
        print(num1 * num2)
    elif operator == 'Divi':
        print(num1 / num2)
    else:
        print('Enter valid operator')

# Calling the function
calc(33,22,'Divi')