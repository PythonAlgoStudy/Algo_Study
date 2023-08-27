boards = []

# 모든 3*3 보드 생성
for i in range(2**9):
    board = [[0 for _ in range(3)] for _ in range(3)]
    for j in range(9):
        if i&(1<<j):
            board[j//3][j%3]=1
    boards.append(board)

# 십자뒤집기 함수
def flip(board, x, y):
    dx, dy = [0,0,0,1,-1], [0,1,-1,0,0]
    board2 = [[board[i][j] for j in range(3)] for i in range(3)]
    for i in range(5):
        if 0<=x+dx[i]<3 and 0<=y+dy[i]<3:
            board2[x+dx[i]][y+dy[i]] = 1-board[x+dx[i]][y+dy[i]]
    return board2
 
graph = [[0 for _ in range(2**9)] for _ in range(2**9)]

#십자뒤짐기로 연결되는 보드들 사이 인접 리스트 만들기
for board in boards:
    for i in range(3):
        for j in range(3):
            graph[boards.index(board)][boards.index(flip(board, i, j))] = 1
       
N = int(input())

#bfs
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
    
#입력 받은 보드에서 bfs로 0번 보드(... ... ...) 로 가는 최단거리 찾기
for i in range(N):
    board = []
    for j in range(3):
        s = list(input())
        board.append([1 if s[k]=='*' else 0 for k in range(3)])
    

    print(bfs(boards.index(board)))
