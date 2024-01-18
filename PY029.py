#Write a program to split odd and even numbers and store in a seperate list respectively?

age = [10,32,43,20,46,13,16,82,71,23,54,15]

oddAge = []
evenAge = []

for i in age:
    if i % 2 == 0:
        evenAge.append(i)
    else:
        oddAge.append(i)

print(oddAge)
print(evenAge)