x = int(input())

i = 1
n = 1
while True :
    if x <= n :
        break

    i += 1
    n += i
# 8번째 -> 3/2 i = 2, n = 3 / i = 3, n = 6 / i = 4, n = 10 /

spare = n - x

if i % 2 == 0 :

    print(str(i - spare) + "/" + str(1 + spare))

else :

    print(str(1 + spare) + "/" + str(i - spare))
