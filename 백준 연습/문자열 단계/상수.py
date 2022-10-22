s = list(map(str, input().split()))
a = list(s[0])
b = list(s[1])

#reverse
a.reverse()
b.reverse()

c = int(a[0]) * 100 + int(a[1]) * 10 + int(a[2])
d = int(b[0]) * 100 + int(b[1]) * 10 + int(b[2])

if c > d :
    print(c)
else :
    print(d)