import os
#Specify the directory you want to list
directory_path='/'
#List all files and directory in the specified path
contents=os.listdir(directory_path)
for item in contents:
    print(item)