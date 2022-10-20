from collections import deque
import time
start = time.time()

# 입력값 받기
n, m = map(int, input().split())
map_info = [list(map(int, input().split())) for _ in range(n)]

virus = []
blank = []
answer = 0
map_temp = [[0] * m for _ in range(n)]

for i in range(n) :
    for j in range(m) :
        if map_info[i][j] == 2 :
            virus.append((i, j))
        elif map_info[i][j] == 0:
            blank.append((i, j))


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def virus_spread (x, y) :

    for i in range(4) :

        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and map_temp[nx][ny] == 0 :
            map_temp[nx][ny] = 2
            virus_spread(nx, ny)

def dfs (depth) :
    global answer

    if depth == 3 :
        q = deque(virus)
        count = 0
        for i in range(n):
            for j in range(m):
                map_temp[i][j] = map_info[i][j]

        while q:
            x, y = q.popleft()

            virus_spread(x, y)

        for i in range(n) :
            for j in range(m) :
                if map_temp[i][j] == 0:
                    count += 1

        answer = max(count, answer)
        return

    # 벽을 골라야 해
    for (x, y) in blank :
        if map_info[x][y] == 0:
            map_info[x][y] = 1
            depth += 1
            dfs(depth)
            map_info[x][y] = 0
            depth -= 1
    # for i in range(n):
    #     for j in range(m):
    #         if map_info[i][j] == 0:
    #             map_info[i][j] = 1
    #             depth += 1
    #             dfs(depth)  # count가 3이 될 때까지 dfs 재귀반복
    #             map_info[i][j] = 0  # 빠져나오면 (i, j) 0으로 바꾸기
    #             depth -= 1  # 0으로 바꿨으니까 count 1 줄이고 다시 진행

dfs(0)
print(answer)
print(time.time() - start)