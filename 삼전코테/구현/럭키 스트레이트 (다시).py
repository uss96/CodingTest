n = str(input())
l = len(n)

front = 0
rear = 0

for i in range(l//2) :
    front += int(n[i])
for i in range(l//2, l) :
    rear += int(n[i])

if front == rear :
    print('LUCKY')
else :
    print('READY')