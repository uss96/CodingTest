while True:
    n = int(input())
    count = 0
    arr = set([])
    if n == 0 :
        break
    elif n == 1:
        arr.add("2")
    else :
        for i in range(n + 1, 2*n + 1) :
            for j in range(2, (int(i**0.5)+1)) :
                if i % j == 0 :
                    break
            else :
                arr.add(i)
    print(len(arr))