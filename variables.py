a = 50567829487567438948567438934894873894875647894385674839487543894875489238475839
b = 100
c = a + b

print('a=' + str(a))
print(type(a))

print('c=' + str(c)) # really large storage of numbers full precision

f = 12232.2323232
print(f)
print(type(f))

print(1.79e+308) ## limit for float numbers
print(1.8e+308) ## exceeds the limit -> infinity

bb = 0b110101
print(bb)

hx = 0xa
print(hx)

d = 1234
e = 54323
print(d/e)

f = 5

print(f**2)

g = 10
# rest of divison
print(g % 3)

h = "6279397482"
print(type(h)) # string

h = "6279397482"
h = int(h)
print(type(h)) # integer


h = "6279397482"
##h = "6279397482asnh"
print(h.isalpha())
print(h.isdigit())


f = 748392.12343
print(type(f))
fi = int(f) ## doesn't round but cut off the decimals
print(fi)
fr = round(f)
print(fr) ## rounds the number







