a = int(input())
b = str(input())

c = a * int(b[2])
d = a * int(b[1])
e = a * int(b[0])
f = e*100 + 10*d + c

print(c)
print(d)
print(e)
print(f)