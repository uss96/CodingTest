# 입력값 받기
from collections import deque

n = int(input())
map_info = [list(map(str, input().split())) for _ in range(n)]
final_result = []
wall = []
# 방향
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

teacher = []
space = []
for i in range(n) :
    for j in range(n) :
        if map_info[i][j] == 'T' :
            teacher.append((i, j))

        elif map_info[i][j] == 'X' :
            space.append((i, j))

teacher_temp = teacher
t = len(teacher)

# 선생님 탐색
def tam(x, y, direction) :

    if direction == 0 : # 왼쪽 방향
        while y >= 0 :
            if map_info[x][y] == 'S' :
                return True
            elif map_info[x][y] == 'O' :
                return False
            y -= 1

    if direction == 1 : # 오른쪽
        while y < n :
            if map_info[x][y] == 'S' :
                return True
            elif map_info[x][y] == 'O' :
                return False
            y += 1

    if direction == 2 : # 위쪽 방향
        while x >= 0 :
            if map_info[x][y] == 'S' :
                return True
            elif map_info[x][y] == 'O' :
                return False
            x -= 1

    if direction == 3 : # 아래쪽 방향
        while x < 0 :
            if map_info[x][y] == 'S' :
                return True
            elif map_info[x][y] == 'O' :
                return False
            x += 1

    return False

find = []

# dfs 만들기
def dfs (depth, idx) :

    if depth == 3 :
        for x, y in teacher:
            count = 0
            for i in range(4) :
                if not tam(x, y, i) :
                    count += 1
        if count == t * 4 :
            find.append('YES')


    for i in range(idx, len(space)) :
        wall.append(space[i])
        a, b = space[i]
        map_info[a][b] = 'O'
        dfs(depth + 1, idx + 1)
        map_info[a][b] = 'X'
        wall.pop()

dfs(0, 0)
if find == [] :
    print('NO')
else :
    print('YES')