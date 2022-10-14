# 입력값 받기

n, m = map(int, input().split())
y, x, d = map(int, input().split())
field = [list(map(int, input().split())) for _ in range (n)]

# 방향 설정
# 북 동 남 서 -> 0 1 2 3
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

# 로봇청소기 가동시키기

count = 1
while True :

    field[y][x] = 2 # 청소 끝난 곳을 2로 표기

    for k in (d - 1, d - 1 - 4, -1) : # 1번의 탐색
        k += 4
        if k >= 4 :
            k % 4

        nx = x + dx[k]
        ny = y + dy[k]

        if field[ny][nx] == 0 : # 비어있는 곳
            x = nx
            y = ny
            d = k
            count += 1
            break

    else : # 비어 있는 곳이 없는 경우
        nx = x - dx[k] # 후진
        ny = y - dy[k]

        # 후진 할 곳 있는 경우
        if field[ny][nx] != 1 :
            x = nx
            y = ny

        # 후진 못 하는 경우
        else :
            break

print(count)



