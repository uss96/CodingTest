tc = int(input())

for _ in range(tc):
    h, w, n = map(int, input().split())
    if n % h != 0 and (n // h) < 9 :
        print(str(n % h) + "0" + str(n // h + 1))

    elif n % h != 0 and (n // h) >= 9 :
        print(str(n % h) + str(n // h + 1))

    elif n % h == 0 and (n // h) <= 9 :
        print(str(h) + "0" + str(n // h))

    elif n % h == 0 and (n // h) > 9 :
        print(str(h) + str(n // h))

