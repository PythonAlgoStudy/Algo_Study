# DFS 
import sys
# 왜 100000인지는 알아봐야함
sys.setrecursionlimit(100000)
n = int(input())
graph = []
max_num = 0
result = 1

# 상하좌우
dx= [0,0,-1,1]
dy= [1,-1,0,0]

# 그래프에 입력 지대를 차례로 low 에 할당해서 넣기
for i in range(n):
    low = list(map(int, input().split()))
    graph.append(low)
    # j 는 최고 지대 찾음
    for j in low :
        if j >max_num:
            max_num = j
# dfs 함수 만들기 
def dfs(x,y,num):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
    # 범위내, 지나가지 않은곳 들를때마다
    if 0<=nx<n and 0<=ny<n and visited[nx][ny]==0:
        # graph 의 함수값이 num 보다 큰 숫자를 지날때마다 
        if graph[nx][ny] > num:
            # visited 값 증가
            visited[nx][ny] =1
            #재귀호출 
            dfs(nx,ny,num)
    
    # 고지대 기점으로 i 번 돈다! 
for i in range(max_num):
    visited = [[0]*n for _ in range(n)]
    cnt = 0
    
    for j in range(n):
        for k in range(n):
            if graph[j][k] >  i and visited[j][k] == 0:
                cnt +=1
                visited[j][k] =1
                dfs(j,k,i)
    result = max(result,cnt)

print(result)






