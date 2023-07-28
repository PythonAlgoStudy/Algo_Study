import sys
from collections import deque
from typing import List, Tuple


def input() -> str:
    return sys.stdin.readline().rstrip()


Dy: Tuple[int, ...] = (-1, 1, 0, 0)
Dx: Tuple[int, ...] = (0, 0, -1, 1)

R, C, N = map(int, input().split())  # type: (int, int, int)
bomb: List[List[int]] = [
    list(map(lambda x: 3 if x == "O" else 0, input())) for i in range(R)
]


def put_bomb(cur_time) -> None:
    for i in range(R):
        for j in range(C):
            if bomb[i][j] == 0:
                bomb[i][j] = cur_time + 3


def blow_up(cur_time) -> None:
    for i in range(R):
        for j in range(C):
            if bomb[i][j] != cur_time:
                continue
            bomb[i][j] = 0
            for dy, dx in zip(Dy, Dx):
                nexty, nextx = i + dy, j + dx  # type: (int, int)
                if not (0 <= nexty < R and 0 <= nextx < C):
                    continue
                if bomb[nexty][nextx] != cur_time:
                    bomb[nexty][nextx] = 0


def print_bomb():
    for i in range(R):
        result: List[str] = ["O" if bomb[i][j] != 0 else "." for j in range(C)]
        print("".join(result))


for i in range(1, N + 1):
    if i % 2 == 0:
        put_bomb(i)
    else:
        blow_up(i)

print_bomb()
