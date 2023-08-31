# 2615 오목 / 구현, 브루트포스
import sys
input = sys.stdin.readline

# 하, 오른쪽 대각, 우, 왼쪽 대각
dx = [0, 1, 1, -1]
dy = [1, 1, 0, 1]

def omok():
    for x in range(19):
        for y in range(19):
            if board[x][y] != 0:
                for i in range(4):
                    cnt = 1
                    nx, ny = x + dx[i], y + dy[i]
                    while 0 <= nx < 19 and 0 <= ny < 19 and board[nx][ny] == board[x][y]:
                        cnt += 1
                        nx += dx[i]
                        ny += dy[i]
                    
                    if cnt == 5:  # 오목이 검정 돌인 경우
                        if 0 <= nx < 19 and 0 <= ny < 19 and board[nx][ny] == board[x][y]:
                            continue
                        if 0 <= x - dx[i] < 19 and 0 <= y - dy[i] < 19 and board[x - dx[i]][y - dy[i]] == board[x][y]:
                            continue
                        return board[x][y], x + 1, y + 1
    return 0, 0, 0  # 오목이 발견되지 않은 경우

# 입력 코드
board = [list(map(int, input().split())) for i in range(19)]
answer, x, y = omok()

if answer == 0:
    print(0)
else:
    print(answer)
    print(x, y)
