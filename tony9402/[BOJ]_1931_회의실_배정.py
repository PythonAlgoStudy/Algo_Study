import sys
from typing import List


def input() -> str:
    return sys.stdin.readline().rstrip()


def solution(N: int, timetable: List[List[int]]) -> int:
    timetable.sort(key=lambda x: (x[1], x[0]))
    pre = -1
    answer = 0
    for start_time, end_time in timetable:
        if pre <= start_time:
            pre = end_time
            answer += 1
    return answer


if __name__ == "__main__":
    N = int(input())
    timetable = [list(map(int, input().split())) for i in range(N)]
    answer = solution(N, timetable)
    print(answer)
