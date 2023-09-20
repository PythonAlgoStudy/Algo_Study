# 5분
import sys
from bisect import bisect_left
T = int(sys.stdin.readline())
while T:
    T -= 1
    _ = sys.stdin.readline()
    A = map(int, sys.stdin.readline().split())
    B = list(map(int, sys.stdin.readline().split()))
    B.sort()
    print(sum(bisect_left(B, a) for a in A))