from collections import deque

def read_board():
    board = 0
    for _ in range(3):
        for c in input():
            board <<= 1
            if c == '*':
                board |= 1
    return board

def bfs():
    dists = {0: 0}
    q = deque([0])
    DR = (0, 0, 0, 1, -1)
    DC = (0, 1, -1, 0, 0)

    while q:
        board = q.popleft()
        dist = dists[board]
        
        for r in range(3):
            for c in range(3):
                new_board = board
                
                for dr, dc in zip(DR, DC):
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nr >= 3 or nc < 0 or nc >= 3:
                        continue
                    new_board ^= 1 << (3 * (2 - nr) + (2 - nc))
                
                if new_board in dists:
                    continue

                q.append(new_board)
                dists[new_board] = dist + 1

    return dists


if __name__ == '__main__':
    result = bfs()
    
    P = int(input())
    for _ in range(P):
        print(result[read_board()])