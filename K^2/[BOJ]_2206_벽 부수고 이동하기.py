import sys 
from collections import deque

N,M = map(int, sys.stdin.readline().split() )
# input = sys.stdin.readline
board =[list(map(int,sys.stdin.readline().rstrip())) for _ in range(N)]
visited =[[[0] *2  for _ in range(N)] for _ in range(N)]
dir = [[-1,0],[1,0],[0,-1],[0,1]]
ans =0 

def bfs():
    # (0.0) 출바, 벽 안부숨
    q = deque([(0,0,0)])
    visited[0][0][0] =1
    while q :
        r,c, wall = q.popleft()
        if r == N -1 and c == M -1:
            return visited[r][c][wall]
        for i in range(4):
            nr = r +dir[i][0]
            nc = c = dir[i][1]
            # 맵 범위 아니면 이동, 방문 한번도 없었으면??
            if 0 <=nr<N and 0<=nc<M and visited[nr][nc][wall] ==0:
                # 벽 아니면 이동, 이전경로 +1 visited에 저장
                if board[nr][nc] == 0:
                    q.append((nr,nc,wall))
                    visited[nr][nc][wall] = visited[r][c][wall] +1

                # 벽 1번도 안부수고, 다음 이동시 (벽_
                if wall == 0 and board[nr][nc] == 1:
                    # 벽 부순 상태 1 
                    q.append((nr,nc,1))
                    # 벽 부순상태의 visited[nr][nc][1]에 이전경로 +1 저장
                    visited[nr][nc][1] = visited[r][c][wall]+1