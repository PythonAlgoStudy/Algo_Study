n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

visit = [[False]*m for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

ans = 0

def dfs(x,y,s,v):
    global ans
    if v == 4:
        ans = max(ans,s)
        return
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx>=0 and nx<n and ny>=0 and ny<m and visit[nx][ny] == False:
            visit[nx][ny] = True
            dfs(nx,ny,s+arr[nx][ny],v+1)
            visit[nx][ny] = False

def T(x, y):
    global ans
    for k in range(4):
        s = arr[x][y]
        b = 1
        for i in range(4):
            if i == k:
                continue
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                b = 0
                break
            s += arr[nx][ny]
        if b:
            ans = max(ans, s)
    
    
for i in range(n):
    for j in range(m):
        if visit[i][j] == False:
            visit[i][j] = True
            dfs(i,j,arr[i][j],1)
            visit[i][j] = False

for i in range(n):
    for j in range(m):
        T(i,j)
print(ans)