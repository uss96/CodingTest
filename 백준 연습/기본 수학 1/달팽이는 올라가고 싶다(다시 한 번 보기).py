a, b, v = map(int, input().split())

dal = (v - b)/(a - b)

if dal == int(dal) :
    print(int(dal))
else :
    n = int(dal) + 1
    print(int(n))



# a * n - b * (n - 1) >= v
# n(a - b) + b >= v
# n >= (v - b) / (a - b)
