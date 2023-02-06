arr = [[0]*100 for _ in range(100)]

t = int(input())
count = 0
for i in range(t):
    a, b = map(int, input().split())
    for j in range(a, a+10):
        for z in range(b, b+10):
            arr[j][z] = 1

for i in range(100):
    for j in range(100):
        count += arr[i][j]
print(count)