import sys
from typing import List, Tuple, Dict
from collections import deque, defaultdict


def input() -> str:
    return sys.stdin.readline().rstrip()


Dy: Tuple[int, ...] = (-1, 1, 0, 0)
Dx: Tuple[int, ...] = (0, 0, -1, 1)


def is_inrange(y: int, x: int) -> bool:
    return 0 <= y < 3 and 0 <= x < 3


def next_board(arr: str, y: int, x: int):
    nxt_arr: str = ""
    pos: Dict[Tuple[int, int], bool] = {}
    pos[(y, x)] = True
    for dy, dx in zip(Dy, Dx):
        next_y, next_x = y + dy, x + dx
        if not is_inrange(next_y, next_x):
            continue
        pos[(next_y, next_x)] = True

    for i in range(3):
        for j in range(3):
            if (i, j) not in pos:
                nxt_arr = f"{nxt_arr}{arr[i * 3 + j]}"
            else:
                nxt_arr = f"{nxt_arr}{'*' if arr[i * 3 + j] == '.' else '.'}"

    return nxt_arr


def solution(arr: List[str]):
    Queue = deque(["".join(arr)])
    visited: Dict[str, int] = defaultdict(int)
    while Queue:
        cur_board = Queue.popleft()
        for i in range(3):
            for j in range(3):
                nxt_board = next_board(cur_board, i, j)
                if nxt_board in visited:
                    continue
                visited[nxt_board] = visited[cur_board] + 1
                Queue.append(nxt_board)

    return visited["........."]


if __name__ == "__main__":
    T = int(input())
    for tc in range(T):
        arr: List[str] = [input() for i in range(3)]
        print(solution(arr))
