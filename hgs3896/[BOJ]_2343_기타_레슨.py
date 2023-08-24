from typing import Tuple, List

def get_input() -> Tuple[int, List[int]]:
    import sys
    input = lambda: sys.stdin.readline().rstrip()
    _, M = map(int, input().split())
    lectures = list(map(int, input().split()))
    return lectures, M

def num_least_bluerays(lectures: List[int], blueray_size: int):
    s = 0
    cnt = 0
    for l in lectures:
        if s + l > blueray_size:
            cnt += 1
            s = 0
        s += l
    if s != 0:
        cnt += 1
    return cnt

def parametric_search(lectures: List[int], M: int) -> int:
    # 1 <= M <= len(lectures) <= 10**5
    # lectures[i] <= 10000
    
    # - Possible Answer Space
    # max(lectures) ~ sum(lectures) <= max(lectures) * len(lectures)
    l = max(lectures)
    r = l * len(lectures) + 1
    # [l, r)
    while l != r:
        m = l + (r - l) // 2
        if num_least_bluerays(lectures, m) <= M:
            r = m
        else:
            l = m + 1
    return r

print(parametric_search(*get_input()))