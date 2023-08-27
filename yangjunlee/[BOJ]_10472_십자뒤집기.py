boards = []

for i in range(2**9):
    board = [[0 for _ in range(3)] for _ in range(3)]
    for j in range(9):
        if i&(1<<j):
            board[j//3][j%3]=1
    boards.append(board)
 
def flip(board, x, y):
    dx, dy = [0,0,0,1,-1], [0,1,-1,0,0]
    board2 = [[board[i][j] for j in range(3)] for i in range(3)]
    for i in range(5):
        if 0<=x+dx[i]<3 and 0<=y+dy[i]<3:
            board2[x+dx[i]][y+dy[i]] = 1-board[x+dx[i]][y+dy[i]]
    return board2
 
graph = [[0 for _ in range(2**9)] for _ in range(2**9)]
 
for board in boards:
    for i in range(3):
        for j in range(3):
            graph[boards.index(board)][boards.index(flip(board, i, j))] = 1
       
N = int(input())

def bfs(start):
    visited = [0 for _ in range(2**9)]
    visited[start] = 1
    que=[start]
    while que:
        x = que.pop(0)
        count = visited[x]
        if x==0:
            return count-1
        for i in range(2**9):
            if graph[x][i]==1 and visited[i]==0:
                visited[i]=count+1
                que.append(i)
    

for i in range(N):
    board = []
    for j in range(3):
        s = list(input())
        board.append([1 if s[k]=='*' else 0 for k in range(3)])
    

    print(bfs(boards.index(board)))
