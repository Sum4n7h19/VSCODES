# Create a program to check Euclidean Distance between consecutive points

coordinate1 = (1,2)
coordinate2 = (8,9)
# Collecting coordinate x and y
x1 = coordinate1[0]
x2 = coordinate2[0]

y1 = coordinate1[1]
y2 = coordinate2[1]

# Finding difference between coordinates x and y
diff_x = (x2 - x1)**2
diff_y = (y2 - y1)**2

# Applying eucledian formula
distance = (diff_x + diff_y)**0.5

print(distance)
