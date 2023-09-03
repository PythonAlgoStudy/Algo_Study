def BFS(v):
    visited=[0]*(N+1)
    visited[v]=1
    que=[[v,0]]
    CB=[0]*(N+1)
    while(que):
        q, cb=que.pop(0)
        for i in node[q]:
            if not visited[i]:
                visited[i]=1
                que.append([i, cb+1])
                CB[i]=cb+1
    return CB
N, M=map(int, input().split())


node=[[] for _ in range(N+1)]




for i in range(M):
    a, b=map(int, input().split())
    node[a].append(b)
    node[b].append(a)
for i in range(N+1):
    node[i].sort()
    

cbs=[]
for i in range(1, N+1):
    cbs.append(sum(BFS(i)))
print(cbs.index(min(cbs))+1)
