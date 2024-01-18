# Write a program to identify matching value between two lists.

group_A = ['Sumanth', 'Sanjay', 'Divya', 'Nithya']
group_B = ['Divya', 'Harshitha', 'Sagar', 'Inchara']

common = []

for i in group_A:
    if i in group_B:
        common.append(i)
    
print(common)