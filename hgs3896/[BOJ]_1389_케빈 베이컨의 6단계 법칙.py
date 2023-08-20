from collections import deque, defaultdict

# 입력 처리
N, M = map(int, input().split())
graph = defaultdict(set)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)

# bacon[i][j] = i와 j 사이의 케빈 베이컨 수
bacon = defaultdict(lambda: defaultdict(int))
for i in range(1, N+1):
    # i에서 시작하는 bfs로 다른 정점에 대해 케빈 베이컨 수(정점 i로부터의 최단거리) 계산
    q = deque([(i, 0)])
    while q:
        node, dist = q.popleft()

        for next_node in graph[node]:
            # next_node가 bacon[i]에 없는 것을 체크하여 중복 방문을 막음
            if next_node not in bacon[i]:
                bacon[i][next_node] = dist+1
                q.append((next_node, dist+1))

# 케빈 베이컨 수의 합이 가장 작은 정점을 출력
print(min(bacon, key=lambda x: sum(bacon[x].values())))
