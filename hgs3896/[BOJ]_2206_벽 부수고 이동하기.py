from collections import deque

# 입력
n, m = map(int, input().split())
graph = [list(map(lambda x: int(x[0] == '1'), input())) for _ in range(n)]

dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))

# min_dist[r][c][can_break] = (0, 0)에서 (r, c)까지 can_break번 벽을 부술 수 있는 최단 거리
# 모든 지점을 중복없이 다 지난다고 해도 최대 n*m번이므로 n*m+1로 초기화
min_dist = [[[n*m+1, n*m+1] for _ in range(m)] for _ in range(n)]
# 초기 원점에서 벽을 부수지 않고 온 거리는 1
min_dist[0][0][1] = 1

q = deque([(0, 0, 1)])
while q:
    # r, c: 현재 위치
    # can_break: 남은 벽 부수기 횟수
    r, c, can_break = q.popleft()

    for dr, dc in dirs:
        nr, nc = r+dr, c+dc
        if not (0 <= nr < n and 0 <= nc < m):
            continue
        if graph[nr][nc] == 1 and can_break:
            if min_dist[nr][nc][can_break - 1] > min_dist[r][c][can_break] + 1:
                # 벽을 만났을 때 벽을 부술 수 있다면 부수고 갔을 때 최단 거리인 경우 진행
                q.append((nr, nc, can_break - 1))
                min_dist[nr][nc][can_break - 1] = min_dist[r][c][can_break] + 1
        elif graph[nr][nc] == 0:
            if min_dist[nr][nc][can_break] > min_dist[r][c][can_break] + 1:
                # 최단 거리인 경우 진행
                q.append((nr, nc, can_break))
                min_dist[nr][nc][can_break] = min_dist[r][c][can_break] + 1

# 최단거리가 n*m+1이면 도달할 수 없는 것이므로 -1 출력
if min(min_dist[n-1][m-1]) == n*m+1:
    print(-1)
else:
    print(min(min_dist[n-1][m-1]))