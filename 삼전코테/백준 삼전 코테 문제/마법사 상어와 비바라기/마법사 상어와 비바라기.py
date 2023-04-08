# 입력값 받기

N, M = map(int, input().split())

bucket_map = []
for _ in range(N):
    bucket_map.append(list(map(int, input().split())))

cloud_data = []
for _ in range(M):
    d, s = list(map(int, input().split()))
    cloud_data.append([(d, s)])

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

cloud_map = [[N-1, 0], [N-1, 1], [N-2, 0], [N-2, 1]]

def move_rain_copy_make(bucket_map, cloud_map, cloud_data) :
    pd, ps = cloud_data.pop(0)
    new_cloud_map = []
    no_cloud_map = []
    real_new_cloud_map = []

    while cloud_map :
        x, y = cloud_map.pop(0)
        nx = (x + dx[pd-1]*ps) % N
        ny = (y + dy[pd-1]*ps) % N
        new_cloud_map.append([nx, ny])
        bucket_map[nx][ny] += 1

    while new_cloud_map :
        x, y = new_cloud_map.pop(0)
        no_cloud_map.append([x, y])
        count = 0
        for d in range(4) :
            nx = x + dx[2*d+1]
            ny = y + dy[2*d+1]

            if 0<= nx < N and 0 <= ny < N and bucket_map[nx][ny] > 0 :
                count += 1

        bucket_map[x][y] += count

    for i in range(N) :
        for j in range(N) :
            if [i, j] not in no_cloud_map and bucket_map[i][j] >= 2 :
                real_new_cloud_map.append([i, j])
                bucket_map[i][j] -= 2

    return bucket_map, real_new_cloud_map

for i in range(M) :
    bucket_map, cloud_map = move_rain_copy_make(bucket_map, cloud_map, cloud_data[i])


water = 0
for x in range(N) :
    for y in range(N) :
        water += bucket_map[x][y]

print(water)