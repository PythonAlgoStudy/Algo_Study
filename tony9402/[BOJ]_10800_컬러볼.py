import sys
from collections import defaultdict, deque
from typing import Deque, Dict, List, Tuple


def input() -> str:
    return sys.stdin.readline().rstrip()


def solution(arr: List[List[int]]) -> List[int]:
    N = len(arr)
    color_balls = sorted([(y, x, idx) for idx, (x, y) in enumerate(arr)])
    answer: List[int] = [0] * N
    G: Dict[int, int] = defaultdict(int)
    Queue: Deque[Tuple[int, int]] = deque()
    sum_of_ball_sizes = 0

    pre_size = -1
    for ball_size, ball_color, ball_idx in color_balls:
        if pre_size != ball_size:
            while Queue:
                cur_ball_size, cur_ball_color = Queue.popleft()
                sum_of_ball_sizes += cur_ball_size
                G[cur_ball_color] += cur_ball_size
        answer[ball_idx] = sum_of_ball_sizes - G[ball_color]
        Queue.append((ball_size, ball_color))
        pre_size = ball_size
    return answer


if __name__ == "__main__":
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(N)]
    answer: List[int] = solution(arr)
    print("\n".join(map(str, answer)))
