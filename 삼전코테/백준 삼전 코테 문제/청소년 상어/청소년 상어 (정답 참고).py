import copy

# 초기값 설정
board = [[] for _ in range(4)]
ans = 0

# 방향 설정
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

# 입력값 받기
for i in range(4) :
    data = list(map(int, input().split()))
    fish = []
    for j in range(4) :
        fish.append([data[2*j], data[2*j+1]-1])

    board[i] = fish

# dfs 함수 만들기

def dfs (s_x, s_y, score, board) :
    global ans
    score += board[s_x][s_y][0]
    ans = max(score, ans)
    board[s_x][s_y][0] = 0

    # 물고기 이동
    for a in range(1, 17) :
        f_x, f_y = -1, -1
        for x in range(4) :
            for y in range(4) :
                if board[x][y][0] == a :
                    f_x, f_y = x, y
                    break

        if f_x == -1 and f_y == -1 :
            continue
        f_d = board[f_x][f_y][1]

        for b in range(8) :
            nd = (f_d + b) % 8
            nx = f_x + dx[nd]
            ny = f_y + dy[nd]

            if not (0 <= nx < 4 and 0 <= ny < 4) or (nx == s_x and ny == s_y) :
                continue
            board[f_x][f_y][1] = nd
            board[f_x][f_y], board[nx][ny] = board[nx][ny], board[f_x][f_y]
            break

    # 청소년 상어의 식사
    s_d = board[s_x][s_y][1]
    for i in range(1, 5) :
        nx = s_x + dx[s_d] * i
        ny = s_y + dy[s_d] * i

        if (0 <= nx < 4 and 0 <= ny < 4) and (board[nx][ny][0] > 0) :
            dfs(nx, ny, score, copy.deepcopy(board))

dfs(0, 0, 0, board)
print(ans)