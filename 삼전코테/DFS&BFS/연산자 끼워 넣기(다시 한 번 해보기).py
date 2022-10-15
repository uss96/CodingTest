n = int(input())
arr = list(map(int, input().split())) # n개
a, b, c, d = (map(int, input().split())) # 연산 개수 입력값

result = []


# dfs 코드
def dfs(depth, now) :
    global a, b, c, d
    # 연산자 n - 1개 되면 계산 진행하고 결과값 저장
    if depth == n :
        result.append(now)
        return

    if a > 0 :
        a -= 1
        dfs(depth + 1, now + arr[depth])
        a += 1
    if b > 0:
        b -= 1
        dfs(depth + 1, now - arr[depth])
        b += 1
    if c > 0:
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