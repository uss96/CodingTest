s = str(input())

list(s)
count = 0

if s[0] == ' ' :
    count -= 1
if s[-1] == ' ' :
    count -= 1

for i in range(len(s)) :
    if s[i] == ' ' :
        count += 1

print(count + 1)