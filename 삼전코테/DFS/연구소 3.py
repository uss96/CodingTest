from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]

visited = [[0] * n for _ in range(n)]
test_visited = [[0] * n for _ in range(n)]

virus = []
active = []
blank = False

test_map = [[0] * n for _ in range (n)]

for i in range(n) :
    for j in range(n) :
        if map[i][j] == 1 :
            map[i][j] = -1

        elif map[i][j] == -2 :
            map[i][j] = -2
            virus.append((i, j))

answer = 100000
flag = False

def dfs(cnt, idx) :
    global flag, answer
    local_ans = 0
    if cnt == m :
        for i in range(n):
            for j in range(n) :
                test_map[i][j] = map[i][j]
                test_visited[i][j] = visited[i][j]

        for x, y, cur_time in active :
            test_visited[x][y] = 1

        q = deque(active)
        while q :
            x, y, cur_time = q.popleft()
            for i in range(4) :
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < n and not test_visited[nx][ny] :
                    test_visited[nx][ny] = 1

                    if test_map[nx][ny] == 0 :
                        test_map[nx][ny] = cur_time + 1
                        q.append(nx, ny, test_map[nx][ny])

                    elif test_map[nx][ny] == -2 :
                        q.append(nx, ny, cur_time + 1)

        for i in range (n) :
            for j in range (n) :
                if test_map[i][j] == 0 :
                    return

                if local_ans < test_map[i][j] :
                    local_ans = test_map[i][j]

        flag = True
        answer = min(answer, local_ans)
        return

    for i in range (idx, len(virus)) :
        active.append((virus[i][0], virus[i][1], 0))
        dfs(cnt + 1, idx + 1)
        active.pop()

for i in range(n) :
    for j in range(n) :
        if map[i][j] == 0 and not blank :
            blank = True

if not blank :
    print(0)
else :
    dfs(0, 0)
    if not flag :
        print(-1)
    else :
        print(answer)
