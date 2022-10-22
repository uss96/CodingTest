s = list(str(input()))
alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
result = [str(-1)] * 26

for i in range(len(s) - 1, -1, -1) :
    for j in range(len(alpha)) :
        if s[i] == alpha[j] :
            result[j] = str(i)

c = ' '.join(result)
print(c)

