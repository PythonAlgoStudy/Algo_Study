field = [list(map(int, input().split())) for _ in range(19)]
dxs, dys = [1, 1, 0, 0], [0, 1, 1, -1]
is_valid = lambda x, y: 0 <= x < 19 and 0 <= y < 19
LENGTH = 5


def is_win(position, element) -> bool:
    for dx, dy in zip(dxs, dys):
        if _in_row(position, (dx, dy), element):
            return True
    return False


def _in_row(position, direction, element):
    x, y = position
    dx, dy = direction
    for i in range(LENGTH):
        # print(f"checked {x+dx*i}, {y+dy*i}, {field[x + dx * i][y + dy * i]}")
        if not is_valid(x + dx * i, y + dy * i):
            return False
        if not field[x + dx * i][y + dy * i] == element:
            return False
    if is_valid(x + dx * 5, y + dy * 5) and field[x + dx * 5][y + dy * 5] == element:
        return False
    if is_valid(x - dx, y - dy) and field[x - dx * 1][y - dy * 1] == element:
        return False
    return True


answer = []
for i in range(19):
    for j in range(19):
        if field[i][j] != 0:
            if is_win((i, j), field[i][j]):
                answer.append((i, j, field[i][j]))
answer.sort(key=lambda x: (x[1], x[0]))
if answer:
    print(answer[0][2])
    print(answer[0][0] + 1, answer[0][1] + 1)
else:
    print(0)
