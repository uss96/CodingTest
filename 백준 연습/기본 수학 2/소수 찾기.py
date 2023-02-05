n = int(input())
num_list = list(map(int, input().split()))
num = 0
for i in range(n):
    k = num_list[i]
    count = 0
    for j in range(2, k) :
        if k % j == 0 :
            count += 1
    if k != 1 and count == 0 :
        num += 1


print(num)