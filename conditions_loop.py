p = True
q = False

if p and q:
    print('p and q = TRUE')
else:
    print('p and q = NOT TRUE')
# or

if p or q:
    print('p and q = TRUE')
else:
    print('p and q = NOT TRUE')

# xor

if p ^ q: # represented by ^
    print('p and q = TRUE')
else:
    print('p and q = NOT TRUE')

## loops
for i in range(5):
    print(i)

for i in range(10):
    if i==3:
        continue
    print(i)
    if i==7:
        break


def sum(a, b):
    return a + b

print(sum(100000,2))
