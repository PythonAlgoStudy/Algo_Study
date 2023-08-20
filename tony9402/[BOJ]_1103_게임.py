import sys
from typing import List, Tuple

# sys.setrecursionlimit(10**8) when submit as "python3"


def input() -> str:
    return sys.stdin.readline().rstrip()


Dy: Tuple[int, ...] = (-1, 1, 0, 0)
Dx: Tuple[int, ...] = (0, 0, -1, 1)


def solution(N: int, M: int, board: List[str]) -> int:
    DP: List[List[int]] = [[-1 for j in range(M)] for i in range(N)]
    visited: List[List[int]] = [[0 for j in range(M)] for i in range(N)]

    def dfs(y: int, x: int) -> Tuple[bool, int]:
        if not (0 <= y < N and 0 <= x < M) or board[y][x] == "H":
            return False, 0

        if visited[y][x]:
            return True, -1

        if DP[y][x] != -1:
            return False, DP[y][x]

        visited[y][x] = 1
        w: int = int(board[y][x])
        for dy, dx in zip(Dy, Dx):  # type: (int, int)
            next_y, next_x = y + dy * w, x + dx * w  # type(int, int)
            stop, ret = dfs(next_y, next_x)
            if stop:
                return stop, ret
            DP[y][x] = max(DP[y][x], ret + 1)
        visited[y][x] = 0
        return False, DP[y][x]

    _, answer = dfs(0, 0)
    return answer


if __name__ == "__main__":
    N, M = map(int, input().split())  # type: (int, int)
    board: List[str] = [input() for i in range(N)]
    answer: int = solution(N, M, board)
    print(answer)
