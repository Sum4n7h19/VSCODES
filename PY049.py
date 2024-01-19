# list all folders in current directory and delete it using OS module

import os
# Returns the current working directory
dir = os.getcwd()
list_dir = os.listdir(dir)

for i in list_dir:
    if i.startswith('mycode'):
        try:
            os.rmdir(i)
        except:
            pass