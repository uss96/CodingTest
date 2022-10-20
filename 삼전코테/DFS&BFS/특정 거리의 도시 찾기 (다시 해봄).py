from collections import deque
# 입력값 받기

n, m, k, x = map(int, input().split())

# 그래프 선언 (0 ~ n까지 필요)
graph = [[] for _ in range(n + 1)]

# 그래프 받기
for _ in range(m) :
    a, b = map(int, input().split())
    graph[a].append(b)

# 최단거리 초기화
distance = [-1] * (n + 1)
distance[x] = 0 # x는 거리 0으로 만들기

# bfs 만들기
q = deque([x])
while q:
    now = q.popleft()
    for next_node in graph[now] :
        if distance[next_node] == -1 : # 처음 가볼 경우 최단거리 초기화
            distance[next_node] = distance[now] + 1
            q.append(next_node) # 다음 노드 넣기

check = False
for i in range(1, n + 1) :
    if distance[i] == k :
        check = True
        print(i)

if not check :
    print(-1)