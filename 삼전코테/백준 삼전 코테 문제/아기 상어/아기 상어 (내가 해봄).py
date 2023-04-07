from collections import deque
# 입력값 받자!

N = int(input())
fish_map = [list(map(int, input().split())) for _ in range(N)]

# 아기상어 어딨냐!

for i in range(N):
    for j in range(N) :
        if fish_map[i][j] == 9:
            s_x, s_y = i, j

# 탐사 방향
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 초기값들 셋팅

ans = 0
size = 2
eat_count = 0

# bfs 입력값 : 상어 위치, 출력값 : 먹이감 리스트

def bfs (x, y) :
    visited = [[0] * N for _ in range(N)]
    queue = deque([[x, y]])

    eat_list = []
    visited[x][y] = 1

    while queue :
        i, j = queue.popleft()

        for d in range(4) :
            ni = i + dx[d]
            nj = j + dy[d]

            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0 :
                if fish_map[x][y] > fish_map[ni][nj] and fish_map[ni][nj] != 0:
                    visited[ni][nj] = visited[i][j] + 1
                    eat_list.append((visited[ni][nj]-1, ni, nj))
                elif fish_map[x][y] == fish_map[ni][nj] :
                    visited[ni][nj] = visited[i][j] + 1
                    queue.append([ni, nj])
                elif fish_map[ni][nj] == 0 :
                    visited[ni][nj] = visited[i][j] + 1
                    queue.append([ni, nj])

    return sorted(eat_list, key = lambda x : (x[0], x[1], x[2]))

# 실제 문제 시행

while True :
    fish_map[s_x][s_y] = size
    eat_list = deque(bfs(s_x, s_y))

    if not eat_list :
        break

    time, nx, ny = eat_list.popleft()
    ans += time
    eat_count += 1

    if size == eat_count :
        size += 1
        eat_count = 0

    fish_map[s_x][s_y] = 0
    s_x, s_y = nx, ny

print(ans)