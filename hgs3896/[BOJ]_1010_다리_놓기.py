# N번만큼 1~M사이 숫자를 중복 없이 순서와 상관 없이 뽑는 것
# => mCn
# 풀이 시간 5분
from functools import cache

@cache
def nCr(n, r):
    if r == 0 or r == n:
        return 1
    return nCr(n-1, r-1) + nCr(n-1, r)

for _ in range(int(input())):
    N, M = map(int, input().split())
    print(nCr(M, N))