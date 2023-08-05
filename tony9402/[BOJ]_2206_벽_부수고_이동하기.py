import sys
from collections import deque
from typing import List, Tuple


def input() -> str:
    return sys.stdin.readline().rstrip()


Dy: Tuple[int, ...] = (-1, 1, 0, 0)
Dx: Tuple[int, ...] = (0, 0, -1, 1)


# state[2][N][M]
def solution(N: int, M: int, board: List[str]) -> int:
    state = [[[-1 for j in range(M)] for i in range(N)] for k in range(2)]
    Q: deque[Tuple[int, int, int]] = deque([(0, 0, 0)])
    state[0][0][0] = 1
    while Q:
        wall, y, x = Q.popleft()  # type(int, int, int)
        for dy, dx in zip(Dy, Dx):  # type: (int, int)
            next_y, next_x = y + dy, x + dx  # type: (int, int)
            if not (0 <= next_y < N and 0 <= next_x < M):
                continue

            # if (next_y, next_x) is wall
            if board[next_y][next_x] == "1" and wall == 0:
                state[1][next_y][next_x] = state[wall][y][x] + 1
                Q.append((1, next_y, next_x))

            # if (next_y, next_x) is not wall
            if board[next_y][next_x] == "0" and state[wall][next_y][next_x] == -1:
                state[wall][next_y][next_x] = state[wall][y][x] + 1
                Q.append((wall, next_y, next_x))

    answer = 10**8
    if state[0][N - 1][M - 1] != -1:
        answer = state[0][N - 1][M - 1]
    if state[1][N - 1][M - 1] != -1:
        answer = min(answer, state[1][N - 1][M - 1])
    if answer == 10**8:
        answer = -1
    return answer


if __name__ == "__main__":
    N, M = map(int, input().split())  # type: (int, int)
    board: List[str] = [input() for i in range(N)]
    answer = solution(N, M, board)
    print(answer)
