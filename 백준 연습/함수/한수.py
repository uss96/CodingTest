n = int(input())
han_list = []
for i in range(1, (n + 1)) :
    a = list(str(i))
    count = 0

    for j in range(1, len(a) - 1) :
        if (int(a[j - 1]) - int(a[j])) != (int(a[j]) - int(a[j + 1])) :
            count += 1

    if count == 0 :
        han_list.append(i)

print(len(han_list))