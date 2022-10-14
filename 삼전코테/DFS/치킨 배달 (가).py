# 입력값 받기
n, m = map(int, input().split())
map = [list(map(int, input().split())) for _ in range (n)]

house_list = []
chicken_list = []
choose_chicken = []
answer = 100000

for i in range (n) :
    for j in range (n) :
        if map[i][j] == 2 :
            chicken_list.append((i, j))
        elif map[i][j] == 1 :
            house_list.append((i, j))

def dfs (depth, idx) :
    global answer

    if depth == m :
        sum = 0
        for house in house_list :
            val = 100000
            for choose in choose_chicken :
                temp = abs(house[0] - choose[0]) + abs(house[1] - choose[1])
                val = min(val, temp)
            sum += val
        answer = min(answer, sum)
        return

    for i in range(idx, len(chicken_list)) :
        if chicken_list[i] in choose_chicken :
            continue

        choose_chicken.append(chicken_list[i])
        dfs(depth+1, idx+1)
        choose_chicken.pop()

dfs(0, 0)
print(answer)