n = int(input())
if n != 1:
    k = n
    arr = []
    while 1:
        if k == 1 :
            break
        for i in range(2, n + 1):
            if k % i == 0:
                arr.append(i)
                k = k / i
                break

    for i in range(len(arr)):
        print(arr[i])
