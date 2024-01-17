# Python program to broadcast matematical operation into an array

list_1 = [1,2,3,4,5,6,7,8,9]
list_2 = []
for i in list_1:
    temp = i*2
    list_2.append(temp)
print(list_2)
# List comprehension
list_3 = [i*3 for i in list_1]
print(list_3)