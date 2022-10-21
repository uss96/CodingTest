c = int(input())

for i in range(c) :
    arr = list(map(int, input().split()))

    n = arr.pop(0)
    avg = (sum(arr)) / n
    count = 0

    for j in range (n):
        if arr[j] > avg:
            count += 1

    ratio = count / n * 100

    print("{:.3f}".format(ratio) + "%")