r,c,n = map(int,input().split())
graph = []
second = []
for i in range(r):
    graph.append(input())
    temp = []
    for j in range(c):
        temp.append('.')
    second.append(temp)

for k in range(n+1):
  if(k == 0):
    for i in range(r):
        for j in range(c):
            if(graph[i][j] == 'O'):
                second[i][j] = '2'
    graph = second

  elif(k%2 ==1) :
    bomb = []
    for i in range(r):
        for j in range(c):
            if(graph[i][j] == 'O'):
                bomb.append((i,j))
            if(graph[i][j] == '1'):
                second[i][j] = 'O'
            if(graph[i][j] == '2'):
                second[i][j] = '1'
    for m,n in bomb:
        second[m][n] = '.'
        if(0<=m-1):
            second[m-1][n] = '.'
        if(m+1<r):
            second[m+1][n] = '.'
        if(0<=n-1):
            second[m][n-1] = '.'
        if(n+1<c):
            second[m][n+1] = '.'
    graph = second
  elif(k%2 == 0):
    for i in range(r):
        for j in range(c):
            if(graph[i][j] == '1'):
                second[i][j] = 'O'
            if(graph[i][j] == '2'):
                second[i][j] = '1'
            if(graph[i][j] == '.'):
                second[i][j] = '2'

    graph = second
    
for i in range(r):
  for j in range(c):
      if(graph[i][j] == '1') or (graph[i][j] == '2')or (graph[i][j] == 'O'):
        graph[i][j] = 'O'


for i in range(r):
    print(''.join(graph[i]))
