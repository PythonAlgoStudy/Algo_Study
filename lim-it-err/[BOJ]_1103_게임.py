dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
is_valid = lambda x, y: 0 <= x < N and 0 <= y < M and matrix[x][y] != "H" if True else False


def dfs(x, y):
    if not is_valid(x, y):
        return 0
    if visited[x][y]:
        return -1
    if dp[x][y] != -1:
        return dp[x][y]

    visited[x][y] = True
    dp[x][y] = 0
    for i in range(4):
        nx = x + dx[i] * int(matrix[x][y])
        ny = y + dy[i] * int(matrix[x][y])
        temp = dfs(nx, ny)
        if temp == -1:
            return -1
        dp[x][y] = max(dp[x][y], temp + 1)

    visited[x][y] = False
    return dp[x][y]

N, M = map(int, input().split())
matrix = [input() for _ in range(N)]
dp = [[-1]*M for _ in range(N)]
visited = [[False]*M for _ in range(N)]

result = dfs(0, 0)
if result == -1:
    print(-1)
else:
    print(result)
