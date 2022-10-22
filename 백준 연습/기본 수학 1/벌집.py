#1 7 19 37 61 ...

n = int(input())
i = 0
end = 1
while True :
    if n == 1 :
        break
    i += 1
    end += 6 * i
    if end >= n :
        break
print(i + 1)