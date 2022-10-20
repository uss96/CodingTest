from collections import deque
n, m = map(int, input().split())
map_info = [list(map(int, input().split())) for _ in range(n)]

chicken_list = []
choose_list = []
house_list = []
result = 100000

for i in range(n) :
    for j in range(n) :
        if map_info[i][j] == 2 :
            chicken_list.append((i, j))
        if map_info[i][j] == 1 :
            house_list.append((i, j))

def dfs(depth, idx) :
    global result
    if depth == m :
        sum = 0
        for house in house_list :
            val = 100000
            for chicken in chicken_list :
                temp = abs(house[0] - chicken[0]) + abs(house[1] - chicken[1])
                val = min(temp, val)
            sum += val
        result = min(sum, result)

    for i in range(idx, len(chicken_list)) :
        if chicken_list[i] in choose_list :
            continue

        choose_list.append(chicken_list[i])
        dfs(depth + 1, idx + 1)
        choose_list.pop()

dfs(0, 0)
print(result)