# Print characters from a string that are present at an even index number
# For example, str = "python" so you should display ‘p’, ‘t’, ‘n’

text = 'Center for Geoinformatics Technology'
length = len(text)
print(length)

for index_pos in range(length):
    if index_pos % 2 == 0:
        print(text[index_pos])
