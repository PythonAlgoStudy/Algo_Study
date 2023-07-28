import sys
from collections import deque
from typing import List, Tuple


def input() -> str:
    return sys.stdin.readline().rstrip()


Dy: Tuple[int, ...] = (-1, 1, 0, 0)
Dx: Tuple[int, ...] = (0, 0, -1, 1)

M, N = map(int, input().split())  # type: (int, int)
box: List[List[int]] = [list(map(int, input().split())) for i in range(N)]


def get_position_of_tomato() -> List[Tuple[int, int]]:
    return [(y, x) for y in range(N) for x in range(M) if box[y][x] == 1]


def check_all_tomato_riped() -> bool:
    return len([1 for y in range(N) for x in range(M) if box[y][x] == 0]) == 0


Q = deque(get_position_of_tomato())

step: int = -1
while Q:
    qsize: int = len(Q)
    step += 1
    for _ in range(qsize):
        y, x = Q.popleft()  # type: (int, int)
        for dy, dx in zip(Dy, Dx):  # type: (int, int)
            nexty, nextx = y + dy, x + dx  # type: (int, int)
            if not (0 <= nexty < N and 0 <= nextx < M):
                continue
            if box[nexty][nextx] != 0:
                continue
            box[nexty][nextx] = 1
            Q.append((nexty, nextx))

print(step if check_all_tomato_riped() else -1)
