import sys
from collections import deque

def bfs(N, M, arr): # bfs를 통한 최소날짜 찾기
  
  q = deque()
  v = [[-1] * M for _ in range(N)] # 가로/ 세로 토마토 상자 방문처리
  
  # 익지 않은 토마토 갯수 확인
  raw = 0  # Initialize cnt as 0
  for i in range(N):
    for j in range(M):
      if arr[i][j] == 0:
        raw += 1
      elif arr[i][j] == 1:
        q.append((i,j))
        v[i][j] = 0
        
  # 재귀를 통한 bfs
  while q:
    ci, cj = q.popleft() # 현재 위치
    
    # 상하좌우 위치를 이동하는 경우
    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
      ni, nj = ci + di, cj + dj # 다음 위치
      # 방문한 위치가 방문하지 않고 토마토가 익지 않은 경우
      if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 0 and v[ni][nj] == -1:
        q.append((ni,nj))
        v[ni][nj] = v[ci][cj] + 1
        raw -= 1 # 익지 않은 토마토의 갯수 줄여나가기
        
  if raw == 0 : # 모든 토마토가 다 익은경우
    return max(map(max, v))
  else:
    return -1 # 토마토가 다 익지 못하는 경우
        
input = sys.stdin.readline
M, N = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
ans = bfs(N, M , arr)
print(ans)