
# 입력값 받기
s = str(input())

abc = []
num = []

for i in range(len(s)) :
    if s[i].isalpha() :
        abc.append(s[i])
    else :
        num.append(int(s[i]))

abc.sort()


b = str(sum(num))
abc.append(b)
print(''.join(abc))