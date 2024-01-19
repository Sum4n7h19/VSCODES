#  list all folders in current directory and rename it using OS module

import os
# Returns the current working directory
dir = os.getcwd()
list_dir = os.listdir(dir)

for i in list_dir:
    if i.startswith('Test'):
        try:
            temp = i[4:]
            newName = 'mycode' + temp
            os.rename(i, newName)
        except:
            pass