# write a program to convert degree,minutes,seconds into decimal degree

degree = int(input('Enter degree: '))
minutes = int(input('Enter minutes: '))
seconds = float(input('Enter seconds: '))

if minutes < 60 and seconds < 60:
    dd = degree + (minutes/60) + (seconds/3600)
    print(f'The Decimal degree is {dd}')
else:
    print('Invalid input')
    


