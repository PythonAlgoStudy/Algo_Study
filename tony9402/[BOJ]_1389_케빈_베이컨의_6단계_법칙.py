import sys
from typing import List, Tuple


def input() -> str:
    return sys.stdin.readline().rstrip()


# Using Floyd's algorithm
# Time Complexity: O(N^3)
def solution(N: int, M: int, edges: List[Tuple[int, int]]) -> int:
    INF = 0x3F3F3F3F
    D: List[List[int]] = [
        [INF if i != j else 0 for j in range(N + 1)] for i in range(N + 1)
    ]
    for u, v in edges:  # type: (int, int)
        D[u][v] = D[v][u] = 1
    for k in range(1, N + 1):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                D[i][j] = min(D[i][j], D[i][k] + D[k][j])

    min_value = INF
    answer = 0
    for i in range(1, N + 1):
        value = sum([x for x in D[i] if x != INF])
        if min_value > value:
            min_value = value
            answer = i
    return answer


if __name__ == "__main__":
    N, M = map(int, input().split())  # type: (int, int)
    edges = []
    for i in range(M):
        u, v = map(int, input().split())
        edges.append((u, v))
    answer = solution(N, M, edges)
    print(answer)
