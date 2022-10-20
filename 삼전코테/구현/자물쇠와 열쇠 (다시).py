# 입력값 받기
m, n = map(int, input().split())
key = [list(map(int, input().split())) for _ in range(m)]
lock = [list(map(int, input().split())) for _ in range(n)]

wide_lock = [[1] * 3 * n for _ in range(3 * n)]
for i in range(n) :
    for j in range (n) :
        wide_lock[i + n][j + n] = lock[i][j]

def rot90 (a) :
    a = list(zip(*a[::-1]))
    return a

def check (wide_lock) :
    l = len(wide_lock) // 3
    for i in range(l, 2*l) :
        for j in range(l, 2*l) :
            if wide_lock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    for _ in range(4) :
        key = rot90(key)

        for x in range(n * 2) :
            for y in range (n * 2) :
                for i in range(m) :
                    for j in range(m) :
                        wide_lock[x + i][y + j] += key[i][j]

                if check(wide_lock) == True :
                    return True
                for i in range(m):
                    for j in range(m):
                        wide_lock[x + i][y + j] -= key[i][j]
        return False

print(solution(key, lock))