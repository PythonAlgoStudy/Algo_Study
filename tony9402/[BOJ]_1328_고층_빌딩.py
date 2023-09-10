import sys
from collections import defaultdict


def input() -> str:
    return sys.stdin.readline().rstrip()


def solution(N: int, L: int, R: int) -> int:
    MOD = 1_000_000_007

    DP = defaultdict(int)
    DP[(1, 1, 1)] = 1
    for i in range(2, N + 1):
        for j in range(1, i + 1):
            for k in range(1, i + 1):
                value = (
                    DP[(i - 1, j - 1, k)]
                    + DP[(i - 1, j, k - 1)]
                    + DP[(i - 1, j, k)] * (i - 2)
                )
                DP[(i, j, k)] = value % MOD
    return DP[(N, L, R)]


if __name__ == "__main__":
    N, L, R = map(int, input().split())
    print(solution(N, L, R))
