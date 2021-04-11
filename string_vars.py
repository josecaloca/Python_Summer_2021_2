s = 'abcdefaa'

print(len(s))
print(s[1:])
print(s[1:3])
print(s[:2])
print(s[-2:])
print(s[-3:])

s2 = 'abc\ndef' # \n includes another line
print(s2)

print(ord('a')) ## check ascii table

s4 = 'abc\tdef\t\t\thello'
print(s4)

s5 = 'abc\td\ef\t\t\te\gwg'
print(s5)

s6 = "student's"
print(s6)

s6 = 'student\'s'
print(s6)

s7 = '              asasasas asasasasas'
print(s7.strip()) # eliminates leading spaces

s5_tab = s5.split('\t')
print(s5_tab )

