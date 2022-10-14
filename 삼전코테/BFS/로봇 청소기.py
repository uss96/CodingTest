# 입력값 받기

n, m = map(int, input().split())
x, y, d = map(int,input().split())
field = [list(map(int, input().split())) for _ in range (n)]

# 방향 설정
# 0, 1, 2, 3 -> 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 청소와 이동
cnt = 1
while True:
    field[x][y] = 2 # 청소 끝난 곳
    for k in range(d - 1, d - 1 - 4, -1) : # 왼쪽 방향부터 탐색하므로
        k += 4 # 계산하기 쉽게 (-) 인덱스를 (+)로 변환
        if k > 3 :
            k = k % 4

        nx = x + dx[k]
        ny = y + dy[k]

        # 청소할 곳이 있을 때
        if field[nx][ny] == 0 :
            x = nx # 청소할 곳으로 이동
            y = ny
            d = k # 바라보는 방향을 움직인 방향으로 바꿔준다.
            cnt += 1 # 청소 하고 카운트 증가
            break

    else : # 모든 방향에 청소할 곳이 없을 때
        nx = x - dx[d]
        ny = x - dy[d]

        # 후진 할 곳이 있을 때
        if field[nx][ny] != 1 :
            x = nx
            y = ny
        # 후진 할 곳이 없을 때
        else :
            break

print(cnt)

