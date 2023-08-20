import sys
input = sys.stdin.readline
INF = sys.maxsize

n, m = tuple(map(int, input().split()))
relationships = [[INF] * n for _ in range(n)]

# 인접행렬
for _ in range(m):
    i, j = tuple(map(int, input().split()))
    relationships[i - 1][j - 1] = 1
    relationships[j - 1][i - 1] = 1

# 자기자신까지의 거리 = 0
for i in range(n):
    relationships[i][i] = 0

# Floyd-Warshall: 각 정점까지의 최단거리 계산
for k in range(n):
    for i in range(n):
        for j in range(n):
            relationships[i][j] = min(relationships[i][k] + relationships[k][j], relationships[i][j])

# 각 사람의 케빈 베이컨 수 계산
answer = []
for i in range(n):
    kb_number = sum(relationships[i])
    answer.append((i + 1, kb_number))

answer.sort(key = lambda x: (x[1], x[0]))
print(answer[0][0])