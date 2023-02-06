t = int(input())
eratos = [0]*2 + 9998*[1]
for i in range(2, 10000):
    for j in range(2*i, 10000, i):
        eratos[j] = 0

for i in range(t) :
    n = int(input())
    a, b = n//2, n//2
    while a > 0:
        if eratos[a] == 1 and eratos[b] == 1 :
            print(a, b)
            break
        else :
            a -= 1
            b += 1
