h, m = map(int,input().split())


if m < 45 :
    if h == 0 :
        h1 = 23
        m1 = m + 15
    else :
        h1 = (h - 1)
        m1 = (m + 15)
    print(h1, end=" ")
    print(m1)

else :
    h2 = (h)
    m2 = (m - 45)
    print(h2, end=" ")
    print(m2)