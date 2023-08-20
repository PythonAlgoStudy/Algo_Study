# 테트로미노 ((높이, 너비), [각 테트로미노의 모양에 대응되는 상대 좌표 값])
tetromino = [
    ((1, 4), [(0, 0), (0, 1), (0, 2), (0, 3)]),
    ((2, 2), [(0, 0), (0, 1), (1, 0), (1, 1)]),
    ((3, 2), [(0, 0), (1, 0), (2, 0), (2, 1)]),
    ((3, 2), [(0, 0), (1, 0), (1, 1), (2, 1)]),
    ((2, 3), [(0, 0), (0, 1), (0, 2), (1, 1)]),
]

# 회전시 상대 좌표 값 변환 함수들
rotate_methods = [
    lambda dr, dc: (dr, dc),   # 원본
    lambda dr, dc: (dc, -dr),  # 90도 회전
    lambda dr, dc: (-dr, -dc), # 180도 회전
    lambda dr, dc: (-dc, dr),  # 270도 회전
]

# 대칭시 상대 좌표 값 변환 함수들
# (원점대칭은 180도 회전과 동일하기 때문에 제외)
symetric_methods = [
    lambda dr, dc: (dr, dc),   # 원본
    lambda dr, dc: (-dr, dc),  # 상하대칭
    lambda dr, dc: (dr, -dc),  # 좌우대칭
]

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

def findMaxTetrominoSum():
    ans = 0
    for (h, w), rel_pos_arr in tetromino:
        for rot_func in rotate_methods:
            for sym_func in symetric_methods:
                dh, dw = sym_func(*rot_func(h - 1, w - 1))
                delta_pos_arr = list(map(lambda t: sym_func(*rot_func(*t)), rel_pos_arr))

                # 시작점 (r, c)에서 끝점 (r + dh, c + dw)까지
                # 범위 내 영역인지 확인 후 합을 구한다
                for r in range(N):
                    if not 0 <= r + dh < N:
                        continue
                    for c in range(M):
                        if not 0 <= c + dw < M:
                            continue
                        s = sum(board[r+dr][c+dc] for dr, dc in delta_pos_arr)
                        ans = max(ans, s)
    return ans

print(findMaxTetrominoSum())