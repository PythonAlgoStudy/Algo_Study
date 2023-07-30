from collections import deque

#bfs 정의
def bfs(graph, start):
    queue = deque()
    for i in start:
        queue.append(i)
    while queue:
        current = queue.popleft()
        if(graph[current[0],current[1]] == 1):
            continue
        
        #방문처리
        graph[current[0],current[1]] = 1
        
#입력
m,n = map(int,input().split())
graph = []
start = []
for i in range(n):
    graph.append(list(map(int,input())))

#시작 지점(1) 전부 찾아서 start에 저장    
for j in range(m):
    for k in range(n):
        if(graph[m,n] == 1):
            start.append([m,n,0])

#bfs 알고리즘 호출            
answer = bfs(graph,[m,start])

#출력
print(answer)
