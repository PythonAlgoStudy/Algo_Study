N, M = map(int, input().split())
r, c, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
DR = (-1, 0, 1, 0)
DC = (0, 1, 0, -1)
cnt = 0
while True:
    if board[r][c] == 0:
        board[r][c] = 2
        cnt += 1
    
    if not any(board[r+dr][c+dc] == 0 for dr, dc in zip(DR, DC)):
        if board[r-DR[d]][c-DC[d]] != 1:
            r = r-DR[d]
            c = c-DC[d]
        else:
            break
    else:
        d = (d + 3) % 4
        if board[r+DR[d]][c+DC[d]] == 0:
            r = r+DR[d]
            c = c+DC[d]

print(cnt)