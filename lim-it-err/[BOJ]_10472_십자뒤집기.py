import sys

INF = 1e9
is_valid = lambda x, y: 0 <= x < 3 and 0 <= y < 3 if True else False
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
N = int(input())


def toggle(element):
    if element == "*":
        return "."
    return "*"


def input_to_number(data):
    ret_val = 0
    for i in range(9):
        x, y = i // 3, i % 3
        if data[x][y] == "*":
            ret_val += 2**i
    return ret_val


def bfs(source, target_code):
    queue = [(source, 0, 0)]
    visited = []
    while queue:
        current_source, clicks, prev_code = queue.pop(0)
        if prev_code in visited:
            continue
        if prev_code == target_code:
            return clicks
        visited.append(prev_code)
        for i in range(9):
            row, col = i // 3, i % 3
            _source = current_source.copy()

            _source[row] = (
                _source[row][:col]
                + toggle(_source[row][col])
                + _source[row][(col + 1) :]
            )

            for dx, dy in zip(dxs, dys):
                new_row, new_col = row + dx, col + dy
                if is_valid(new_row, new_col):
                    _source[new_row] = (
                        _source[new_row][:new_col]
                        + toggle(_source[new_row][new_col])
                        + _source[new_row][(new_col + 1) :]
                    )
            code = input_to_number(_source)
            queue.append((_source, clicks + 1, code))
    return INF


for testcase in range(N):
    source = ["...", "...", "..."]
    target = [input() for _ in range(3)]
    min_click = bfs(source, input_to_number(target))
    print(min_click)
