import sys
from typing import List, Tuple


def input() -> str:
    return sys.stdin.readline().rstrip()


Dy: Tuple[int, ...] = (-1, 0, 1, 0)
Dx: Tuple[int, ...] = (0, 1, 0, -1)


def solution(Map: List[List[int]], r: int, c: int, d: int):
    step = 0
    while True:
        if Map[r][c] == 0:
            step += 1
            Map[r][c] = 2

        idx = 1
        while idx <= 4:
            nxt_d = (d - idx + 4) % 4
            nxt_y, nxt_x = r + Dy[nxt_d], c + Dx[nxt_d]
            if Map[nxt_y][nxt_x] == 0:
                break
            idx += 1

        if idx > 4:
            pre_d = (d + 2) % 4
            pre_y, pre_x = r + Dy[pre_d], c + Dx[pre_d]
            if Map[pre_y][pre_x] == 1:
                break
            r, c = pre_y, pre_x
        else:
            d = (d - idx + 4) % 4
            nxt_y, nxt_x = r + Dy[d], c + Dx[d]
            if Map[nxt_y][nxt_x] == 0:
                r, c = nxt_y, nxt_x

    return step


if __name__ == "__main__":
    N, M = map(int, input().split())
    r, c, d = map(int, input().split())
    Map: List[List[int]] = [list(map(int, input().split())) for i in range(N)]
    print(solution(Map, r, c, d))
