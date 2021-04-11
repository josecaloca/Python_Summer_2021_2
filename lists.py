li = [1232, 2323, 23435, 2356, 876, 98989]

print(li)

for elements in li: # print each element of the list
    #print(elements)
    #print(li.index(elements))
    print('Element: %i at position: %s' % (elements, li.index(elements))) # problem with duplicates

li.sort()
print()
print()


for i in range(len(li)):
    #print(li[i])
    print('Element: %i at position: %s' % (li[i], i))

#############################

li2 = [1232, 'abcd', 1.1243, 'hello world',  2323, 23435.212121, 2356, 876, 98989]

print()
print()

for i in range(len(li2)):
    print('Element: %s at position: %s' % (li2[i], i))

li2.append('appended string') # at the end
print(li2)

print()

li2.insert(3, 'appended string') # in the 3rd position
print(li2)

print()
print(li2)
print(li2[3:])
print(li2[:-2])
print(li2[-2:])

# sort(li2) # error












