from collections import deque
import sys
INF = sys.maxsize
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]
# 3차원 방문 리스트 초기화. 마지막 차원은 벽을 부순 상태인지 아닌지를 나타냅니다. 
# visited[x][y][0]: (x, y)를 방문하고 벽을 부순 경우
# visited[x][y][1]: (x, y)를 방문하고 벽을 부수지 않은 경우
visited = [[[0]*2 for _ in range(m)] for _ in range(n)]
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]  # 동, 남, 서, 북 방향

def bfs():
    q = deque()
    q.append((0, 0, 1))  # x, y, wall. 시작점과 벽을 아직 부수지 않았음을 의미
    visited[0][0][1] = 1  # 시작 위치 방문 처리

    while q:
        x, y, wall = q.popleft()
        # 도착점에 도달하면 그 때의 이동 횟수를 반환
        if x == n-1 and y == m-1:
            return visited[x][y][wall]

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy  # 다음 위치

            if 0 <= nx < n and 0 <= ny < m:  # 다음 위치가 유효한지 확인
                # 다음 위치에 벽이 있고, 아직 벽을 부순 적이 없는 경우
                if board[nx][ny] == '1' and wall == 1:
                    visited[nx][ny][0] = visited[x][y][1] + 1  # 벽을 부수고 이동
                    q.append((nx, ny, 0))  # 벽을 부순 상태로 큐에 추가

                # 다음 위치가 벽이 아니고, 아직 방문하지 않은 경우
                elif board[nx][ny] == '0' and visited[nx][ny][wall] == 0:
                    visited[nx][ny][wall] = visited[x][y][wall] + 1  # 이동
                    q.append((nx, ny, wall))  # 현재 상태 그대로 큐에 추가

    return -1  # 모든 칸을 확인한 후에도 도착점에 도달하지 못한 경우 -1 반환

print(bfs())
