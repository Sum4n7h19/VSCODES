# Program to create a guessing game
import random

myChoice = int(input('Choose a number between 1 to 5: \n'))
# Declaring choices
cards = [1,2,3,4,5]

# Selecting random choice
systemChoice = random.choice(cards)
if myChoice == systemChoice:
    print(f"System choice is {systemChoice}")
    print('Correctly guessed the number')
else:
    print(f"System choice is {systemChoice}")
    print('Wrongly guessed the number')
