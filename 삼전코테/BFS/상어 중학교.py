from collections import deque

# 입력값 받기
n, m = map(int, input().split())
board= [list(map(int, input().split())) for _ in range(n)]



# 인접 블록 찾기 -> 블록 크기, 무지개 크기, 블록 좌표 리턴
def bfs (x, y, color) :
    q = deque()
    q.append([x, y])
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    block_cnt, rainbow_cnt = 1, 0 # 블록 개수, 무지개 블록 개수
    blocks, rainbows = [[x, y]], [] # 블록 좌표 넣을 리스트, 무지개좌표 넣을 리스트

    while q :
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == color and not visited[nx][ny]: # 범위 안이고 방문 안 한 일반 블록인 경우
                visited[nx][ny] = 1
                q.append([nx, ny])
                block_cnt += 1
                blocks.append([nx, ny])

            elif 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0 and not visited[nx][ny] : # 범위 안이고 방문 안 한 무지개 블록인 경우
                visited[nx][ny] = 1
                q.append([nx, ny])
                block_cnt += 1
                rainbow_cnt += 1
                rainbows.append([nx, ny])

    # 무지개 블록은 방문 다시 해제
    for x, y in rainbows :
            visited[x][y] = 0

    return [block_cnt, rainbow_cnt, blocks + rainbows]


# 블록 제거 함수
def remove(block) :
    for x, y in block:
        board[x][y] = -2

# 중력 함수
def gravity(a) :
    for i in range(n - 2, -1, -1) : # 밑에서 부터 체크
        for j in range(n) :
            if a[i][j] > -1 : # -1이 아니면 아래로 다운
                r = i
                while True :
                    if 0 <= r + 1 < n and a[r + 1][j] == -2 : # 다음 행이 인덱스 범위 안이면서 -2이면 아래로 다운
                        a[r + 1][j] = a[r][j]
                        a[r][j] = -2
                        r += 1
                    else :
                        break

# 반시계 회전 함수
def rot90 (a) :
    a = list(zip(*a))[::-1]
    a = [list(s) for s in a]
    return a

score = 0

# 오토 플레이
while True :
    # 크기 가장 큰 블록 찾기
    visited = [[0] * n for _ in range(n)] # 방문 체크
    blocks = [] # 가능한 블록 그룹들 넣을 리스트

    for i in range(n) :
        for j in range(n) :
            if not visited[i][j] and board[i][j] > 0 : # 일반 블록이면서 방문 안 한 경우
                visited[i][j] = 1 # 방문
                block_info = bfs(i, j, board[i][j]) # 인접한 블록 찾기
                if block_info[0] >= 2 :
                    blocks.append(block_info)
    blocks.sort(reverse=True)

    # 블록 제거 + 점수 더하기
    if not blocks:
        break
    print(blocks)
    remove(blocks[0][2])
    score += blocks[0][0] ** 2

    # 중력
    gravity(board)

    # 90도 회전
    board = rot90(board)

    # 중력
    gravity(board)


print(score)
print(board)
