s = (str(input()))
s1 = s.lower()

alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
count = [0] * 26

for i in range(len(s1)) :
    for j in range(26) :
        if s1[i] == alpha[j] :
            count[j] += 1

num = 0
pos = []

for i in range(len(alpha)) :
    if count[i] == max(count) :
        num += 1
        pos.append(i)

if num == 1 :
    print(alpha[pos[0]].upper())

else :
    print("?")
