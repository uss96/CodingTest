from collections import deque

# 입력값 받기
n, m = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]

# 방향값 설정
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# bfs
def bfs(x, y, color) :
    q = deque()
    q.append([x, y])

    block_cnt, rainbow_cnt = 1, 0 # 블록 개수 초기화
    blocks, rainbows = [[x, y]], [] # 블록 좌표

    while q :
        x, y = q.popleft()

        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and map[nx][ny] == color and not visited[nx][ny] :
                visited[nx][ny] = 1
                q.append([nx, ny])
                block_cnt += 1
                blocks.append([nx, ny])

            elif 0 <= nx < n and 0 <= ny < n and map[nx][ny] == 0 and not visited[nx][ny] :
                visited[nx][ny] = 1
                q.append([nx, ny])
                block_cnt += 1
                rainbow_cnt += 1
                rainbows.append([nx, ny])

    for x, y in rainbows :
        visited[x][y] = 0

    return [block_cnt, rainbow_cnt, blocks + rainbows]

# 중력
def gravity (map) :
    for i in range (n - 2, -1, -1) :
        for j in range(n) :
            if map[i][j] > -1 :
                r = i
                while True :
                    if 0 <= r + 1 < n and map[r + 1][j] == -2 :
                        map[r + 1][j] = map[r][j]
                        map[r][j] = -2
                        r += 1
                    else :
                        break

# 반시계 회전
def rot90 (map) :
    map = list(zip(*map))[::-1]
    map = [list(s) for s in map]

    # map = list(zip(*map))[::-1]
    # map = [list(s) for s in map]
    return map

# 지우기
def remove(block) :
    for x, y in block :
        map[x][y] = -2

# 자동 돌리기

score = 0

while True :
    visited = [[0] * n for _ in range(n)]
    blocks = []

    for i in range(n) :
        for j in range(n) :
            if map[i][j] > 0 and not visited[i][j]:
                visited[i][j] = 1
                block_info = bfs(i, j, map[i][j])

                if block_info[0] >= 2:
                    blocks.append(block_info)

    blocks.sort(reverse=True)

    if not blocks :
        break
    print(blocks)
    remove(blocks[0][2])
    score += blocks[0][0] ** 2

    gravity(map)
    map = rot90(map)
    gravity(map)

print(score)
print(map)