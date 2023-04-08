# 입력값 받기

N, Q = map(int, input().split())
data = []
for i in range(2**N) :
    data.append(list(map(int, input().split())))

L = list(map(int, input().split()))

# 방향 정보
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

# 배열 90도 회전
def rotate_90 (data, l) :
    new_data = [[0 for _ in range(2**N)] for _ in range(2**N)]

    # i, j를 기준으로 2 ** l 크기의 배열만 회전
    for i in range(0, 2**N, 2**l) :
        for j in range(0, 2**N, 2**l) :
            for k in range(2**l) :
                for m in range(2**l) :
                    new_data[i+k][j+m] = data[i + (2**l - 1 - m)][j + k]
    return new_data

# 얼음 녹이기
def melt_ice(data) :
    new_data = [[0 for _ in range(2**N)] for _ in range(2**N)]
    for i in range(2**N) :
        for j in range(2**N):
            ice_count = 0
            for d in range(4) :
                nx = i + dx[d]
                ny = j + dy[d]

                if 0 <= nx < 2**N and 0 <= ny < 2**N :
                    if data[nx][ny] > 0 :
                        ice_count += 1

            if ice_count < 3 :
                new_data[i][j] = data[i][j] - 1

            else :
                new_data[i][j] = data[i][j]

    return new_data

# 실제 코드 수행
for i in range(Q) :
    data = rotate_90(data, L[i])
    data = melt_ice(data)

sum_ice = 0
visited = [[0 for _ in range(2**N)] for _ in range(2**N)]
max_size = 0

for i in range(2**N):
    for j in range(2**N) :
        if visited[i][j] == 0 and data[i][j] > 0 :
            check = [[i, j]]
            sum_ice += data[i][j]
            visited[i][j] = 1
            now_size = 1

            while check :
                x, y = check.pop(0)

                for d in range(4) :
                    nx = x + dx[d]
                    ny = y + dy[d]

                    if 0 <= nx < 2**N and 0 <= ny < 2 **N :
                        if data[nx][ny] > 0 and visited[nx][ny] == 0 :
                            sum_ice += data[nx][ny]
                            check.append([nx, ny])
                            visited[nx][ny] = 1
                            now_size += 1

            max_size = max(max_size,now_size)

print(sum_ice)
print(max_size)