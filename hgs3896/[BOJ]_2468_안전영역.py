from collections import deque

# 입력
N = int(input())
area = [list(map(int, input().split())) for _ in range(N)]

dr, dc = (0, 0, 1, -1), (1, -1, 0, 0)
heights = set(x for row in area for x in row)
min_h = min(heights)
if min_h > 0:
    heights.add(min_h - 1)

max_safe_area = 0
for h in heights:
    # h 높이 이하인 지역은 물에 잠겼을 때 잠기는 지역을 Floodfill by BFS로 세기
    visited = [[False] * N for _ in range(N)]
    safe_area = 0
    for i in range(N):
        for j in range(N):
            if area[i][j] > h and not visited[i][j]:
                safe_area += 1
                q = deque([(i, j)])
                visited[i][j] = True
                while q:
                    r, c = q.popleft()
                    for dr_, dc_ in zip(dr, dc):
                        nr, nc = r + dr_, c + dc_
                        # 범위를 벗어나거나 이미 방문했거나 물에 잠겼으면 넘어감
                        if not (0 <= nr < N and 0 <= nc < N):
                            continue
                        if visited[nr][nc]:
                            continue
                        if not area[nr][nc] > h:
                            continue
                        q.append((nr, nc))
                        visited[nr][nc] = True
    max_safe_area = max(max_safe_area, safe_area)

print(max_safe_area)