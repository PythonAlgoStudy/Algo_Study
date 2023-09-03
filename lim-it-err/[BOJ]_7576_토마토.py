from collections import deque

is_valid = lambda x, y, sizex, sizey: 0 <= x < sizex and 0 <= y < sizey if True else False


class B7576(object):
    def __init__(self):
        self.N, self.M = list(map(int, input().split(' ')))
        self.visited = [[False for _ in range(self.N)] for _ in range(self.M)]
        self.discovered = [[False for _ in range(self.N)] for _ in range(self.M)]
        self.inputdata = self._get_input()
        self.dx, self.dy = [1, -1, 0, 0], [0, 0, 1, -1]  # EWSN

    def sol_bfs(self):
        q = deque([(i, j) for i in range(self.M) for j in range(self.N) if self.inputdata[i][j] == 1])
        q_iter = len(q)
        iteration = -1
        while q and q_iter:
            if q:
                x, y = q.popleft()
                if self.visited[x][y]:
                    continue
                self.visited[x][y] = True
                self.inputdata[x][y] = 1
                for i in range(4):
                    nx, ny = x + self.dx[i], y + self.dy[i]
                    if not is_valid(nx, ny, self.M, self.N):
                        continue
                    if self.inputdata[nx][ny] == 0 and not self.discovered[nx][ny]:
                        q.append((nx, ny))
                        self.discovered[nx][ny] = True

            q_iter -= 1
            if q_iter == 0:
                q_iter = len(q)
                iteration += 1
        if any((i, j) for i in range(self.M) for j in range(self.N) if self.inputdata[i][j] == 0):
            print(-1)
            return

    def _get_input(self):
        input_data = []
        for i in range(self.M):
            _line = list(map(int, input().split(' ')))
            input_data.append(_line)
        return input_data


if __name__ == "__main__":
    b7576 = B7576()
    b7576.sol_bfs()
