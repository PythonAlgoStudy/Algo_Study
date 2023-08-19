import sys
input =sys.stdin.realine
sys.setrecursionlimit(1000000)

N,M =  map(int,input.split())


graph = [list(input().rstrip()) for _ in range(N)]

visited = [[0 for _ in range(M)] for _ in range(N)]

cache = [[0 for _ in range(M) for _ in range(N)]]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

result = 0import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())

graph = [ list(input().rstrip()) for _ in range(N)]
visited = [[ 0 for _ in range(M)] for _ in range(N)]
cache = [[ 0 for _ in range(M)] for _ in range(N)]

result = 0

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def dfs(y, x, cnt):
  global result

  result = max(result, cnt)
  num = int(graph[y][x])

  for i in range(4):
    ny, nx = y+num*dy[i], x+num*dx[i]
    if 0 <= ny < N and 0 <= nx < M and graph[ny][nx] != "H" and cnt+1 > cache[ny][nx]:
      if visited[ny][nx]:
        print(-1)
        exit()
      
      cache[ny][nx] = cnt + 1
      visited[ny][nx] = 1
      dfs(ny, nx, cnt+1)
      visited[ny][nx] = 0

dfs(0, 0, 0)
print(result+1)
 Tags: dfs dynamic programming

 Categories: Problem Solving

 Updated: July 30, 2022



def dfs(y,x,cnt):
    global result

    result = max(result,cnt)
    num = int(graph[y][x])


    for i in range(4):
        ny,nx = y+num*dy[i] , x+ num*dx[i]
        if 0 <= ny <N and 0 <= nx< M and graph[ny][nx] !="H" and cnt+1> cache[ny][nx]:
            if visited[ny][nx]:
                print(-1)
                exit()
           
            cache[ny][nx] =cnt +1
            visited[ny][nx] =1
            dfs(ny,nx, cnt+1)
      
            visited[ny][nx] = 0 
dfs(0,0,0)
print(result+1)

























