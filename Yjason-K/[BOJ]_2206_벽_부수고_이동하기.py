# 2206. 벽 부수고 이동하기
from collections import deque
import sys

# bfs()
def bfs():
  q = deque()
  q.append([0, 0, 1]) # 시작위치 설정
  # 벽을 부쉈는지에 대한 확인을 위한 3차원 방문 배열 설정
  visited = [ [[0] * 2 for _ in range(M)] for _ in range(N) ]
  visited[0][0][1] = 1 # (1,1) 위치 설정
  
  while q:
    x, y, wall = q.popleft()
    
    # (2,2) 행렬인 경우
    if x == N-1 and y == M-1:
      return visited[x][y][wall] # 도착했을 때의 거리를 반환합니다.

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
      nx, ny = x + dx, y + dy
      
      if 0 <= nx < N and 0 <= ny < M:
        # 벽이 없는 경우
        if arr[nx][ny] == 0 and visited[nx][ny][wall] == 0:
          visited[nx][ny][wall] = visited[x][y][wall] + 1
          q.append([nx, ny, wall])
        
        # 벽이 있고 부술 수 있는 경우
        elif arr[nx][ny] == 1 and wall == 1:
          visited[nx][ny][0] = visited[x][y][wall] + 1
          q.append([nx, ny, 0])
        
  return -1

# 입력값 설정
input = sys.stdin.readline
N, M = map(int, input().split())
arr = [ list(map(int, list(input().strip()))) for _ in range(N) ]

print(bfs())
