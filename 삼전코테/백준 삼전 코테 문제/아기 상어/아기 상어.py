# N*N 크기에 물고기 M마리와 아기 상어 1마리 (9)
# 아기 상어의 초기 크기는 2, 1초에 상하좌우로 인접한 한 칸씩 이동
# 자기보다 큰 물고기는 못 지나감, 같으면 지나갈 수만 있음, 작으면 먹을 수 있음
# 먹을 수 있는 물고기가 1마리면 그 물고기 먹으러 감
# 먹을 수 있는 물고기가 여러 마리면, 거리가 가장 가까운 물고기 (같은 거리일 시 가장 위, 가장 왼쪽)
# 자기와 크기와 같은 수의 물고기를 먹을 때마다 크기가 1 증가. 크기가 2일 시 2마리 먹으면 3
from collections import deque

# 입력값 받기
N = int(input())
fish_map = [list(map(int, input().split())) for _ in range(N)]

# 방향
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 초기 위치 찾기
time = 0
pos = []
for x in range(N) :
    for y in range(N) :
        # 아기 상어의 첫 번째 위치 찾기
        if fish_map[x][y] == 9 :
            pos.append(x)
            pos.append(y)

# bfs 함수 제작 (x, y) -> 아기상어 위치
def bfs(x, y) :
    visited = [[0]*N for _ in range(N)]
    queue = deque([[x, y]])
    eat_list = []

    visited[x][y] = 1

    while queue :
        i, j = queue.popleft()

        for idx in range(4) :
            ni = i + dx[idx]
            nj = j + dy[idx]

            # 인덱스 안에 있으며, 동시에 아직 가보지 않은 곳
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0 :
                # 아기상어의 사이즈가 더 크며, 물고기가 있는 곳
                if fish_map[x][y] > fish_map[ni][nj] and fish_map[ni][nj] != 0 :
                    visited[ni][nj] = visited[i][j] + 1 # 방문 처리 & time 증가
                    eat_list.append((visited[ni][nj] - 1, ni, nj)) # 먹이감 후보에 추가?
                # 아기상어의 사이즈와 같은 물고기가 있는 곳
                elif fish_map[x][y] == fish_map[ni][nj] :
                    visited[ni][nj] = visited[i][j] + 1 # 방문 처리 & time 증가
                    queue.append([ni, nj]) # 이동
                # 물고기가 없는 경우
                elif fish_map[ni][nj] == 0 :
                    visited[ni][nj] = visited[i][j] + 1 # 방문 처리 & time 증가
                    queue.append([ni, nj]) # 이동

    # 먹이감 후보 리스트 우선 순위로 정렬
    return sorted(eat_list, key = lambda x : (x[0], x[1], x[2]))

i, j = pos
size = [2, 0]

# 맨 앞의 후보만 먹고 위치 이동 후 다시 bfs 시작
while True :
    fish_map[i][j] = size[0] # 아기 상어 위치에 size 넣기
    eat_list = deque(bfs(i, j))

    if not eat_list : # 먹이감 후보가 없는 경우 끝내기
        break
    # 먹이감 리스트의 첫 번째 먹이를 뽑아 그 위치로 이동 & time 증가
    step, nx, ny = eat_list.popleft()
    time += step
    size[1] += 1

    # 사이즈와 먹은 물고기 수가 같을 때 사이즈 증가
    if size[0] == size[1] :
        size[0] += 1
        size[1] = 0

    fish_map[i][j] = 0 # 상어 이전 위치 0으로 만들기
    i, j = nx, ny

print(time)






