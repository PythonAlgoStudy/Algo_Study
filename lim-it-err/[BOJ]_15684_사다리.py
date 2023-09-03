# 시뮬레이션과 같은 로직
from collections import defaultdict
from itertools import combinations

answer = 5
N, M, H = map(int, input().split())


field_line = [[0 for i in range(N)] for i in range(H)]


def install_pos(field, pos):
    if field[pos[0]][pos[1]] != 0 or field[pos[0]][pos[1] + 1] != 0:
        return False
    field[pos[0]][pos[1]] = 1
    field[pos[0]][pos[1] + 1] = -1
    return True


for i in range(M):
    height, starting = map(int, input().split())
    install_pos(field_line, (height - 1, starting - 1))


def simulate_by_root(field, root):
    for i in range(H):
        root += field[i][root]
    return root


def is_success(field):
    for i in range(N):
        if i != simulate_by_root(field, i):
            return False
    return True


def get_candidate():
    candidate = []
    for i in range(H):
        for j in range(N):
            if j == N - 1:
                continue
            if field_line[i][j] == 0 and field_line[i][j + 1] == 0:
                candidate.append((i, j))
    return candidate


def every_case(pos_lst):
    new_field = [[field_line[i][j] for j in range(N)] for i in range(H)]
    for pos in pos_lst:
        if install_pos(new_field, pos) is False:
            return False
    if is_success(new_field):
        return True
    return False


candidates = get_candidate()
for i in range(0, 4, 1):
    lst = list(combinations(candidates, i))
    for combination in lst:
        if every_case(combination):
            print(i)
            exit()
print(-1)
