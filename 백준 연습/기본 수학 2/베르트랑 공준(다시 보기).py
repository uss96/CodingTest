eratos = [0]*2 + [1]*246912

for i in range(2, 246913) :
    if eratos[i] :
        for j in range(i*2, 246913, i):
            eratos[j] = 0

while True :
    x = int(input())
    if x == 0:
        break
    print(sum(eratos[x+1:x*2+1]))

