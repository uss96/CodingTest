tc = int(input())

count = 0
for i in range(tc) :
    voca = str(input())
    gro = list(voca)
    same = 0
    num = []
    group = []

    for j in range(1, len(gro)) :

        if j == 1 :
            num.append(gro[j - 1])
        num.append(gro[j])

        if gro[j] == gro[j - 1] :
            num.pop(-1)
    temp = set(num)
    group = list(temp)

    if len(num) == len(group) :
        count += 1
print(count)