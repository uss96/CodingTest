# 치킨 배달
# 치킨 거리는 집과 가장 가까운 치킨집 사이의 거리
# 도시의 치킨 거리는 모든 집의 치킨 거리의 합

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

house_list = []
chicken_list = []
choosen_chicken_list = []
answer = 1000000  # 임의의 숫자
# 치킨집, 집 위치 값 넣기
for i in range(N):
    for j in range(N):
        if graph[i][j] == 2:
            chicken_list.append((i, j))
        if graph[i][j] == 1:
            house_list.append((i, j))


# dfs 구현
def dfs(depth, idx):
    global answer

    if depth == M:
        sum = 0
        for house in house_list:  # 하우스 당 체크 시작
            val = 1000000  # 임의의 숫자
            for choosen_chicken in choosen_chicken_list:  # 치킨집 순차 탐색
                tmp = abs(house[0] - choosen_chicken[0]) + abs(house[1] - choosen_chicken[1])  # 치킨 거리
                val = min(tmp, val)  # 각 house 당 치킨 거리의 최소 값  = val
            sum += val  # 도시의 치킨 거리 = val의 합 = 각 house 당 치킨 거리의 최소 값의 합
        answer = min(answer, sum)
        return

    for i in range(idx, len(chicken_list)):  # combination 구현
        if chicken_list[i] in choosen_chicken_list:
            continue

        choosen_chicken_list.append(chicken_list[i])
        dfs(depth + 1, i + 1)
        choosen_chicken_list.pop()


dfs(0, 0)
print(answer)
