# 입력값 받기
n, m = map(int, input().split())
lock = [list(map(int, input().split())) for _ in range(n)]
key = [list(map(int, input().split())) for _ in range(m)]


# a = list(map(list, zip(*a[::-1])))

def check(new_lock) :
    lock_length = len(new_lock) // 3
    for i in range(lock_length, lock_length * 2) :
        for j in range(lock_length, lock_length * 2) :
            if new_lock[i][j] != 1:
                return False
    return True

def solution(key, lock) :
    n = len(lock)
    m = len(key)

    # 자물쇠의 크기를 기존의 3배로 변환
    new_lock = [[0] * (3 * n) for _ in range (3 * n)]
    # 새로운 자물쇠의 중간 부분에 기존 자물쇠 넣기
    for i in range (n) :
        for j in range (n) :
            new_lock[i+n][j+n] = lock[i][j]

    # 4가지 방향에 대해서 확인
    for rotation in range(4) :
        key = list(map(list, zip(*key[::-1]))) # 열쇠 회전
        for x in range (n * 2) :
            for y in range (n * 2) :
                # 자물쇠에 열쇠 끼워 넣기
                for i in range(m) :
                    for j in range(m) :
                        new_lock[x + i][y + j] += key[i][j]
                # 새로운 자물쇠에 열쇠가 정확히 맞는지 검사
                if check(new_lock) == True :
                    return True
                # 자물쇠에서 열쇠 다시 빼기
                for i in range (m) :
                    for j in range(m) :
                        new_lock[x+i][y+j] -= key[i][j]
    return False

