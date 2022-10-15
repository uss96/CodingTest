# 입력값 받기
n = int(input())
k = int(input())

map_info = [[0] * (n + 1) for _ in range (n + 1)]
direct_info = []

# 사과 위치 1로 표시
for _ in range(k) :
    a, b = map(int, input().split())
    map_info[a][b] = 1

# 방향 정보 받기
l = int(input())
for _ in range(l) :
    x, c = input().split()
    direct_info.append((int(x), c))

# 방향 값 설정 (동, 남, 서, 북)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(direction, c) :
    if c == 'L' :
        direction = (direction - 1) % 4
    else :
        direction = (direction + 1) % 4
    return direction

def simulate():
    x, y = 1, 1 # 뱀의 머리 위치
    map_info[x][y] = 2 # 뱀이 존재하는 위치는 2로 표시
    direction = 0 # 처음에 동쪽
    time = 0 # 시작한 이후 지난 시간
    idx = 0 # 다음에 회전할 정보
    q = [(x, y)] # 뱀이 차지하고 있는 위치 정보 (꼬리가 앞쪽)
    while True :
        nx = x + dx[direction]
        ny = y + dy[direction]

        # 맵 범위 안에 있고, 뱀의 몸통이 없는 위치라면
        if 1 <= nx <= n and 1 <= ny <= n and map_info[nx][ny] != 2 :
            # 사과가 없다면 이동 후 꼬리 제거
            if map_info[nx][ny] == 0 :
                map_info[nx][ny] = 2
                q.append((nx, ny))
                px, py = q.pop(0)
                map_info[px][py] = 0
            # 사과가 있다면 이동 후에도 꼬리 유지
            elif map_info[nx][ny] == 1 :
                map_info[nx][ny] = 2
                q.append((nx, ny))

        # 벽이나 뱀의 몸통과 부딪혔다면
        else :
            time += 1
            break

        x, y = nx, ny #다음 위치로 머리통 이동
        time += 1

        if idx < l and time == direct_info[idx][0] : # 회전할 시간인 경우 회전
            direction = turn(direction, direct_info[idx][1])
            idx += 1


    return time

print(simulate())