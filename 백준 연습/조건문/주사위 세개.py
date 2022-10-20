a, b, c = map(int, input().split())


if a == b and b == c :
    d = 10000 + a * 1000
    print(d)

elif a == b and a != c :
    e = 1000 + a * 100
    print(e)

elif b == c and a != c :
    f = 1000 + b * 100
    print(f)

elif a == c and a != b :
    g = 1000 + a * 100
    print(g)

else :
    h = max(a, b, c) * 100
    print(h)