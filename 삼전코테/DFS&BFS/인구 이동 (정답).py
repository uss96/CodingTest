import sys
sys.setrecursionlimit(100000) # 최대 재귀 한도를 늘린다.

N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]

def solution():
    cnt = 0
    # 인접한 국가와의 인구 차이를 통해 연합 유무 탐색
    def dfs(x, y):
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and check[nx][ny]:
                if L <= abs(arr[x][y] - arr[nx][ny]) <= R:
                    check[nx][ny] = False
                    union.append([nx, ny])
                    dfs(nx, ny)

    while True:
        check = [[True] * N for _ in range(N)] # 탐색 유무
        flag = True
        for i in range(N):
            for j in range(N):
                union = []
                if check[i][j]:
                    union.append([i, j]) # 연합 나라 저장
                    check[i][j] = False
                    dfs(i, j)

                    if len(union) > 1:
                        flag = False
                        avg = sum([arr[x][y] for x, y in union]) // len(union)
                        for x, y in union:
                            arr[x][y] = avg

        if flag: # 연합의 개수가 2개 이상인 적이 없으면 종료
            break

        cnt += 1

    return cnt

print(solution())