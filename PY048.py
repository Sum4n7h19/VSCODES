# Create 10 folders using OS module

import os
# Returns the current working directory
dir = os.getcwd()
print(dir)

for i in range(1,11):
    os.mkdir(f"{dir}/Test_{i}")
