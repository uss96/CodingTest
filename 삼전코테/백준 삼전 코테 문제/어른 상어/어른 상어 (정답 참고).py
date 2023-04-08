# 입력값 받기

N, M, K  = map(int, input().split())

data = [list(map(int, input().split())) for _ in range(N)]
directions = list(map(int, input().split()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

prior = []
for _ in range(M) :
    temp = []
    for _ in range(4) :
        temp.append(list(map(int, input().split())))
    prior.append(temp)

smell_map = [[[0, 0]] * N for _ in range(N)]

def update_smell() :
    for i in range(N) :
        for j in range(N) :
            if smell_map[i][j][1] > 0 :
                smell_map[i][j][1] -= 1

            if data[i][j] != 0:
                smell_map[i][j] = [data[i][j], K]

def move() :
    new_data = [[0] * N for _ in range(N)]
    for x in range(N) :
        for y in range(N) :
            # 상어가 있을 때
            if data[x][y] != 0 :
                # 초기 이동 방향
                d = directions[data[x][y] - 1]
                found = False

                for idx in prior[data[x][y]-1][d-1] :
                    nx = x + dx[idx - 1]
                    ny = y + dy[idx - 1]

                    if 0 <= nx < N and 0 <= ny < N :
                        # 냄새가 주변에 꽉 차지 않은 경우
                        if smell_map[nx][ny][1] == 0 :
                            directions[data[x][y] - 1] = idx
                            if new_data[nx][ny] == 0 :
                                new_data[nx][ny] = data[x][y]
                            else :
                                new_data[nx][ny] = min(new_data[nx][ny], data[x][y])
                            found = True
                            break
                if found :
                    continue

                # 주변에 냄새 꽉찬 경우
                for idx in prior[data[x][y]-1][d-1] :
                    nx = x + dx[idx - 1]
                    ny = y + dy[idx - 1]
                    if 0 <= nx < N and 0 <= ny < N :
                        if smell_map[nx][ny][0] == data[x][y] :
                            directions[data[x][y]-1] = idx
                            new_data[nx][ny] = data[x][y]
                            break
    return new_data

ans = 0

while True :
    update_smell()
    new_data = move()
    data = new_data
    verify = True
    ans += 1

    for x in range(N):
        for y in range(N) :
            if data[x][y] > 1 :
                verify = False

    if verify :
        print(ans)
        break

    if ans >= 1000 :
        print(-1)
        break