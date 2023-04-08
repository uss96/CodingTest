# 입력값

N, M, K = map(int, input().split())

fireball = []
for _ in range(M) :
    r, c, m, s, d = list(map(int, input().split()))
    fireball.append([r, c, m, s, d])

fire_map = [[[] for _ in range(N)] for _ in range(N)]

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

# 파이어볼 이동!

for _ in range(K) :
    while fireball :
        sr, sc, sm, ss, sd = fireball.pop(0)
        nr = (sr + ss * dx[sd]) % N
        nc = (sc + ss * dy[sd]) % N
        fire_map[nr][nc].append([sm, ss, sd])

    for x in range(N):
        for y in range(N) :
            # 파이어볼이 2개 이상인 경우
            if len(fire_map[x][y]) > 1 :
                sum_m, sum_s, cnt_odd, cnt_even, cnt = 0, 0, 0, 0, len(fire_map[x][y])

                while fire_map[x][y] :
                    bm, bs, bd = fire_map[x][y].pop(0)
                    sum_m += bm
                    sum_s += bs

                    if bd % 2 == 0 :
                        cnt_even += 1
                    else :
                        cnt_odd += 1

                if cnt_even == cnt or cnt_odd == cnt :
                    nd = [0, 2, 4, 6]
                else :
                    nd = [1, 3, 5, 7]

                if sum_m // 5 != 0 :
                    for d in nd :
                        fireball.append([x, y, sum_m//5, sum_s//cnt, d])
            # 파이어볼 1개인 경우
            if len(fire_map[x][y]) == 1 :
                fireball.append([x, y] + fire_map[x][y].pop())

print(sum([x[2] for x in fireball]))
