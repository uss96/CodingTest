
s = str(input())
l = len(s)
answer = l

for i in range(1, l//2 + 1) :
    compress = ""
    prev = s[0 : i]
    count = 1

    for j in range(i, l, i) :
        if prev == s[j : j + i] :
            count += 1
        else :
            if count >= 2 :
                compress += str(count) + prev
            else :
                compress += prev

            prev = s[j : j + i]
            count = 1

    if count >= 2:
        compress += str(count) + prev
    else :
        compress += prev

    answer = min(answer, len(compress))
print(answer)