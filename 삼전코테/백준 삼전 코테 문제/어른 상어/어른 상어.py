n, m, k = map(int, input().split())

# 처음상어 위치
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

# 상어의 초기 방향 정해주기
directions = list(map(int, input().split()))

# 상어의 방향별 우선순위 받아오기(위 아래 왼쪽 오른쪽)
priorities = []
for i in range(m):
    temp = []
    for _ in range(4):
        temp.append(list(map(int, input().split())))
    priorities.append(temp)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 상황판 그리기(상어번호, 냄새가 머무는 시간)
smell = [[[0, 0]] * n for _ in range(n)]

# 모든 냄새 정보 업데이트
def update_smell():
    for i in range(n):
        for j in range(n):
            # 냄새가 남아있는 경우
            if smell[i][j][1] > 0:
                smell[i][j][1] -= 1
            # 상어가 존재하는 위치의 경우
            if data[i][j] != 0:
                smell[i][j] = [data[i][j], k]


# 상어 이동
def move():
    new_data = [[0] * n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if data[x][y] != 0:
                direction = directions[data[x][y] - 1] # 초기 이동 방향 정하기
                found = False
                # 상어의 위치인 경우
                for idx in priorities[data[x][y] - 1][direction - 1]:
                    nx = x + dx[idx - 1]
                    ny = y + dy[idx - 1]
                    if 0 <= nx < n and 0 <= ny < n:
                        if smell[nx][ny][1] == 0: # 냄새가 나지 않는 곳이라면
                            directions[data[x][y] - 1] = idx # 이동 방향 바꾸기
                            # 상어 이동시키기
                            if new_data[nx][ny] == 0: # 상어가 안 겹치는 경우
                                new_data[nx][ny] = data[x][y]
                            else : # 상어가 겹치는 경우
                                new_data[nx][ny] = min(data[x][y], new_data[nx][ny])
                            found = True # 냄새가 나지 않는 어떤 곳에 이동했기 때문에
                            break
                if found: # 주변이 모두 냄새가 남아있지 않아 어딘가로 이동한 경우
                    continue

                # 주변에 모두 냄새가 남아있다면, 자신의 냄새가 있는 곳으로 이동
                for idx in priorities[data[x][y] - 1][direction - 1]:
                    nx = x + dx[idx - 1]
                    ny = y + dy[idx - 1]
                    if 0 <= nx < n and 0 <= ny < n:
                        if smell[nx][ny][0] == data[x][y]: # 자신의 냄새가 있는 곳이라면
                            # 해당 상어 방향 변경
                            directions[data[x][y] - 1] = idx
                            # 상어 이동시키기
                            new_data[nx][ny] = data[x][y]
                            break
    return new_data

answer = 0
while True:
    update_smell() # 냄새 업데이트 (시간 지나기, 상어 위치에 냄새 뿌리기)
    new_data = move() # 상어 이동
    data = new_data # 데이터 덮어씌우기
    answer += 1 # 1초 지남

    check = True # 상어 1만 있는지 구하는 여부
    for i in range(n):
        for j in range(n):
            if data[i][j] > 1:
                check = False
    if check:
        print(answer)
        break

    # 1000초가 지날 때까지 끝나지 않았다면
    if answer >= 1000:
        print(-1)
        break