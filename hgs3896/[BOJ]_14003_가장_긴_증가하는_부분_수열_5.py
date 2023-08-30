# 풀이시간: 1시간
def read_input():
    import sys
    N = int(sys.stdin.readline())
    A = list(map(int, sys.stdin.readline().rstrip().split()))
    return N, A

def LIS(N, A):
    # BOJ에서 제공되는 pypy 특정 버전엔 bisect_left에서 key를 입력받는 버전이 없어 type error가 남
    from bisect import bisect_left
    B = []
    P = [-1] * N
    for i, v in enumerate(A):
        j = bisect_left(B, v, key=lambda idx: A[idx])
        if j == len(B):
            if B:
                P[i] = B[-1]
            B.append(i)
        else:
            if j > 0:
                P[i] = B[j-1]
            B[j] = i

    result = []
    idx = B[-1]
    while idx != -1:
        result.append(A[idx])
        idx = P[idx]
    result.reverse()
    return result

B = LIS(*read_input())
print(len(B))
print(*B)