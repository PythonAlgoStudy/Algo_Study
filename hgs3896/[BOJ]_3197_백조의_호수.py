import sys
from collections import deque
R, C = map(int, sys.stdin.readline().rstrip().split())
lake = [list(sys.stdin.readline().rstrip()) for _ in range(R)]

def floodfill(r, c, v):
    lake[r][c] = v
    dq = deque([(r, c)])
    while dq:
        r, c = dq.popleft()
        for dr, dc in zip((0, 0, -1, 1), (-1, 1, 0, 0)):
            nr, nc = r+dr, c+dc
            if nr < 0 or nr >= R:
                continue
            if nc < 0 or nc >= C:
                continue
            if lake[nr][nc] != '.':
                continue
            lake[nr][nc] = v
            dq.append((nr, nc))

def near_water(r, c):
    for dr, dc in zip((0, 0, -1, 1), (-1, 1, 0, 0)):
        nr, nc = r+dr, c+dc
        if nr < 0 or nr >= R:
            continue
        if nc < 0 or nc >= C:
            continue
        if lake[nr][nc] != 'X':
            return True
    return False

icebergs = []
cnt = 0
for r in range(R):
    for c in range(C):
        if lake[r][c] == 'L':
            floodfill(r, c, cnt)
            cnt += 1
        elif lake[r][c] == 'X' and near_water(r, c):
            icebergs.append((r, c))

new_cnt = cnt
for r in range(R):
    for c in range(C):
        if lake[r][c] == '.':
            floodfill(r, c, new_cnt)
            new_cnt += 1

icebergs = set(icebergs)
new_icebergs = set()

g = list(range(new_cnt))
def find_parent(y):
    x = y
    while x != g[x]:
        x = g[x]
    # Path Compression
    g[y] = x
    return x

def merge(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a == b:
        return
    g[a] = b

def finished():
    x = find_parent(0)
    for y in range(1, cnt):
        if x != find_parent(y):
            return False
    return True

days = 0
while not finished():
    for r, c in icebergs:
        water = []
        for dr, dc in zip((0, 0, -1, 1), (-1, 1, 0, 0)):
            nr, nc = r+dr, c+dc
            if nr < 0 or nr >= R:
                continue
            if nc < 0 or nc >= C:
                continue
            if lake[nr][nc] == 'X':
                if (nr, nc) not in icebergs:
                    new_icebergs.add((nr, nc))
            else:
                water.append(find_parent(lake[nr][nc]))
        if len(water) > 1:
            for a, b in zip(water[:-1], water[1:]):
                merge(a, b)
        lake[r][c] = find_parent(water[0])
    days += 1
    icebergs, new_icebergs = new_icebergs, set()
print(days)