dp = [[0 for _ in range(32)] for _ in range(32)]

for j in range(31):
    dp[0][j+1] = 1

for i in range(1,32):
    for j in range(30):
        dp[i][j+1] = dp[i-1][j+2] + dp[i][j]

while True:
    N = int(input())
    if N == 0:
        break
    print(dp[N][1])


# Mathmatically
# while True:
#     from math import factorial
#     N = int(input())
#     print(int(factorial(2*N)/factorial(N)/(N+1)/factorial(N)))