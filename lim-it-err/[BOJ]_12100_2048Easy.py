N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
dir_mapping = {0: [0, 1], 1: [1, 0], 2: [0, -1], 3: [-1, 0]}
is_valid = lambda x, y: 0 <= x < N and 0 <= y < N if True else False
MAX_VALUE = -1


def action(_board, block_pos: tuple, block_dir: int):
    x, y = block_pos
    dx, dy = dir_mapping[block_dir]
    value = _board[x][y]
    while is_valid(x + dx, y + dy):
        if _board[x + dx][y + dy] == 0:
            x += dx
            y += dy
            continue
        elif _board[x + dx][y + dy] != value:
            return False, _board
        elif _board[x + dx][y + dy] == value:
            import copy

            __board = copy.deepcopy(_board)
            __board[block_pos[0]][block_pos[1]] = 0
            __board[x + dx][y + dy] = 2 * value
            return True, __board
        else:
            print("UnexpectedError")
            raise AssertionError()
    return False, _board


q = [board]  # position(x, y)
q2 = []
visited = []
step = 5
while step:
    while q:
        board = q.pop()
        if board in visited:
            continue
        visited.append(board)
        for i in range(N):
            for j in range(N):
                if board[i][j] != 0:
                    for dir in range(4):
                        ret, _board = action(board, (i, j), dir)
                        if not ret:
                            continue
                        q2.append(_board)
                        print(_board)
                        MAX_VALUE = max([max(_board[i]) for i in range(N)])
    step -= 1
    q = q2.copy()
    q2 = []
print(MAX_VALUE)
