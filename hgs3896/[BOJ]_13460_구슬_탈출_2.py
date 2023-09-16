# 2시간 19분
import sys
def read_board():
    N, M = map(int, sys.stdin.readline().split())
    board = [
        list(sys.stdin.readline().rstrip())
        for _ in range(N)
    ]
    red_pos = None
    blue_pos = None
    for r, row in enumerate(board):
        for c, v in enumerate(row):
            if v == 'R':
                red_pos = (r, c)
                board[r][c] = '.'
            if v == 'B':
                blue_pos = (r, c)
                board[r][c] = '.'
    return red_pos, blue_pos, board

def tilt(red, blue, dr, dc, board):
    is_moving = True
    while is_moving:
        is_moving = False
        if board[red[0]][red[1]] != 'O' and ((board[red[0]+dr][red[1]+dc] == '.' and (red[0]+dr, red[1]+dc) != blue) or board[red[0]+dr][red[1]+dc] == 'O'):
            red = (red[0]+dr, red[1]+dc)
            is_moving = True
        if board[blue[0]][blue[1]] != 'O' and ((board[blue[0]+dr][blue[1]+dc] == '.' and (blue[0]+dr, blue[1]+dc) != red) or board[blue[0]+dr][blue[1]+dc] == 'O'):
            blue = (blue[0]+dr, blue[1]+dc)
            is_moving = True
    return red, blue

def compress(red_pos, blue_pos):
    return red_pos[0] << 12 | red_pos[1] << 8 | blue_pos[0] << 4 | blue_pos[1]

def decompress(pos):
    return ((pos >> 12) & 0xf, (pos >> 8) & 0xf), ((pos >> 4) & 0xf, pos & 0xf)

red_pos, blue_pos, board = read_board()

def is_hole(pos):
    return board[pos[0]][pos[1]] == 'O'

DR = (0,1,0,-1)
DC = (1,0,-1,0)

dp = [None] * (1 << 16)
def dfs(compressed_pos, num_tries):
    if dp[compressed_pos] is not None and num_tries + dp[compressed_pos] <= 10:
        return dp[compressed_pos]
    
    if num_tries > 10:
        return 11
    
    red_pos, blue_pos = decompress(compressed_pos)
    result = 11
    if is_hole(blue_pos):
        # 실패
        pass
    elif is_hole(red_pos):
        # 성공
        result = 0
    else:
        # 다음 경우 살펴보기
        for dr, dc in zip(DR, DC):
            new_red_pos, new_blue_pos = tilt(red_pos, blue_pos, dr, dc, board)
            if red_pos == new_red_pos and blue_pos == new_blue_pos:
                continue

            result = min(result, dfs(compress(new_red_pos, new_blue_pos), num_tries+1) + 1)

    # 현재 상태에서 성공가능한 경우 최솟값 저장
    dp[compressed_pos] = result
    return dp[compressed_pos]

result = dfs(compress(red_pos, blue_pos), 0)
print(result if result != 11 else -1)