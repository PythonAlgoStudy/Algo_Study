# 풀이시간: 8시간
def read_input():
    import sys
    input = lambda: sys.stdin.readline().rstrip()
    N, M, H = map(int, input().split(' '))
    ladders = [[False] * H for _ in range(N-1)]
    for _ in range(M):
        a, b = map(int, input().split(' '))
        ladders[b-1][a-1] = True
    return N, H, ladders

def solve(N, H, ladders):
    INF = 10**7
    threshold = 3

    def is_identical_ladder(ladders):
        # path 검증
        for original_idx in range(N-1):
            idx = original_idx
            for row_idx in range(H):
                if idx > 0 and ladders[idx - 1][row_idx]:
                    idx -= 1
                elif idx < N-1 and ladders[idx][row_idx]:
                    idx += 1
            if idx != original_idx:
                return False
        return True
    
    def dfs(ladders, num_ladders_added, prev, step):
        if is_identical_ladder(ladders):
            return num_ladders_added
        if step >= threshold:
            return INF
        ret = dfs(ladders, num_ladders_added, prev, step+1)
        for col_idx in range(N-1):
            for row_idx in range(H):
                if ladders[col_idx][row_idx]:
                    continue
                if col_idx > 0 and ladders[col_idx-1][row_idx]:
                    continue
                if col_idx+1 < N-1 and ladders[col_idx+1][row_idx]:
                    continue
                if (col_idx, row_idx) <= prev:
                    continue
                ladders[col_idx][row_idx] = True
                ret = min(ret, dfs(ladders, num_ladders_added + 1, (col_idx, row_idx), step+1))
                ladders[col_idx][row_idx] = False
        return ret

    result = dfs(ladders, 0, (-1, -1), 0)
    if result == INF:
        return -1
    return result

print(solve(*read_input()))