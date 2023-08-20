R,C,N = map(int,input().split())
bomb = [[0]*C for _ in range(R)]

       
dx = [-1,1,0,0]
dy = [0,0,-1,1]

        
#1단계
t = 0
graph = [list(input()) for _ in range(R)]
for i in range(R):
    for j in range(C):
        if graph[i][j] == 'O':
            bomb[i][j] = 3

#2단계
t += 1
for i in range(R):
    for j in range(C):
        bomb[i][j] -= 1

#3단계
def full_bomb():
    for i in range(R):
        for j in range(C):
            if graph[i][j] != 'O':
                graph[i][j] = 'O'
                bomb[i][j] = 3
            else:
                bomb[i][j]-=1

#4단계
def explode():
    for i in range(R):
        for j in range(C):
            bomb[i][j] -= 1
            if bomb[i][j] == 0:
                graph[i][j] = '.'
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if nx>=0 and nx<R and ny>=0 and ny<C:
                        graph[nx][ny] = '.'

while t<N:
    t+=1
    full_bomb()
    if t ==  N:
        break    
    t+=1
    explode()

for i in range(R):
    print(''.join(graph[i]))