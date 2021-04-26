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
