import sys
from collections import defaultdict, deque
from typing import List, Tuple


def input() -> str:
    return sys.stdin.readline().rstrip()


Dy: Tuple[int, ...] = (-1, 0, 1, 0)
Dx: Tuple[int, ...] = (0, -1, 0, 1)


def nxt_pos(cur_pos: Tuple[int, int], direction: int) -> Tuple[int, int]:
    return (cur_pos[0] + Dy[direction], cur_pos[1] + Dx[direction])


def move_ball(
    arr: List[str],
    red_pos: Tuple[int, int],
    blue_pos: Tuple[int, int],
    direction: int,
) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    red_move_cnt, blue_move_cnt = 0, 0
    while True:
        if arr[red_pos[0]][red_pos[1]] == "O":
            break

        red_nxt_pos = nxt_pos(red_pos, direction)
        if arr[red_nxt_pos[0]][red_nxt_pos[1]] == "#":
            break
        red_pos = red_nxt_pos
        red_move_cnt += 1

    while True:
        if arr[blue_pos[0]][blue_pos[1]] == "O":
            break

        blue_nxt_pos = nxt_pos(blue_pos, direction)
        if arr[blue_nxt_pos[0]][blue_nxt_pos[1]] == "#":
            break
        blue_pos = blue_nxt_pos
        blue_move_cnt += 1

    if red_pos[0] == blue_pos[0] and red_pos[1] == blue_pos[1]:
        if arr[red_pos[0]][red_pos[1]] != "O":
            if red_move_cnt > blue_move_cnt:
                red_pos = nxt_pos(red_pos, (direction + 2) % 4)
            else:
                blue_pos = nxt_pos(blue_pos, (direction + 2) % 4)
    else:
        if arr[red_pos[0]][red_pos[1]] == "O":
            print(1)
            exit(0)

    return red_pos, blue_pos


def solution(N: int, M: int, arr: List[str]) -> int:
    red_pos = (0, 0)
    blue_pos = (0, 0)
    for i in range(N):
        for j in range(M):
            if arr[i][j] == "R":
                red_pos = (i, j)
            elif arr[i][j] == "B":
                blue_pos = (i, j)

    visited = defaultdict(int)
    Queue = deque([(red_pos, blue_pos)])
    visited[(red_pos, blue_pos)] = 0
    step = 0

    while Queue:
        step += 1
        if step > 10:
            break

        current_queue_size = len(Queue)
        for _ in range(current_queue_size):
            cur_red_pos, cur_blue_pos = Queue.popleft()
            for k in range(4):
                nxt_red_pos, nxt_blue_pos = move_ball(arr, cur_red_pos, cur_blue_pos, k)
                if (nxt_red_pos, nxt_blue_pos) in visited:
                    continue
                visited[(nxt_red_pos, nxt_blue_pos)] = 1
                Queue.append((nxt_red_pos, nxt_blue_pos))
    return 0


if __name__ == "__main__":
    N, M = map(int, input().split())
    arr: List[str] = [input() for i in range(N)]
    answer: int = solution(N, M, arr)
    print(answer)
