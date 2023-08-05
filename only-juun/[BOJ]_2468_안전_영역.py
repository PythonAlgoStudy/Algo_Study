import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
arr = []
min_height, max_height = sys.maxsize, -1
for _ in range(n):
    row = list(map(int, input().split()))
    min_height, max_height = min(min(row), min_height), max(max(row), max_height)
    arr.append(row)
visited = [[False for _ in range(n)] for _ in range(n)]

# 방문 여부 배열 초기화
def initialize():
    for i in range(n):
        for j in range(n):
            visited[i][j] = False

# 배열 범위 확인
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

# 진행 가능한 칸인지 확인
def can_go(x, y, height):
    return in_range(x, y) and arr[x][y] > height and not visited[x][y]

# 영역 탐색
def bfs(height):
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny, height):
                visited[nx][ny] = True
                q.append((nx, ny))

answer = 1
q = deque()
for height in range(min_height, max_height):
    cnt = 0
    for i in range(n):
        for j in range(n):
            # 한번 탐색을 진행할 때마다 1개의 영역을 체크할 수 있음
            if arr[i][j] > height and not visited[i][j]:
                visited[i][j] = True
                q.append((i, j))
                bfs(height)
                cnt += 1
    initialize()
    answer = max(cnt, answer)

print(answer)