n,m = map(int,input().split())
r,c,d = map(int,input().split()) # d 0,1,2,3 : 위,오른쪽,아래,왼쪽
graph = [list(map(int,input().split())) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
dir = {0:(-1,0),1:(0,1),2:(1,0),3:(0,-1)}

ans = 0
 
x,y = r,c
while True:
    
    if graph[x][y] == 0:
        ans+=1
        graph[x][y] = 2 # 청소완료
    
    # 청소되지 않은 빈칸 있는 경우 True
    is_clean = False
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if graph[nx][ny] == 0 :
            is_clean = True
            break
    
    
    if is_clean:
        d = d-1 if d>0 else 3
        nx,ny = x + dir[d][0], y + dir[d][1]
        if graph[nx][ny] == 0:
            x,y = nx,ny
    
    else:
        back = {0:2,1:3,2:0,3:1}
        nx,ny = x + dir[back[d]][0], y + dir[back[d]][1]
        if graph[nx][ny] == 1:
            break
        else:
            x,y = nx,ny

print(ans)