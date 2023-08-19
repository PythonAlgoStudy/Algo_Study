import sys
from heapq import heappop, heappush
from typing import List


def input() -> str:
    return sys.stdin.readline().rstrip()


def solution(N: int, K: int, arr: List[List[int]], bag: List[int]) -> int:
    arr.sort()
    arr_index = 0
    pq: List[int] = []

    answer = 0
    for weight in sorted(bag):
        while arr_index < N and arr[arr_index][0] <= weight:
            heappush(pq, -arr[arr_index][1])
            arr_index += 1

        if len(pq):
            answer -= heappop(pq)
    return answer


if __name__ == "__main__":
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for i in range(N)]
    bag = [int(input()) for i in range(K)]
    answer = solution(N, K, arr, bag)
    print(answer)
