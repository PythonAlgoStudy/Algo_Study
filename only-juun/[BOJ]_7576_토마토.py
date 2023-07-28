# [BOJ] 7576. 토마토
import sys
from collections import deque
input = sys.stdin.readline

# 입력받기
m, n = tuple(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(n)]

# 범위 내에 있는지 확인
def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

# 익지 않은 토마토인지 확인
def can_go(x, y):
    return in_range(x, y) and arr[x][y] == 0

# 모든 토마토가 익었는지 확인
def all_tomatoes_ripe():
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                return False
    return True

def bfs():
    days = 0
    dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]
    while q:
        x, y, cnt = q.popleft()
        
        days = max(days, cnt)

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny):
                arr[nx][ny] = 1
                q.append((nx, ny, cnt + 1))
    return days

q = deque()
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            q.append((i, j, 0))

answer = bfs()

print(answer if all_tomatoes_ripe() else -1)
