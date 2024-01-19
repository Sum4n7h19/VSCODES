#Python program to print the smallest element in an array

list_1 = [3,6,8,2,45,8,23,89,12,87,1]

small = list_1[0]

for number in list_1:
    if number < small:
        small = number

print(small)