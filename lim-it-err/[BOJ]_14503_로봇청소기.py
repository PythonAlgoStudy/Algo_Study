from collections import deque

N, M = map(int, input().split())
x, y, d = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(N)]
is_valid = (
    lambda x, y: 0 <= x < N and 0 <= y < M and field[x][y] != 1
    if True
    else False  # 1 : Wall
)
dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]
cnt = 0


def is_surround_clean(x, y):
    for dx, dy in zip(dxs, dys):
        if is_valid(x + dx, y + dy):
            if field[x + dx][y + dy] == 0:
                return False
    return True


while True:
    if field[x][y] == 0:  # Not Clean
        field[x][y] = 2  # Clean
        cnt += 1
    if is_surround_clean(x, y):
        if d == 0:  # North
            if is_valid(x + 1, y):
                x += 1
            else:
                break
        elif d == 1:  # East
            if is_valid(x, y - 1):
                y -= 1
            else:
                break

        elif d == 2:  # South
            if is_valid(x - 1, y):
                x -= 1
            else:
                break

        elif d == 3:  # West
            if is_valid(x, y + 1):
                y += 1
            else:
                break

    else:
        d = (d - 1) % 4
        if d == 0:  # North
            if not is_valid(x - 1, y):
                pass
            elif field[x - 1][y] == 0:
                cnt += 1
                x -= 1
                field[x][y] = 2
            else:
                pass

        elif d == 1:  # East
            if not is_valid(x, y + 1):
                pass
            elif field[x][y + 1] == 0:
                cnt += 1
                y += 1
                field[x][y] = 2
            else:
                pass

        elif d == 2:  # South
            if not (is_valid(x + 1, y)):
                pass
            elif field[x + 1][y] == 0:
                cnt += 1
                x += 1
                field[x][y] = 2
            else:
                pass

        elif d == 3:  # West
            if not is_valid(x, y - 1):
                pass
            elif field[x][y - 1] == 0:
                cnt += 1
                y -= 1
                field[x][y] = 2
            else:
                pass
print(cnt)
