from collections import deque
def bfs(graph,x,y,k):
    queue = deque()
    queue.append((x,y))
    graph2[x][y] = 1
    while queue :
        startX,startY = queue.popleft() 
        if(startX-1>=0) and (graph[startX-1][startY]>k) and (graph2[startX-1][startY]==0):
            queue.append((startX-1,startY))
            graph2[startX-1][startY] = 1

        if(startY-1>=0) and (graph[startX][startY-1]>k) and (graph2[startX][startY-1]==0):
            queue.append((startX,startY-1))
            graph2[startX][startY-1] = 1

        if(startX+1<n) and (graph[startX+1][startY]>k) and (graph2[startX+1][startY]==0):
            queue.append((startX+1,startY))
            graph2[startX+1][startY] = 1

        if(startY+1<n) and (graph[startX][startY+1]>k) and (graph2[startX][startY+1]==0):
            queue.append((startX,startY+1))
            graph2[startX][startY+1] = 1

        
n = int(input())
graph = []
for i in range(n):
    temp = list(map(int,input().split()))
    graph.append(temp)
    
    
temp = 0
graph2 = []
answer = 0
maxnum = max(graph[0])
for m in range(n-1):
  if(maxnum <= max(graph[m+1])):
    maxnum = max(graph[m+1])
for k in range(maxnum):
    graph2 = [[0]*n for _ in range(n)]   
    for i in range(n):
      for j in range(n):
        if (graph[i][j]>k) and (graph2[i][j] == 0)  :
            bfs(graph,i,j,k)
            temp += 1
    if answer <= temp:
        answer = temp
    temp = 0
print(answer)
