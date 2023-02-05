n = int(input())
num = 0
for i in range(n//5+1):
    dum = n - i*5
    if dum%3 == 0:
        num = i + dum/3

if num == 0:
    print("-1")
else:
    print(int(num))