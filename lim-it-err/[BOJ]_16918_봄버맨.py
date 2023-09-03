R, C, N = map(int, input().split())
init_map = []

for i in range(R):
    init_map.append(input())

countmap = [[-100 if init_map[i][j]=="." else 0 for j in range(C)] for i in range(R)] # Remaining Seconds
is_valid = lambda x, y: 0<=x<R and 0<=y<C if True else False
dx, dy = [1, 0, 0, -1], [0, 1, -1, 0] #

def get_candidate(_map, second):
    explode_candidate = []
    for i in range(R):
        for j in range(C):
            if _map[i][j] == second-3:
                explode_candidate.append((i, j))
    return explode_candidate

def explode(_countmap, _candidates):
    for candidate in _candidates:
        x, y = candidate
        _countmap[x][y] = -100
        for i in range(4):
            if is_valid(x+dx[i], y+dy[i]):
                _countmap[x+dx[i]][y+dy[i]] = -100
    return _countmap

def fill_bomb(_countmap, second):
    return [[_countmap[i][j] if _countmap[i][j]!=-100 else second for j in range(C)] for i in range(R)]  # Remaining Seconds

for i in range(1, N+1):
    if i%2:
        candidate = get_candidate(countmap, i)
        countmap = explode(countmap, candidate)
    else:
        countmap = fill_bomb(countmap, i)

result = [["O" if countmap[i][j]!=-100 else "." for j in range(C)] for i in range(R)]
for i in range(R):
    print("".join(result[i]))
