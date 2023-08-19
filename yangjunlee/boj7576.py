from collections import deque
m, n = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]

queue=deque([])
dx, dy=[-1, 1, 0, 0] , [0,0,-1,1]
ans=0

for i in range(n):
    for j in range(m):
        if box[i][j]==1:
            queue.append([i,j])

def bfs():
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            xp, yp=x+dx[i], y+dy[i]
            if 0<=xp<n and 0<=yp<m and box[xp][yp]==0:
                box[xp][yp]=box[x][y]+1
                queue.append([xp, yp])
bfs()

for a in box:
    for b in a:
        if b==0:
            print(-1)
            exit(0)
    ans=max(ans, max(a))
print(ans-1)
                
