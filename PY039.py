# Write a program to convert two lists into a dictionary as Key Value pairs

Keys = ['Name', 'Adress', 'Age']
Values = ['Sumanth', 'Mysore', 23]

INFO = {}

if len(Keys) == len(Values):
    list_length = len(Keys)
    for i in range(list_length):
        INFO[Keys[i]] = Values[i]

print(INFO)