# 입력값 받기

n, m = map(int, input().split())
y, x, d = map(int, input().split())
map = [list(map(int, input().split())) for _ in range (n)]

# 방향 설정
# 북 동 남 서 -> 0 1 2 3
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

# 로봇 청소기 동작 코드
count = 1
while True :
    map[y][x] = 2 # visited

    for k in (d - 1, d - 1 - 4, -1) : # 로청 1회 동작
        k += 4 # 인덱스 +로 변경

        if k > 3 : # 3 초과할 경우 나눠주기
            k % 4

        nx = x + dx[k]
        ny = y + dy[k]

        if map[ny][nx] == 0 : # 청소할 수 있는 경우
            x = nx
            y = ny
            d = k
            count += 1
            break

    else : # 청소할 수 없는 경우
        nx = x - dx[k] # 후진
        ny = y - dy[k]

        if map[ny][nx] != 1 : # 뒤가 벽이 아닌 경우
            x = nx
            y = ny
        else : # 뒤가 벽인 경우
            break


print(count)