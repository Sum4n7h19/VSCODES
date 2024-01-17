# Calculate the BMI of a person
#  BMI = mass(kg)/height^2(m)

name =input('Enter a name: ')
weight = float(input(f'Enter weight in kg of {name}: '))
height = float(input(f'Enter height in meters of {name}: '))

bmi = weight/(height*height)
print(f'BMI value of {name} is {bmi}')

if bmi < 18.49:
    print(f'{name} is underweight')
elif bmi >= 18.49 and bmi < 24.99:
    print(f'{name} is normal weight')
elif bmi >= 24.99 and bmi <29.99:
    print(f'{name} is overweight')
else:
    print(f'{name} is obese')