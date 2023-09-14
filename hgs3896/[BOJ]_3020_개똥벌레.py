# 맞딱뜨리는 장애물 갯수: (아랫거 > k) + (위에꺼 >= H-k)
# 풀이시간: 18분
def read_input():
    import sys
    N, H = map(int, sys.stdin.readline().rstrip().split())
    obstacles = [int(sys.stdin.readline()) for _ in range(N)]
    return N, H, obstacles

def solve(N, H, obstacles):
    lower = [0] * H
    upper = [0] * H
    for h in obstacles[::2]:
        lower[h] += 1
    for h in obstacles[1::2]:
        upper[h] += 1
    for i in range(1, H):
        lower[i] += lower[i-1]
        upper[i] += upper[i-1]
    min_num_num_obstacles = N + 1
    cnt = 0
    for k in range(H):
        num_obstacles = lower[-1] - lower[k] + upper[-1] - upper[H-k-1]
        if num_obstacles < min_num_num_obstacles:
            min_num_num_obstacles = num_obstacles
            cnt = 1
        elif num_obstacles == min_num_num_obstacles:
            cnt += 1
    return min_num_num_obstacles, cnt

print(*solve(*read_input()))