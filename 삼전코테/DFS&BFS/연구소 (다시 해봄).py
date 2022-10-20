from collections import deque
import time
start = time.time()
# 입력값 받기

n, m = map(int, input().split())
map_info = [list(map(int, input().split())) for _ in range(n)]

virus = []
blank = []
wall = []
wall_map = [[0] * m for _ in range (n)]
answer = 0

# 바이러스, 빈칸 넣기
for i in range(n) :
    for j in range(m) :
        if map_info[i][j] == 2 :
            virus.append((i, j))
        elif map_info[i][j] == 0 :
            blank.append((i, j))

# 방향성
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 바이러스 퍼지는 코드 작성
def virus_spread(x, y) :

    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]

        # 범위 안이고 빈 칸인 경우
        if 0 <= nx < n and 0 <= ny < m and wall_map[nx][ny] == 0 :
            wall_map[nx][ny] = 2
            virus_spread(nx, ny)

# dfs 코드 작성
def dfs(depth) :
    global answer

    if depth == 3 :
        q = deque(virus)
        count = 0
        for i in range(n) :
            for j in range(m) :
                wall_map[i][j] = map_info[i][j]
        while q:
            x, y = q.popleft()
            virus_spread(x, y)

        for i in range(n) :
            for j in range(m) :
                if wall_map[i][j] == 0:
                    count += 1

        answer = max(answer, count)
        return

    for i in range(n) :
        for j in range(m) :
            if map_info[i][j] == 0 :
                map_info[i][j] = 1
                depth += 1
                dfs(depth) # count가 3이 될 때까지 dfs 재귀반복
                map_info[i][j] = 0 # 빠져나오면 (i, j) 0으로 바꾸기
                depth -= 1 # 0으로 바꿨으니까 count 1 줄이고 다시 진행
dfs(0)
print((answer))
print(time.time() - start)