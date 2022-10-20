from collections import deque
# 입력값 받기
n, k = map(int, input().split())
map_info = [list(map(int, input().split())) for _ in range(n)]
s, x, y = map(int, input().split())

x = x - 1
y = y - 1

virus_pos = []
for i in range(n) :
    for j in range(n) :
        if map_info != 0 :
            virus_pos.append((map_info[i][j], i, j))

virus_pos.sort()

da = [-1, 1, 0, 0]
db = [0, 0, -1, 1]

# 바이러스 퍼지게 하기
def virus_spread (c, a, b, count) :

    for i in range(4) :
        na = a + da[i]
        nb = b + db[i]

        if 0 <= na < n and 0 <= nb < n and map_info[na][nb] == 0 :
            map_info[na][nb] = c
            count += 1
            virus_pos.append((c, na, nb))

    return count

def dfs(depth) :
    count = 1

    q = deque(virus_pos)

    while q :

        count = 0

        for _ in range(len(virus_pos)) :
            c, a, b = q.popleft()
            virus_spread(c, a, b, count)

        depth += 1

        if depth == s or count == 0:
            print(map_info[x][y])
            break

        virus_pos.sort()

dfs(0)