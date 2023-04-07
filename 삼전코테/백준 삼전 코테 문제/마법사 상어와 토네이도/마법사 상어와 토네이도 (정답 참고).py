# 입력값 받기

N = int(input())
sand = [list(map(int, input().split())) for _ in range(N)]

# 초기값 및 정답 담을 변수 설정
s_x, s_y = N // 2, N // 2
ans = 0

# 방향 설정 (왼, 아래, 오, 위)
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

# 방향별 모래 이동 비율 설정
left = [(1, 1, 0.01), (-1, 1, 0.01), (1, 0, 0.07), (-1, 0, 0.07), (1, -1, 0.1),
        (-1, -1, 0.1), (2, 0, 0.02), (-2, 0, 0.02), (0, -2, 0.05), (0, -1, 0)]
right = [(x, -y, z) for x, y, z in left]
up = [(y, x, z) for x, y, z in left]
down = [(-y, x, z) for x, y, z in left]
dict = {0 : left, 1 : down, 2 : right, 3 : up}

# a 구하고 이동 시 sand 재조정하는 함수 만들기

def sandstorm(s_x, s_y, direction) :
    global ans

    if s_y < 0 :
        return

    total = 0  # a 구하기 위해
    for dx, dy, z in direction :
        nx = s_x + dx
        ny = s_y + dy

        if z == 0 : # a 차례
            new_sand = sand[s_x][s_y] - total
        else :
            new_sand = int(sand[s_x][s_y] * z)
            total += new_sand

        if 0 <= nx < N and 0 <= ny < N :
            sand[nx][ny] += new_sand

        else :
            ans += new_sand


# 실제 문제 수행하는 코드
time = 0 # 횟수

for i in range(2 * N - 1) :
    # i // 4 (time + 1), i % 4 (방향 전환)
    d = i % 4 # 방향
    if d == 0 or d == 2 :
        time += 1

    for _ in range(time) :
        n_x = s_x + dx[d]
        n_y = s_y + dy[d]

        sandstorm(n_x, n_y, dict[d])
        s_x, s_y = n_x, n_y

print(ans)