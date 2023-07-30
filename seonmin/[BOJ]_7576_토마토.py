from collections import deque

#bfs 정의
def bfs(graph, start):
    queue = deque()
    for i in start:
        queue.append(i)
    while queue:
        current = queue.popleft()

        #방문처리
        graph[current[0]][current[1]] = 1

        #그래프 한계치 안 넘고, 방문 안 한 곳이면 큐에 넣기
        #상
        if(0<=current[0]-1 and graph[current[0]-1][current[1]]==0):
            queue.append([current[0]-1,current[1],current[2]+1])
        #하
        if(current[0]+1<len(graph) and graph[current[0]+1][current[1]]==0):
            queue.append([current[0]+1,current[1],current[2]+1])
        #좌
        if(0<=current[1]-1 and graph[current[0]][current[1]-1]==0):
            queue.append([current[0],current[1]-1,current[2]+1])
        #우
        if(current[1]+1<len(graph[0]) and graph[current[0]][current[1]+1]==0):
            queue.append([current[0],current[1]+1,current[2]+1])
        
    return current[2]

#입력
m,n = map(int,input().split())
graph = []
start = []
for i in range(n):
    graph.append(list(map(int,input().split())))

#시작 지점(1) 전부 찾아서 start에 저장    
for j in range(m):
    for k in range(n):
        if graph[k][j] == 1:
            start.append([k,j,0])

#bfs 알고리즘 호출            
answer = bfs(graph,start)

#다 익었는지 확인    
for j in range(m):
    for k in range(n):
        if graph[k][j] == 0:
            answer = -1

#출력
print(answer)
