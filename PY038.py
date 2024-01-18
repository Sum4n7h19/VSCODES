# Write a program to ask user to input 5 name and store it in a list.

totalItems = int(input('Enter total item you want to purchase: '))
itemList = []
for item in range(totalItems):
    itemName = input(f"Enter item {item + 1} name: ")
    itemList.append(itemName)

print(itemList)

