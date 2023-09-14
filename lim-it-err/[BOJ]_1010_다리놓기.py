from math import factorial

num = int(input())
for _ in range(num):
    M, N = map(int, input().split())
    numerator, denominator = factorial(N), factorial(M) * factorial(N - M)
    print(numerator // denominator)
