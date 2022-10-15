
# 입력값 받기
n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range (n)]

chicken_list = []
house_list = []
choose_chicken = []
answer = 100000

for i in range(n) :
    for j in range(n) :
        if city[i][j] == 2 :
            chicken_list.append((i, j))
        elif city[i][j] == 1 :
            house_list.append((i, j))

def dfs(depth, idx) :
    global answer

    if depth == m :
        sum = 0
        for i in range(house_list) :
            dist = 100000
            for j in range(choose_chicken) :
                temp = abs(i[0] - j[0]) + abs(i[1] - j[1])
                dist = min(dist, temp)
            sum += dist
        answer = min(answer, sum)

    for i in range(idx, len(chicken_list)) :
        if chicken_list[i] in choose_chicken :
            continue

        choose_chicken.append(chicken_list[i])
        dfs(depth + 1, idx + 1)
        choose_chicken.pop()


dfs(0, 0)
print(answer)