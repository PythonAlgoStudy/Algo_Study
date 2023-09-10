from collections import deque
import copy

p = int(input())
answer = []
dx = [0,-1,1,0,0]
dy = [0,0,0,-1,1]


def convert_visit(board):
    str_visit = ''
    for i in range(3):
        for j in range(3):
            if board[i][j] == '.':
                str_visit+='0'
            else:
                str_visit+='1'
    return str_visit

def convert_board(board,x,y):
    convert_board = copy.deepcopy(board)
    
    for i in range(5):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<3 and 0<=ny<3:
            convert_board[nx][ny] = '.' if convert_board[nx][ny] == '*' else '*'
    return convert_board        
    
def bfs(board):
    q = deque()
    q.append(board)
    ans = 0
    while q:
        t = len(q)
        for _ in range(t):
            pop_board = q.popleft()
            if pop_board == compare:
                return ans
            
            for i in range(3):
                for j in range(3):
                    c_b = convert_board(pop_board,i,j)
                    if convert_visit(c_b) in visit:
                        continue
                    visit.append(convert_visit(c_b))
                    q.append(c_b)
        ans+=1


    
for _ in range(p):
    board = [list('...') for _ in range(3)]
    compare = [list(input()) for _ in range(3)]
    visit = []
    visit.append(convert_visit(board))
    answer.append(bfs(board))

for i in answer:
    print(i)