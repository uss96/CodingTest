from collections import deque
# 입력값 받기
n = int(input())
map_info = [list(map(str, input().split())) for _ in range(n)]
map_temp = [[0] * n for _ in range(n)]
teacher = []
blank = []
result = []
t = len(teacher)

for i in range(n) :
    for j in range(n) :
        if map_info[i][j] == 'T' :
            teacher.append((i, j))
        elif map_info[i][j] == 'X' :
            blank.append((i, j))

# 탐지
# direction = 0 -> 서쪽, 1 -> 동쪽, 2 -> 북쪽, 3 -> 남쪽
def tam(x, y, direction) :
    if direction == 0 :
        while y >= 0 :
            if map_info[x][y] == 'S' :
                return True
            elif map_info[x][y] == 'O' or 'T' :
                return False
            y -= 1

    if direction == 1 :
        while y < n :

            if map_info[x][y] == 'S' :
                return True
            elif map_info[x][y] == 'O' or 'T':
                return False
            y += 1

    if direction == 2 :
        while x >= 0 :
            if map_info[x][y] == 'S' :
                return True
            elif map_info[x][y] == 'O' or 'T':
                return False
            x -= 1

    if direction == 3 :
        while x < n :

            if map_info[x][y] == 'S' :
                return True
            elif map_info[x][y] == 'O' or 'T':
                return False
            x += 1

    return False

def dfs(depth, idx) :

    if depth == 3 :
        q = deque(teacher)
        count = 0
        while q:
            x, y = q.popleft()
            for direction in range(4) :
                if not tam(x, y, direction) :
                    count += 1
        if count * 4 == t :
            result.append('YES')


    for i in range(idx, len(blank)):
        a, b = blank[i]
        map_info[a][b] = 'O'

        dfs(depth + 1, idx + 1)
        map_info[a][b] = 'X'


dfs(0,0)
if result == [] :
    print ('NO')
else :
    print('YES')
