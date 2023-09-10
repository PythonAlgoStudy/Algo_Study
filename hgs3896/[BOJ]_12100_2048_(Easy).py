N = int(input())
Board = [list(map(int, input().split())) for _ in range(N)]

def can_merge(stack):
    return len(stack) >= 2 and stack[-1][0] == stack[-2][0] and not stack[-1][1] and not stack[-2][1]

def iterate_along_with_(board, direction):
    # 상하좌우
    if direction == 0:
        for c in range(N):
            yield (board[r][c] for r in range(N))
    elif direction == 1:
        for c in range(N):
            yield (board[r][c] for r in range(N-1, -1, -1))
    elif direction == 2:
        for r in range(N):
            yield (board[r][c] for c in range(N))
    elif direction == 3:
        for r in range(N):
            yield (board[r][c] for c in range(N-1, -1, -1))

def apply_along_with(board, direction, idx, arr):
    # 상하좌우
    if direction == 0:
        for r, v in enumerate(arr):
            board[r][idx] = v
    elif direction == 1:
        for r, v in enumerate(arr):
            board[N-1-r][idx] = v
    elif direction == 2:
        for c, v in enumerate(arr):
            board[idx][c] = v
    elif direction == 3:
        for c, v in enumerate(arr):
            board[idx][N-1-c] = v

def tilt(board, direction):
    new_board = [[0] * N for _ in range(N)]
    for idx, iterator in enumerate(iterate_along_with_(board, direction)):
        stack = []
        for v in iterator:
            if v != 0:
                stack.append((v, False))
                if can_merge(stack):
                    w, _ = stack.pop()
                    stack.pop()
                    stack.append((2 * w, True))
        apply_along_with(new_board, direction, idx, (v for v, _ in stack))
    return new_board

def maxBlock(board, step=0):
    if step >= 5:
        return max(max(row) for row in board)

    return max(
        maxBlock(tilt(board, d), step+1)
        for d in range(4)
    )

print(maxBlock(Board))