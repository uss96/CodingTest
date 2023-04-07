from collections import deque
# 초기값 받기
N = int(input())
fish_map = [list(map(int, input().split())) for _ in range(N)]

# 아기 상어의 초기 위치는?

for i in range(N) :
    for j in range(N) :
        if fish_map[i][j] == 9 :
            s_x, s_y = i, j

size = [2, 0]
ans = 0

# 탐사 방향 // 순서는 중요하지 않음!
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# bfs 제작하기 // 입력값 : 아기상어의 위치, 출력값 : 먹이감 리스트

def bfs (x, y) :
    visited = [[0] * N for _ in range(N)] # N * N 크기의 [0]으로 채워진 2차원 리스트! 먹이감 이동 시간과 위치를 알기 위함
    queue = deque([[x, y]]) # queue 초기 위치를 넣어줌 (아기 상어 위치)
    eat_list = [] # 먹이감 리스트 선언

    visited[x][y] = 1 # 아기 상어 초기 위치

    while queue: # queue 안에 아무것도 없을 때까지 계속 반복
        i, j = queue.popleft() # queue 안에 있는 i, j를 뽑음!

        # i, j에서 상, 하, 좌, 우 탐색
        for d in range(4) :
            ni = i + dx[d]
            nj = j + dy[d]

            # 만약 ni, nj가 인덱스 내부 범위이고, 아직 간 적 없다면
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0 :
                # (ni, nj)의 물고기가 아기 상어보다 작은 경우 & 빈칸이 아닌 경우 --> 먹자!
                if fish_map[x][y] > fish_map[ni][nj] and fish_map[ni][nj] != 0 :
                    visited[ni][nj] = visited[i][j] + 1 # 소요 시간을 알기 위해 visitied 맵에 표시
                    eat_list.append((visited[ni][nj]-1, ni, nj)) # 아기 상어 초기 위치를 1로 뒀기 때문에 1 뺌 + 이동 위치
                elif fish_map[x][y] == fish_map[ni][nj] : # 아기상어와 위치 물고기 크기가 같을 때
                    visited[ni][nj] = visited[i][j] + 1
                    queue.append([ni, nj]) # 다음 이동 후보 리스트에만 넣어둠
                elif fish_map[ni][nj] == 0 : # 탐사 위치에 물고기가 없는 경우
                    visited[ni][nj] = visited[i][j] + 1
                    queue.append([ni, nj]) # 다음 이동 후보 리스트에만 넣어둠

    return sorted(eat_list, key = lambda x : (x[0], x[1], x[2])) # 거리, x, y에 대해 정렬

while True :
    fish_map[s_x][s_y] = size[0] # 아기상어 위치에 상어 크기 넣어줌
    eat_list = deque(bfs(s_x, s_y)) # eat_list를 bfs를 통해 구해줌

    if not eat_list :
        break # 먹이감 리스트가 더 이상 없는 경우 while문 벗어나기

    time, nx, ny = eat_list.popleft() # 가장 왼쪽 꺼 빼오기

    # 소요 시간 증가 및 먹은 횟수 1회 +
    ans += time
    size[1] += 1

    # 상어 사이즈 증가
    if size[0] == size[1] :
        size[0] += 1
        size[1] = 0

    # 상어 위치 바꾸기
    fish_map[s_x][s_y] = 0
    s_x, s_y = nx, ny

print(ans)
