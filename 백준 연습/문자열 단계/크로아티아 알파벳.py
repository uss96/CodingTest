a = str(input())
s = list(a)
count = 0
for i in range(len(s)) :
    if s[i] == "=" :
        if s[i - 1] == "z" and s[i - 2] == "d" :
            count -= 1
        else :
            count += 0

    elif s[i] == "-" :
        count += 0
    elif s[i] == "j" :
        if s[i - 1] == "n" or s[i - 1] == "l" :
            count += 0
        else :
            count += 1
    else :
        count += 1


print(count)