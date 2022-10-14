
# 입력값 받기

n, m = map(int, input().split())
map = [list(map(int, input().split())) for _ in range (n)]

# 치킨, 집, 고르는 치킨집, 출력값 초기 설정
chicken_list = []
house_list = []
choose_list = []
answer = 100000

# 리스트에 추가하기
for i in range(n) :
    for j in range(n) :
        if map[i][j] == 2 :
            chicken_list.append((i, j))
        elif map[i][j] == 1 :
            house_list.append((i, j))

# dfs 함수 만들기
def dfs (depth, idx) :
    global answer
    # depth == m인 경우 치킨거리 계산
    if depth == m :
        sum = 0
        for house in house_list :
            val = 100000
            for choose in choose_list :
                temp = abs(house[0] - choose[0]) + abs(house[1] - choose[1])
                val = min(temp, val)
            sum += val
        answer = min(answer, sum)
        return

    # 조합 부분 만들기
    for i in range(idx, len(chicken_list)) :
        # 만약 이미 있는 조합이면 건너뛰기
        if chicken_list[i] in choose_list :
            continue

        choose_list.append(chicken_list[i])
        dfs(depth + 1, idx + 1)
        choose_list.pop()

dfs(0, 0)
print(answer)


