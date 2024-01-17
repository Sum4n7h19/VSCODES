# Python program to generate a random number
import random
# Declaring variables
num = int(input("Enter total number of random number you want to generate: "))
randomList = [] 

# Iterating through range of numbers
for i in range(1,num+1):
    rand = random.randint(1,100)
    randomList.append(rand)
print(randomList)