m = int(input())
n = int(input())
num_list = []

for i in range(m, n + 1):
    count = 0
    for j in range(2, i) :
        if i % j == 0 :
            count += 1
    if i != 1 and count == 0:
        num_list.append(i)

if sum(num_list) == 0 :
    print("-1")
else :
    print(sum(num_list))
    print(num_list[0])