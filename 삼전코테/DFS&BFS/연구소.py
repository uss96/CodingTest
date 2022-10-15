# 입력값 받기
from collections import deque
import time

start = time.time()

n, m = map(int, input().split())

map = [list(map(int, input().split())) for _ in range(n)]
wall_map = [[0] * m for _ in range(n)]

# 이동 방향
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

virus_pos = []


for i in range(n) :
    for j in range(m) :
        if map[i][j] == 2 :
            virus_pos.append((i, j))

result = 0

# 바이러스가 사방으로 퍼지게 하는 함수
def virus(x, y) :

    for i in range (4) :
        nx = x + dx[i]
        ny = y + dy[i]

        # 상, 하, 좌, 우 중 바이러스가 퍼질 수 있는 경우
        if 0 <= nx < n and 0 <= ny < m and wall_map[nx][ny] == 0:
            # 해당 위치에 바이러스 배치하고 다시 재귀적으로 수행
            wall_map[nx][ny] = 2
            virus(nx, ny)

# 맵에서 안전 영역 크기를 계산하는 함수
def cal() :
    area = 0
    for i in range(n) :
        for j in range(m) :
            if wall_map[i][j] == 0 :
                area += 1
    return area

#  dfs를 통해 벽을 설치하면서 매번 안전 영역의 크기를 계산
def dfs(count) :
    global result
    # 울타리가 3개 설치된 경우
    if count == 3 :
        for i in range(n) :
            for j in range(m) :
                wall_map[i][j] = map[i][j]
        q = deque(virus_pos)
        # 각 바이러스의 위치에서 전파 진행
        while q:
            x, y = q.popleft()
            virus(x, y)

        # 안전 영역 최댓값 계산하기
        result = max(result, cal())
        return

    # 빈 공간에 울타리 설치
    for i in range(n) :
        for j in range(m) :
            if map[i][j] == 0 :
                map[i][j] = 1
                count += 1
                dfs(count) # count가 3이 될 때까지 dfs 재귀반복
                map[i][j] = 0 # 빠져나오면 (i, j) 0으로 바꾸기
                count -= 1 # 0으로 바꿨으니까 count 1 줄이고 다시 진행

dfs(0)
print(result)
print(time.time() - start)