# 4881 알약/ 수학, 다이나믹 프로그래밍

import sys
input = sys.stdin.readline

# dp 배열 만들기
dp = [ [0] * 31 for _ in range(31) ]

for i in range(1, 31):
  dp[1][i] = i
  
for i in range(2, 31):
  for j in range(i, 31):
    dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
while (N := int(input())) != 0:
  print(dp[N][N])