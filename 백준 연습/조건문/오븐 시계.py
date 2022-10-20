a, b = map(int, input().split())
c = int(input())

d = c // 60
e = c % 60

if e + b >= 60 : # 분이 60분 넘어갈 경우
    a += 1

    if a + d >= 24 : # 시간이 24시를 넘어갈 경우
        h = a + d - 24
        m = e + b - 60

    else :
        h = a + d
        m = e + b - 60

else :

    if a + d >= 24 :
        h = a + d - 24
        m = e + b

    else :
        h = a + d
        m = e + b

print(h, end=" ")
print(m)
