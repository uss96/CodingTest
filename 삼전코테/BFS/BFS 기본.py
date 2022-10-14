# BFS 기본 코드 연습

from collections import deque

# 상, 하, 좌, 우 구현
dy = {-1, 1, 0, 0}
dx = {0, 0, -1, 1}

def out_of_range(y, x) : # 격자에서 벗어났는지 판별하는 함수
    return y < 0 or y >= N or x < 0 or x >= N

def bfs(y, x) :
    q = deque() # queue
    # 시작 좌표 (y, x) 삽입 및 visited 표시
    q.append((y, x))
    visited = [[False] * N for _ in range(N)] # N*N 격자의 경우
    visited[y][x] = True

    while q : #queue에 값이 존재하는 동안 반복
        sy, sx = q.popleft()
        for d in range(4) : # pop한 좌표의 4방향 탐색
            ny = sy + dy[d]
            nx = sx + dx[d]

            if out_of_range(ny, nx) or visited[ny][nx] : # 격자에서 벗어났거나, 방문한 좌표의 경우 continue
                continue

            else : # 아닌 경우 (상황에 따라 예외가 있는 경우 처리해야 함)
                do_something() # 이후 동작 호출 (혹은 코드를 바로 작성)
                q.append((ny, nx)) # queue에 탐색한 좌표 추가 및 방문 기록
                visited[ny][nx] = True