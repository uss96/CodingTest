# 입력값 받기
from collections import deque

n, k = map(int, input().split())
map_info = [list(map(int, input().split())) for _ in range(n)]
s, x, y = map(int, input().split())

x = x - 1
y = y - 1

virus_pos = []

# 바이러스 위치 파악하기

for i in range(n):
    for j in range(n) :
        if map_info[i][j] != 0 :
            virus_pos.append((map_info[i][j], i, j))

virus_pos.sort()
q = deque(virus_pos)

# 바이러스 퍼뜨리기
da = [1, -1, 0, 0]
db = [0, 0, 1, -1]

# 바이러스 1번 퍼뜨리기
def virus(c, a, b, temp) :
    for i in range(4) :
        na = a + da[i]
        nb = b + db[i]

        if 0 <= na < n and 0 <= nb < n and map_info[na][nb] == 0:
            map_info[na][nb] = c
            q.append((c, na, nb))
            temp += 1

    return temp


# dfs문 만들기
def dfs(count) :
    temp = 1

    # 바이러스 퍼뜨리기
    while q:

        temp = 0
        for _ in range (len(virus_pos)) :
            c, a, b = q.popleft()
            virus(c, a, b, temp)

        count += 1
        # count가 s이거나 virus가 더 이상 퍼지지 않는 경우 결과값 출력
        if count == s or temp == 0:
            print(map_info[x][y])
            break

        virus_pos.sort()

dfs(0)