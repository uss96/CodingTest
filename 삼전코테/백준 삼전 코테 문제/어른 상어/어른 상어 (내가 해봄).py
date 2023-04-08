# 입력값 받기

N, M, K = map(int, input().split())

shark_map = [list(map(int, input().split())) for _ in range(N)]

s_d = list(map(int, input().split()))

prior = []
for _ in range(M) :
    temp = []
    for _ in range(4) :
        temp.append(list(map(int, input().split())))
    prior.append(temp)

smell_map = [[[0, 0]] * N for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def smell_timer() :
    for x in range(N) :
        for y in range(N) :
            if smell_map[x][y][1] > 0 :
                smell_map[x][y][1] -= 1

            if shark_map[x][y] != 0:
                smell_map[x][y] = [shark_map[x][y], K]

def shark_move() :
    move_map = [[0] * N for _ in range(N)]

    for x in range(N) :
        for y in range(N) :
            # 상어 찾기
            if shark_map[x][y] != 0 :
                found = False
                d = s_d[shark_map[x][y]-1]
                # 냄새가 가득 차지 않은 경우
                for idx in prior[shark_map[x][y]-1][d-1] :
                    nx = x + dx[idx-1]
                    ny = y + dy[idx-1]

                    # 인덱스 안일 경우
                    if 0 <= nx < N and 0 <= ny < N :
                        if smell_map[nx][ny][1] == 0 :
                            s_d[shark_map[x][y]-1] = idx
                            if move_map[nx][ny] == 0 :
                                move_map[nx][ny] = shark_map[x][y]
                            else :
                                move_map[nx][ny] = min(move_map[nx][ny], shark_map[x][y])
                            found = True
                            break
                # 냄새가 가득 찬 경우
                if found :
                    continue

                for idx in prior[shark_map[x][y]-1][d-1]:
                    nx = x + dx[idx-1]
                    ny = y + dy[idx-1]

                    if 0 <= nx <N and 0<= ny < N :
                        if smell_map[nx][ny][0] == shark_map[x][y] :
                            s_d[shark_map[x][y]-1] = idx
                            move_map[nx][ny] = shark_map[x][y]
                            break
    return move_map

ans = 0
# 실제 수행 코드
while True :
    smell_timer()
    move_map = shark_move()

    shark_map = move_map
    ans += 1
    verify = True

    for x in range(N) :
        for y in range(N) :
            if shark_map[x][y] > 1 :
                verify = False
                break

    if verify :
        print(ans)
        break

    if ans >= 1000 :
        print(-1)
        break