s = str(input())

mun = []
num = 0
l = len(s)
for i in range(l) :
    if s[i].isalpha() :
       mun.append(s[i])
    else :
        num += int(s[i])

mun.sort()
fin = str(num)
mun.append(fin)

print(''.join(mun))