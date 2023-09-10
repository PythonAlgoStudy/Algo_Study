N, L, R = map(int, input().split())

M = 100
dp = [[[0 for _ in range(M+1)] for _ in range(M+1)] for _ in range(M+1)]
dp[1][1][1] = 1

for i in range(2, N+1):
    for j in range(1, L+1):
        for k in range(1, R+1):
            dp[i][j][k] = dp[i-1][j-1][k] + dp[i-1][j][k-1] + dp[i-1][j][k]*(i-2)
            
print(dp[N][L][R]%1000000007)

# N을 하나 늘리는 경우를 고려하자
# N=i-1의 경우에서 모든 빌딩의 높이를 하나씩 늘리고
# 크기 1짜리 빌딩을 왼쪽에 추가하면 i, L+1, R의 경우가 된다
# 크기 1짜리 빌딩을 오른쪽에 추가하면 i, L, R+1의 경우가 된다
# 크기 1짜리 빌딩을 중간에 추가하면 i, L, R의 경우가 된다 ("빌딩 중간"이 i-2개 있으므로 i-2를 곱해준다)
