from collections import deque
n, m = map(int, input().split())
box = [list(map(int, list(input()))) for _ in range(n)]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1

queue=deque([[0,0,0]])
dx, dy=[-1, 1, 0, 0] , [0,0,-1,1]


def bfs():
    while queue:
        x,y,z=queue.popleft()
        for i in range(4):
            if x==n-1 and y==m-1: return visited[x][y][z]
            xp, yp=x+dx[i], y+dy[i]
            if xp<0 or xp>=n or yp<0 or yp>=m:continue
            if box[xp][yp]==0 and visited[xp][yp][z]==0:
                visited[xp][yp][z]=visited[x][y][z]+1
                queue.append([xp, yp, z])
            if z==0 and box[xp][yp]==1 and visited[xp][yp][z+1]==0:
                visited[xp][yp][z+1]=visited[x][y][z]+1
                queue.append([xp, yp, z+1])
    return -1


print(bfs())
