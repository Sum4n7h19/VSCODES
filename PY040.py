#Python program to print the largest element in an array

list_1 = [3,4,6,76,22,65,778,334]

large = 0

for number in list_1:
    if number > large:
        large = number

print(large)