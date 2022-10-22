generator = []
all_list = []

for i in range(1, 10001) :
    ans = i
    n = list(str(i))
    all_list.append(i)
    for j in range(len(n)) :
        ans += int(n[j])
    generator.append(ans)

set_gen = set(generator)
set_all = set(all_list)
temp = set.difference(set_all, set_gen)
result = list(temp)
result.sort()
for i in range(len(result)) :
    if result[i] <= 10000 :
        print(result[i])
