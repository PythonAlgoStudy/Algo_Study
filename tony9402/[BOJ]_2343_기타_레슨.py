import sys
from typing import List


def input() -> str:
    return sys.stdin.readline().rstrip()


def solution(N: int, K: int, arr: List[int]) -> int:
    lo, hi = max(arr), 1_000_000_000
    while lo <= hi:
        mid = (lo + hi) // 2
        cnt, cur_sum = 0, 0
        for x in arr:
            if cur_sum + x > mid:
                cur_sum = 0
                cnt += 1
            cur_sum += x
        if cur_sum != 0:
            cnt += 1

        if cnt <= K:
            hi = mid - 1
        else:
            lo = mid + 1

    return lo


if __name__ == "__main__":
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    answer: int = solution(N, K, arr)
    print(answer)
