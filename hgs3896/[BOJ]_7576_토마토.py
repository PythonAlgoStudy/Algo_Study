from collections import deque

# 입력
M, N = list(map(int, input().split()))
totamo = [input().split() for _ in range(N)]

# BFS로 토마토가 모두 익을 때까지 걸리는 시간을 구한다
def bfs(tomato):
    rotten = [[M*N+1] * M for _ in range(N)]

    q = deque()
    for r, row in enumerate(tomato):
        for c, col in enumerate(row):
            if col == '1':
                q.append((r, c, 0))
                rotten[r][c] = 0

    result = 0
    while q:
        r, c, date = q.popleft()
        # 토마토가 익을때까지 걸리는 시간의 최댓값 갱신
        result = max(result, date)

        for dr, dc in zip((-1, 0, 1, 0), (0, 1, 0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M and tomato[nr][nc] == '0' and rotten[nr][nc] > date + 1:
                tomato[nr][nc] = '1'
                rotten[nr][nc] = date + 1
                q.append((nr, nc, date + 1))

    # 하나라도 익지 않은 토마토 발견시 -1, 아니면 최댓값 반환
    return -1 if any(item == '0' for row in tomato for item in row) else result

print(bfs(totamo))