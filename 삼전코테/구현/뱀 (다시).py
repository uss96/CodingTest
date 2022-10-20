
# 입력값 받기
n = int(input())
k = int(input())

map_info = [[0] * (n + 1) for _ in range(n + 1)]
direct_info = []
for i in range(k) :
    a, b = map(int, input().split())
    map_info[a][b] = 1

# 방향 정보 (동 남 서 북)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

l = int(input())
for _ in range(l) :
    x, c = input().split()
    direct_info.append(x, c)

def turn(direction, c) :
    if c == 'L' :
        direction = (direction - 1) % 4
    else :
        direction = (direction + 1) % 4
    return direction

def action() :
    x, y = 1, 1
    map_info[x][y] = 2
    direction = 0
    time = 0
    idx = 0
    q = [(x, y)]

    while True :
        nx = x + dx[direction]
        ny = y + dy[direction]

        if 0< nx <= n and 0 < ny <= n and map_info[nx][ny] != 2 :
            if map_info[nx][ny] == 0 :
                q.append((nx, ny))
                map_info[nx][ny] = 2
                px, py = q.pop(0)
                map_info[px][py] = 0

            if map_info[nx][ny] == 1 :
                q.append((nx, ny))
                map_info[nx][ny] = 2

        else :
            time += 1
            break

        x = nx
        y = ny
        time += 1

        if idx < l and time == direct_info[idx][0] :
            direction = turn(direction, direct_info[idx][1])
            idx += 1

    return time

print(action())