n,m = map(int,input().split())


INF = 987654321

graph = [[INF]*(n) for _ in range(n)]

for a in range(n):
  for b in range( n):
    if a == b:
        graph[a][b] = 0

for _ in range(m):
    a,b = map(int, input().split())
    graph[a-1][b-1] = 1
    graph[b-1][a-1] = 1

for k in range( n):
  for a in range( n):
    for b in range( n):
        graph[a][b] = min(graph[a][b],graph[a][k]+graph[k][b])
        graph[b][a] = min(graph[a][b],graph[a][k]+graph[k][b])


answer = []
for a in range(n):
    answer.append(sum(graph[a]))

minNode = 0
for i in range(len(answer)-1):
  if(answer[i]>answer[i+1]):
    minNode = i+1
    
    

print(minNode+1)
