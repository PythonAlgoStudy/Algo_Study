from collections import deque

N, M = map(int, input().split())
matrix = [input() for _ in range(N)]
dxs, dys = [0, 0, 1, -1], [1, -1, 0, 0]
is_valid = lambda x, y: 0 <= x < N and 0 <= y < M if True else False
visited = [[[False for _ in range(M)] for _ in range(N)] for _ in range(2)]
# distance = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(2)]
distance = []
def bfs():
    q = deque([(0, 0, 1, 0)]) # x, y, chance, distance
    while q:
        x, y, c, d = q.popleft()  # c as chance
        if x == N-1 and y == M-1:
            # print(min(distance[0][N-1][M-1],distance[1][N-1][M-1]))
            distance.append(d+1)
            continue
        if visited[c][x][y]:
            continue
        visited[c][x][y] = True
        for dx, dy in zip(dxs, dys):
            nx, ny = x+dx, y+dy #new x, new y
            if not is_valid(nx, ny):
                continue
            if matrix[nx][ny] == "0":
                q.append((nx, ny, c, d+1))
            elif matrix[nx][ny] == "1" and c == 1:
                q.append((nx, ny, 0, d+1))
            else:
                pass
    #Failed
        # print(q)

    if distance:
        print(min(distance))
    else:
        print(-1)
bfs()
