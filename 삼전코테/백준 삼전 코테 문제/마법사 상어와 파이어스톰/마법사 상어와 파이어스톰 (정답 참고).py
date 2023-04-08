# 입력값 받기

N, Q = map(int, input().split())

ice_map = []
for _ in range(2**N) :
    ice_map.append(list(map(int, input().split())))

L_list = list(map(int, input().split()))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def rotate_90(ice_map, l) :
    new_map = [[0 for _ in range(2**N) ] for _ in range(2**N)]

    for i in range(0, 2**N, 2**l):
        for j in range(0,2**N, 2**l):
            for k in range(2**l) :
                for m in range(2**l) :
                    new_map[i+k][j+m] = ice_map[i+2**l-m-1][j+k]

    return new_map

def melt(ice_map) :
    new_map = [[0 for _ in range(2**N)] for _ in range(2**N)]
    for i in range(2**N):
        for j in range(2**N):
            ice_num = 0
            for d in range(4) :
                nx = i + dx[d]
                ny = j + dy[d]

                if 0 <= nx < 2**N and 0 <= ny < 2**N :
                    if ice_map[nx][ny] > 0 :
                        ice_num += 1


            if ice_num >= 3 :
                new_map[i][j] = ice_map[i][j]
            else :
                new_map[i][j] = ice_map[i][j] - 1

    return new_map

for i in range(Q) :

    ice_map = rotate_90(ice_map, L_list[i])
    ice_map = melt(ice_map)

sum_ice, max_size = 0, 0
visited = [[False for _ in range(2**N)] for _ in range(2**N)]

for x in range(2**N):
    for y in range(2**N):
        if visited[x][y] == False and ice_map[x][y] > 0 :
            ice_size = 1
            check = [[x, y]]
            sum_ice += ice_map[x][y]
            visited[x][y] = 1

            while check :
                i, j = check.pop(0)
                for d in range(4):
                    nx = i + dx[d]
                    ny = j + dy[d]

                    if 0 <= nx < 2**N and 0 <= ny < 2**N :
                        if ice_map[nx][ny] > 0 and visited[nx][ny] == False :
                            ice_size += 1
                            visited[nx][ny] = True
                            sum_ice += ice_map[nx][ny]
                            check.append([nx, ny])

            max_size = max(max_size, ice_size)

print(sum_ice)
print(max_size)
