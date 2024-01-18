#Write a program to print string “Python” as “Pyyttthhhhooooonnnnnn”
text = 'Python'
length = len(text)


for i in range(length):
    print(text[i]*(i+1), end='')

    