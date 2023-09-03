import sys
from collections import deque
from typing import List, Tuple


def input() -> str:
    return sys.stdin.readline().rstrip()


Dy: Tuple[int, ...] = (-1, 1, 0, 0)
Dx: Tuple[int, ...] = (0, 0, -1, 1)


def BFS(arr: List[List[int]], h: int) -> int:
    N, M = len(arr), len(arr[0])  # type: (int, int)
    count_of_safe_area = 0
    used: List[List[int]] = [[0 for j in range(M)] for i in range(N)]
    for i in range(N):
        for j in range(M):
            if arr[i][j] <= h or used[i][j]:
                continue
            Q: deque[Tuple[int, int]] = deque([(i, j)])
            count_of_safe_area += 1
            while Q:
                y, x = Q.popleft()  # type: (int, int)
                for dy, dx in zip(Dy, Dx):
                    next_y, next_x = y + dy, x + dx  # type: (int, int)
                    if not (0 <= next_y < N and 0 <= next_x < M):
                        continue
                    if used[next_y][next_x] == 1 or arr[next_y][next_x] <= h:
                        continue
                    Q.append((next_y, next_x))
                    used[next_y][next_x] = 1
    return count_of_safe_area


def solution(N: int, arr: List[List[int]]) -> int:
    answer = 0
    for h in range(0, 101):
        answer = max(answer, BFS(arr, h))
    return answer


if __name__ == "__main__":
    N: int = int(input())
    arr: List[List[int]] = [list(map(int, input().split())) for i in range(N)]
    print(solution(N, arr))
