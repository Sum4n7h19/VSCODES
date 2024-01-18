#Write a program to display numbers divisible by both 3 and 5 between the range of 0,100

for i in range(0,101):
    if i % 3 == 0 and i % 5 == 0:
        print(f'{i} is divisible by both 3 and 5')