from collections import deque

m,n = map(int,input().split())

matrix= [list(map(int,input().split())) for _ in range(n)]  

queue = deque([])

dx,dy =[-1,1,0,0],[0,0,-1,1]


ans =0

for  i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            queue.append([i,j])

def bfs():
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx, ny = dx[i] + x, dy[i]+y
           
            if 0<= nx < n  and 0 <= ny < m and matrix[nx][ny] == 0:
                
                matrix[nx][ny] = matrix[x][y] + 1
                queue.append([nx,ny])
bfs()
for i in matrix :
    for j in i:
      
        if j == 0:
            print(-1)
            exit(0)

    ans = max(ans,max(i))

print(ans-1)