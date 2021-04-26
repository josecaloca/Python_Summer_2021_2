'''
Instructions:
Using recursion please write a function that will compute the total space occupied by a folder and its subfolders and files.
Please do not use os.walk or any other system command to return the size directly but implement it yourself. For reference you can see a version of the code that uses os.walk instead of recursion here: https://github.com/prubach/Python_Summer_2021_2/blob/master/space_occupied.py
Once you have that working correctly please add also counting of the number of files in that folder and all its subfolders
'''

import os

def space_occupied(f):
    total_size = os.path.getsize(f)
    for i in os.listdir(f):
        path = os.path.join(f, i)
        if os.path.isfile(path):
            total_size += os.path.getsize(path)
        else:
            if os.path.isdir(path):
              total_size += space_occupied(path)
    return total_size

# print(space_occupied('C:\abcdef'))
