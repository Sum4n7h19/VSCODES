# Create a list based on sum of two consecutive pairs

numList = [1,2,3,4,5,6,7,8]

output = []

if len(numList) % 2 == 0:
    for i in range(0,len(numList)-1):
        sum = numList[i] + numList[i+1]
        output.append(sum)
        print(f'{i+1} consecutive sum is {sum}')
print(output)