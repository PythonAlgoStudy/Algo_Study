# boj 16918.봄버맨
import sys
from collections import deque
input = sys.stdin.readline

# 입력받기: r*c 격자판, n초
r, c, n = list(map(int, input().strip().split()))
board = [list(map(lambda x: 3 if x == 'O' else 0, input())) for _ in range(r)]

def in_range(x, y):
    return 0 <= x < r and 0 <= y < c

def countdown():
    for i in range(r):
        for j in range(c):
            if board[i][j] != 0:
                board[i][j] -= 1

def bomb():
    dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]
    bombs = []
    for x in range(r):
        for y in range(c):
            if board[x][y] == 0:
                bombs.append((x, y))

    for x, y in bombs:
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny):
                board[nx][ny] = 0

def plant():
    for i in range(r):
        for j in range(c):
            if board[i][j] == 0:
                board[i][j] = 3

# 1. 초기 폭탄을 설치한다.
# 2. 1초 동안 아무것도 하지 않는다.
countdown()
for i in range(2, n + 1):
    # 3. 폭탄이 없는 곳에 폭탄을 설치한다.
    if i % 2 == 0:
        plant()
        if i != n:
            countdown()
    else:
        # 4. 3초전에 설치한 폭탄이 폭발한다.
        countdown()
        bomb()

for i in range(r):
    for j in range(c):
        print("O" if board[i][j] != 0 else ".", end = '')
    print()

# ------
# # boj 16918.봄버맨
# import sys
# from collections import deque
# input = sys.stdin.readline

# # 입력받기: r*c 격자판, n초
# r, c, n = list(map(int, input().strip().split()))
# board = [list(input().strip()) for _ in range(r)]
# arr = [[0 for _ in range(c)] for _ in range(r)]

# def in_range(x, y):
#     return 0 <= x < r and 0 <= y < c

# def set_timer():
#     for i in range(r):
#         for j in range(c):
#             if board[i][j] == 'O' and arr[i][j] == 0:
#                 arr[i][j] == 3

# def countdown():
#     for i in range(r):
#         for j in range(c):
#             if board[i][j] == 'O' and arr[i][j] != 0:
#                 arr[i][j] -= 1

# def bomb():
#     dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]
#     for x in range(r):
#         for y in range(c):
#             if board[x][y] == 'O' and arr[x][y] == 0:
#                 board[x][y] = '.'
#                 for dx, dy in zip(dxs, dys):
#                     nx, ny = x + dx, y + dy
#                     if in_range(nx, ny) and board[nx][ny] == 'O' and arr[nx][ny] != 0:
#                         board[nx][ny] = '.'

# def plant():
#     for i in range(r):
#         for j in range(c):
#             if board[i][j] != "O":
#                 board[i][j] = "O"
#                 arr[i][j] = 3

# cnt = 0
# # 1. 초기 폭탄을 설치한다.
# set_timer()
# # 2. 1초 동안 아무것도 하지 않는다.
# countdown()
# cnt += 1
# while cnt < n:
#     # 3. 폭탄이 없는 곳에 폭탄을 설치한다.
#     plant()
#     cnt += 1
#     countdown()
#     if cnt < n:
#         # 4. 3초전에 설치한 폭탄이 폭발한다.
#         countdown()
#         cnt += 1
#         bomb()
#     else:
#         break

# for i in range(r):
#     for j in range(c):
#         print(board[i][j], end = '')
#     print()

