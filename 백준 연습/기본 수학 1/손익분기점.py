a, b, c = map(int, input().split())

num = 0
idd = 0

if b >= c :
    print("-1")

else :

    idd = c - b

    print(a // idd + 1)

