import sys
from typing import List, Tuple

Dy: Tuple[int, ...] = (-1, 1, 0, 0)
Dx: Tuple[int, ...] = (0, 0, -1, 1)


def input() -> str:
    return sys.stdin.readline().rstrip()


def solution(N: int, M: int, arr: List[List[int]]) -> int:
    answer = [0]
    visited = set()

    def is_inrange(y, x) -> bool:
        return 0 <= y < N and 0 <= x < M

    def dfs(y: int, x: int, step: int, score: int) -> None:
        if step == 4:
            answer[0] = max(answer[0], score)
            return
        for dy, dx in zip(Dy, Dx):
            next_y, next_x = y + dy, x + dx
            if not is_inrange(next_y, next_x):
                continue
            pos = next_y * M + next_x
            if pos in visited:
                continue
            visited.add(next_y * M + next_x)
            if step == 2:
                dfs(y, x, step + 1, score + arr[next_y][next_x])
            dfs(next_y, next_x, step + 1, score + arr[next_y][next_x])
            visited.discard(next_y * M + next_x)

    for i in range(N):
        for j in range(M):
            visited.add(i * M + j)
            dfs(i, j, 1, arr[i][j])
            visited.discard(i * M + j)

    return answer[0]


if __name__ == "__main__":
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for i in range(N)]
    answer = solution(N, M, arr)
    print(answer)
