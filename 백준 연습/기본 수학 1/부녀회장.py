t = int(input())

for a in range(t):
    k = int(input())
    n = int(input())
    arr = [[0] * n for x in range(k+1)]
    for b in range(n):
        arr[0][b] = b + 1
    for c in range(k+1):
        arr[c][0] = 1

    for d in range(1, k+1):
        for e in range(1, n):
            arr[d][e] = arr[d - 1][e] + arr[d][e - 1]

    print(arr[k][n-1])
