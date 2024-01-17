# Python program to print the duplicate elements of an array
# Array 
weight = [10, 32, 23, 54, 54, 67, 76, 85, 67, 10]
# Importing counter module
from collections import Counter
# counting repeated numbers and storing in dictionary
d = Counter(weight)
print(d)
# Then creating a new list only with the repeated numbers using list comprehension
new_list = list([item for item in d if d[item]>1])
print(new_list)