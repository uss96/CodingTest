tc = int(input())

for i in range(tc) :
    result = []
    arr = list(map(str, input().split()))
    n = int(arr[0])
    arr_list = list(arr[1])

    for j in range(len(arr_list)) :
        result += arr_list[j] * n

    c = ''.join(result)
    print(c)