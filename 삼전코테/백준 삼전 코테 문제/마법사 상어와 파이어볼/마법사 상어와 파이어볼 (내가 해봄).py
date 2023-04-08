dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

# 입력값 받기
N, M, K = map(int, input().split())

fireball = []
firemap = [[[] for _ in range(N)] for _ in range(N)]

for _ in range(M) :
    r, c, m, s, d = list(map(int, input().split()))
    fireball.append([r - 1, c - 1, m, s, d])

# 파이어볼 K번 움직이기!

for _ in range(K):

    while fireball : # fireball 전부에 대해 움직임 시행
        sr, sc, sm, ss, sd = fireball.pop(0)
        nr = (sr + ss * dx[sd]) % N
        nc = (sc + ss * dy[sd]) % N
        firemap[nr][nc].append([sm, ss, sd])

    # firemap에 파이어볼 여러 개 있는 경우 찾기
    for x in range(N):
        for y in range(N) :
            if len(firemap[x][y]) > 1 :
                total_m, total_s, count_odd, count_even, count = 0, 0, 0, 0, len(firemap[x][y])
                while firemap[x][y] :
                    pm, ps, pd = firemap[x][y].pop()
                    total_m += pm
                    total_s += ps

                    if pd % 2 == 0 :
                        count_even += 1
                    else :
                        count_odd += 1

                if count_even == count or count_odd == count :
                    nd = [0, 2, 4, 6]
                else :
                    nd = [1, 3, 5, 7]

                if total_m // 5 != 0:
                    for d in nd :
                        fireball.append([x, y, total_m//5, total_s//count, d])
    # fireball 한 개인 경우
            if len(firemap[x][y]) == 1 :
                fireball.append([x, y] + firemap[x][y].pop())

print(sum([x[2] for x in fireball]))