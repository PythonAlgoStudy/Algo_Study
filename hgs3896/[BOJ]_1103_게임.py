import sys
from collections import defaultdict
sys.setrecursionlimit(10**5)

n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]

visited = set()
dist = defaultdict(int)
dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)

class CycleDetect(Exception):
    def __init__(self):
        super().__init__()

def dfs(v = (0, 0), depth = 0):
    r, c = v
    speed = int(board[r][c])
    
    visited.add(v)
    for deltaR, deltaC in zip(dr, dc):
        nr, nc = r + deltaR * speed, c + deltaC * speed
        if not (0 <= nr < n and 0 <= nc < m):
            continue
        if board[nr][nc] == 'H':
            continue
        if (nr, nc) in visited:
            raise CycleDetect()
        if dist[(nr, nc)] >= depth + 1:
            continue
        dfs((nr, nc), depth + 1)
    dist[(r, c)] = max(dist[(r, c)], depth)
    visited.remove(v)

try:
    if board[0][0] != 'H':
        dfs()
    print(max(dist.values(), default=-1) + 1)
except CycleDetect as e:
    print(-1)