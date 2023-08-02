R, C, N = map(int, input().split())

bomb_map = [[0] * C for _ in range(R)]
dr, dc = (0, 0, 1, -1), (1, -1, 0, 0)

def explode():
    explode_index = []
    # 폭탄은 동시에 터지기 때문에 터질 폭탄의 위치를 저장해놓고 한번에 터트린다.
    for i in range(R):
        for j in range(C):
            if bomb_map[i][j] > 0:
                bomb_map[i][j] -= 1
                if bomb_map[i][j] == 0:
                    explode_index.append((i, j))
    
    # 폭탄 처리
    for r, c in explode_index:
        for dr_, dc_ in zip(dr, dc):
            nr, nc = r + dr_, c + dc_
            if 0 <= nr < R and 0 <= nc < C:
                bomb_map[nr][nc] = 0

# 초기화
for i in range(R):
    row = input()
    for j in range(C):
        if row[j] == 'O':
            bomb_map[i][j] = 3

# 시뮬레이션
for t in range(1, N+1):
    explode()
    if t % 2 == 0:
        for i in range(R):
            for j in range(C):
                if bomb_map[i][j] == 0:
                    bomb_map[i][j] = 3

# 출력
for row in bomb_map:
    print(''.join('O' if x > 0 else '.' for x in row))