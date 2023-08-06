import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())
board = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
ans = 0


def bfs():
    q = deque([(0, 0, 0)])
    visited[0][0][0] = 1

    while q:
        r, c, wall = q.popleft()
        if r == N - 1 and c == M - 1:
            return visited[r][c][wall]

        for i in range(4):
            nr = r + dir[i][0]
            nc = c + dir[i][1]
            if 0 <= nr < N and 0 <= nc < M and visited[nr][nc][wall] == 0:
                if board[nr][nc] == 0:
                    q.append((nr, nc, wall))
                    visited[nr][nc][wall] = visited[r][c][wall] + 1
                
                if wall == 0 and board[nr][nc] == 1:
                    q.append((nr, nc, 1))
                    visited[nr][nc][1] = visited[r][c][wall] + 1

    return -1


print(bfs())
