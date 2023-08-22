N = int(input())
balls = [(i, *map(int, input().split())) for i in range(N)]
balls.sort(key=lambda t: t[2])
result = [0] * N
color_sum = [0] * (N + 1)
total_sum = 0
cur_size = 0
for i in range(N):
    idx, color, size = balls[i]
    if size > cur_size:
        for j in range(i-1, -1, -1):
            if balls[j][2] != balls[i-1][2]:
                break
            # Size가 같을 때까지 누적합 계산
            color_sum[balls[j][1]] += balls[j][2]
            total_sum += balls[j][2]
        cur_size = size
    # total_sum에는 cur_size보다 작은 공 크기의 합이 누적
    # color_sum[color]에는 cur_size보다 작은 color 색상을 가진 공 크기의 합이 누적
    # 즉, cur_size보다 작고 색상이 color가 아닌 공 크기의 합을 아래 식으로 구할 수 있음
    result[idx] = total_sum - color_sum[color]
for r in result:
    print(r)