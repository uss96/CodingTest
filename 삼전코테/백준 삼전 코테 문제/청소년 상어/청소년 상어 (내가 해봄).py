import copy
# 초기값 설정
fish_map = [[] for _ in range(4)]
ans = 0

# 방향 설정
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

# 입력값 받기
for i in range(4) :
    data = list(map(int, input().split()))
    fish_data = []

    for j in range(4) :
        fish_data.append([data[2*j], data[2*j+1]-1])

    fish_map[i] = fish_data

# dfs 만들기
def dfs(s_x, s_y, score, fish_map) :
    global ans # ans 글로벌 변수 선언

    score += fish_map[s_x][s_y][0] # 상어 있는 곳의 물고기 먹음
    ans = max(ans, score) # 글로벌 변수 ans와 score 중 큰 값으로 넣기
    fish_map[s_x][s_y][0] = 0 # 상어가 먹은 물고기 빼기

    # 물고기들의 행진, 1부터 16까지 순서대로
    for i in range(1, 17) :
        f_x, f_y = -1, -1
        for x in range (4) :
            for y in range(4) :
                if fish_map[x][y][0] == i :
                    f_x, f_y = x, y
                    break
        if f_x == -1 and f_y == -1 : # 물고기가 어항 안에 없는 경우
            continue
        f_d = fish_map[f_x][f_y][1]

        for j in range(8) :
            nd = (f_d + j) % 8
            nx = f_x + dx[nd]
            ny = f_y + dy[nd]

            if not (0 <= nx < 4 and 0 <= ny < 4) or (nx == s_x and ny == s_y) : # 물고기 위치가 어항 밖이나 상어 위치인 경우
                continue

            fish_map[f_x][f_y][1] = nd
            fish_map[f_x][f_y], fish_map[nx][ny] = fish_map[nx][ny], fish_map[f_x][f_y] # 물고기 바꿔치기
            break

    # 청소년 상어의 식사 시간
    s_d = fish_map[s_x][s_y][1]
    for i in range(1, 5) :
        nx = s_x + dx[s_d] * i
        ny = s_y + dy[s_d] * i

        if (0 <= nx < 4 and 0 <= ny < 4) and (fish_map[nx][ny][0] > 0) :
            dfs(nx, ny, score, copy.deepcopy(fish_map))

dfs(0, 0, 0, fish_map)
print(ans)

