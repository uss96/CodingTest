arr = [list(map(int, input().split())) for _ in range(9)]

max_val = max(map(max, arr))
print(max_val)
add = []
for i in range(9):
    for j in range(9):
        if arr[i][j] == max_val :
            add.append(i)
            add.append(j)

print(add[0]+1, end=' ')
print(add[1]+1)