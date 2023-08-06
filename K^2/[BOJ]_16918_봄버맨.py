import sys
input = sys.stdin.readline
from collections import deque



dx = [-1,0,1,0]
dy = [0,1,0,-1]

q= deque()


R,C,N = map(int,input().rstrip().split())


board  = []

for _ in range(R):
    board.append(list(input().rstrip()))


def bfs(q,board):
    while q:
        x,y = q.popleft()
        board[x][y] = '.'
      
        for i in range(4): 
            nx,ny = x+dx[i],y+dy[i]

            if nx>= 0 and nx<R and ny>=0 and ny<C and board[nx][ny] == '0':
                board[nx][ny] = '.' 


def simulate(t):
    global q, board
    if t == 1:

        for i in range(R):
            for j in range(C):
                if board[i][j] == '0':
                    q.append((i,j))                
    elif t%2 == 1:
  
        bfs(q,board)
   
        for i in range(R):
            for j in range(C):
                if board[i][j] == '0':
                    q.append((i,j))
    else:
   
        board= [['0']*C for _ in range(R)]
 

for i in range(1,N+1):
    simulate(i)

for i in board:
    print(''.join(i))