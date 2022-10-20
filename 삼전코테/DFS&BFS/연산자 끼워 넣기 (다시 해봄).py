
# 입력값 받기
n = int(input())
arr = list(map(int, input().split()))
a, b, c, d = map(int, input().split())
result = []

def dfs(depth, now) :
    global a, b, c, d

    if depth == n :
        result.append(now)
        return

    if a > 0 :
        a -= 1
        dfs(depth + 1, now + arr[depth])
        a += 1
    if b > 0 :
        b -= 1
        dfs(depth + 1, now - arr[depth])
        b += 1
    if c > 0 :
        c -= 1
        dfs(depth + 1, now * arr[depth])
        c += 1
    if d > 0:
        d -= 1
        dfs(depth + 1, int(now / arr[depth]))
        d += 1

dfs(1, arr[0])
print(max(result))
print(min(result))
