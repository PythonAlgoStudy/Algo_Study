import sys
from collections import deque
from typing import List


def input() -> str:
    return sys.stdin.readline().rstrip()


def update(arr: List[int], reverse=False) -> List[int]:
    ret: List[int] = []
    if reverse:
        arr.reverse()
    Q = deque([x for x in arr if x])
    while Q:
        if len(Q) > 1 and Q[0] == Q[1]:
            ret.append(Q.popleft() * 2)
            Q.popleft()
        else:
            ret.append(Q.popleft())
    ret.extend([0] * (len(arr) - len(ret)))
    if reverse:
        ret.reverse()
    return ret


def move(arr: List[List[int]], direction: int) -> List[List[int]]:
    N = len(arr)
    res = [[0 for j in range(N)] for i in range(N)]
    if direction < 2:
        for i in range(N):
            cur_value = [arr[i][j] for j in range(N)]
            nxt_value = update(cur_value, direction == 1)
            for idx, x in enumerate(nxt_value):
                res[i][idx] = x
    else:
        for j in range(N):
            cur_value = [arr[i][j] for i in range(N)]
            nxt_value = update(cur_value, direction == 3)
            for idx, x in enumerate(nxt_value):
                res[idx][j] = x
    return res


def get_max(arr: List[List[int]]) -> int:
    return max((max(x) for x in arr))


def dfs(arr: List[List[int]], move_cnt: int) -> int:
    return (
        get_max(arr)
        if move_cnt == 5
        else max((dfs(move(arr, k), move_cnt + 1) for k in range(4)))
    )


def solution(arr: List[List[int]]) -> int:
    return dfs(arr, 0)


if __name__ == "__main__":
    N = int(input())
    arr: List[List[int]] = [list(map(int, input().split())) for i in range(N)]
    print(solution(arr))
