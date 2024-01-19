# OS module

import os
# Returns the current working directory
dir = os.getcwd()
print(dir)

# os.mkdir("C:/Users/wwwsu/Documents/VSCODES/Test")

os.mkdir(f"{dir}/Test1")
