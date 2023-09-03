from typing import List, Tuple
import sys


def input() -> str:
    return sys.stdin.readline().rstrip()


def solution(arr: List[int]) -> Tuple[int, int]:
    N = len(arr)
    arr.sort()
    answer = (
        0,
        0,
    )
    INF = 2_000_000_000
    mn = INF
    L, R = 0, N - 1
    while L <= R:
        if mn > abs(arr[L] + arr[R]):
            mn = abs(arr[L] + arr[R])
            answer = (
                arr[L],
                arr[R],
            )
        l_mn = abs(arr[L + 1] + arr[R]) if L + 1 <= R else INF
        r_mn = abs(arr[L] + arr[R - 1]) if R - 1 >= 0 else INF
        if l_mn < r_mn:
            L += 1
        else:
            R -= 1
    return answer


if __name__ == "__main__":
    N = int(input())
    arr = list(map(int, input().split()))
    answer = solution(arr)
    print(*answer)
