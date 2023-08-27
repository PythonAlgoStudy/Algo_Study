N, M = map(int, input().split())
board = [input() for _ in range(N)]

# 보드를 기울일때마다 변화하는 상태는 오직 빨간 구슬과 파란 구슬의 위치 값인데
# 이는 각각이 3~10 정수에 해당되는 2차원 좌표 값이므로
# 보드의 상태를 40비트 정수로 압축할 수 있다.

def compress_pos(r_pos, b_pos):
    return (r_pos[0] << 30) | (r_pos[1] << 20) | (b_pos[0] << 10) | (b_pos[1])

def decompress_pos(cpos):
    mask = (1 << 10) - 1
    b_pos = ((cpos >> 10) & mask, cpos & mask)
    cpos >>= 20
    r_pos = ((cpos >> 10) & mask, cpos & mask)
    return r_pos, b_pos

directions = [
    # left, right, up, down
    (0, -1), (0, 1), (-1, 0), (1, 0)
]

# Find Position
R_pos, B_pos, O_pos = None, None, None
for r in range(N):
    for c in range(M):
        if board[r][c] == 'R':
            R_pos = (r, c)
        if board[r][c] == 'B':
            B_pos = (r, c)
        if board[r][c] == 'O':
            O_pos = (r, c)

# 보드의 상태가 주어질 때 각 방향으로 기울인 후의 보드의 상태를 제공하는 함수
def tilt(board_state, dr, dc):
    # 각각의 동작에서 공은 동시에 움직인다
    # 빨간 구슬이 구멍에 빠지면 성공이지만, 파란 구슬이 구멍에 빠지면 실패
    # 빨간 구슬과 파란 구슬이 동시에 구멍에 빠져도 실패
    # 기울이는 동작을 그만하는 것은 더 이상 구슬이 움직이지 않을 때 까지이다.
    r_pos, b_pos = decompress_pos(board_state)
    
    moving = True
    while moving:
        moving = False

        new_r_pos = (r_pos[0] + dr, r_pos[1] + dc)
        # 빨간 구슬이 현재 위치가 구멍이 아니고 다음 위치가 벽이 아닐 때
        if r_pos != O_pos and board[new_r_pos[0]][new_r_pos[1]] != '#':
            # 다음 위치가 구멍이거나 파란 구슬이 아닐때만 이동가능
            if new_r_pos == O_pos or new_r_pos != b_pos:
                moving = True
                r_pos = new_r_pos        

        new_b_pos = (b_pos[0] + dr, b_pos[1] + dc)
        # 파란 구슬이 현재 위치가 구멍이 아니고 다음 위치가 벽이 아닐 때
        if b_pos != O_pos and board[new_b_pos[0]][new_b_pos[1]] != '#':
            # 다음 위치가 구멍이거나 빨간 구슬이 아닐때만 이동가능
            if new_b_pos == O_pos or new_b_pos != r_pos:
                moving = True
                b_pos = new_b_pos

    return compress_pos(r_pos, b_pos)

# Board Pruning을 위한 자료구조
minimum_moves_to_escape = {}

threshold = 10
def search(board_state, depth):
    # 10번 이하로 빨간 구슬을 구멍을 통해 빼낼 수 있는지를 검사하는 함수
    r_pos, b_pos = decompress_pos(board_state)
    
    # 빨간 구슬이 이미 구멍에 도착했다면
    if r_pos == O_pos:
        # 파란 구슬이 구멍에 도착하지 않은 경우 성공
        return b_pos != O_pos, depth

    # 10번 이하로 성공 불가
    if depth >= threshold:
        return False, depth
    
    # 탐색중 한번 마주쳤던 보드의 상태라면 현재 탐색에서 10번 이내로 탐색 가능한지 확인 후 가능하다면 성공 처리
    if board_state in minimum_moves_to_escape and depth + minimum_moves_to_escape[board_state] <= threshold:
        return True, depth + minimum_moves_to_escape[board_state]

    for dr, dc in directions:
        # 각 방향으로 기울이기
        new_board_state = tilt(board_state, dr, dc)

        # 기울인 새로운 상태의 board를 가지고 그 다음번 탐색에서 사용
        can_escape, d = search(new_board_state, depth+1)
        # 10번 이내에 통과 가능하다면
        if can_escape:
            # d(성공한 시점에서의 depth) - depth(현재 depth)를 이용해 현재 board 상태에서 몇 번의 기울이기로 성공 상태의 board로 가는지의 최솟값을 저장
            minimum_moves_to_escape[new_board_state] = min(d - depth, minimum_moves_to_escape.get(new_board_state, threshold + 1))
            return True, d

    return False, depth

result, _ = search(compress_pos(R_pos, B_pos), 0)
if result:
    print(1)
else:
    print(0)