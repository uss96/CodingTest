from collections import deque

# 입력값 받기
n, l, r = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0

# 특정 위치에서 출발하여 모든 연합을 체크한 뒤에 데이터 댕신
def process (x, y, idx) :
    # (x, y)의 위치와 연결된 나라(연합) 정보를 담는 리스트
    united = []
    united.append((x, y))

    # BFS를 위한 큐 자료구조 정의
    q = deque()
    q.append((x, y))
    union[x][y] = idx  # 현재 연합의 번호 할당
    summary = graph[x][y] # 현재 연합의 전체 인구 수
    count = 1 # 현재 연합의 국가 수
    # 큐가 빌 때까지 반복
    while q:
        x, y = q.popleft()
        # 현재 위치에서 4가지 방향 확인
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            # 바로 옆에 있는 나라 확인
            if 0 <= nx < n and 0 <= ny < n and union[x][y] == -1 :
                # 옆에 있느 ㄴ나라와 인구 차이가 L명 이상, R명 이하라면
                if l <= abs(graph[x][y] - graph[nx][ny]) <= r :
                    q.append((nx, ny))
                    # 연합ㅇ ㅔ추가
                    union[nx][ny] = idx
                    summary += graph[nx][ny]
                    count += 1
                    united.append((nx, ny))

    # 연합 국가끼리 인구를 분배
    for i, j in united :
        graph[i][j] = summary // count
    return count

total_count = 0

# 더 이상 인구 이동을 할 수 없을 때까지 반복
while True :
    union = [[-1] * n for _ in range(n)]
    idx = 0
    for i in range(n) :
        for j in range(n) :
            if union[i][j] == -1 : #해당 나라가 아직 처리되지 않았다면
                process(i, j, idx)
                idx += 1
    # 모든 인구 이동이 끝난 경우
    if idx == n * n :
        break
    total_count += 1

# 인구 이동 횟수 출력
print(total_count)