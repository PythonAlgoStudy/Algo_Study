# 풀이시간 30분
def read_board():
    import sys
    return [sys.stdin.readline().rstrip().split(' ') for _ in range(19)]

def determine_winner(board):
    DR = [-1, 0, 1, 1]
    DC = [1, 1, 1, 0]
    for r in range(19):
        for c in range(19):
            if board[r][c] != '0':
                curr_player = board[r][c]
                for dr, dc in zip(DR, DC):
                    l = 1
                    nr, nc = r - dr, c - dc
                    while 0 <= nr < 19 and 0 <= nc < 19 and board[nr][nc] == curr_player:
                        l += 1
                        nr, nc = nr - dr, nc - dc
                    
                    if l != 1:
                        continue

                    nr, nc = r + dr, c + dc
                    while 0 <= nr < 19 and 0 <= nc < 19 and board[nr][nc] == curr_player:
                        l += 1
                        nr, nc = nr + dr, nc + dc
                    
                    if l == 5:
                        return (curr_player, (r+1, c+1))

    return ('0', None)

winner, pos = determine_winner(read_board())
print(winner)
if winner != '0':
    print(*pos)