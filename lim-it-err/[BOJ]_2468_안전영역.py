from collections import deque

N = int(input())
is_valid = lambda x, y: 0 <= x < N and 0 <= y < N if True else False

dxs, dys = [-1, 1, 0, 0], [0, 0, 1, -1]  # N, S, E, W
area = [list(map(int, input().split())) for _ in range(N)]

def remained_area(height: int):
    area_cnt = 0
    visited = [[False for _ in range(N)] for _ in range(N)]

    def bfs(starting, height: int):
        if area[starting[0]][starting[1]] <= height or visited[starting[0]][starting[1]]:
            return 0
        q = deque([starting])

        while q:
            x, y = q.pop()
            if visited[x][y]:
                continue
            visited[x][y] = True
            for dx, dy in zip(dxs, dys):
                if is_valid(x+dx, y+dy):
                    if area[x + dx][y + dy] > height and not visited[x + dx][y + dy]:
                        q.append((x + dx, y + dy))
        return 1

    for i in range(N):
        for j in range(N):
            area_cnt += bfs((i, j), height)
    return area_cnt


if __name__ == "__main__":
    max_count = 0
    for height in range(100):  # TODO : optimize
        max_count = max(max_count, remained_area(height))
    print(max_count)
