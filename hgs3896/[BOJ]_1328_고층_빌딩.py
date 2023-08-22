from functools import cache

MOD = 1_000_000_007

@cache
def f(n, l, r):
    if (n, l, r) == (1, 1, 1):
        return 1
    v = 0
    if n>1:
        if l>1:
            # 가장 왼쪽에 가장 작은 빌딩을 추가하는 경우
            # N과 L이 1씩 증가 (1가지)
            v += f(n-1, l-1, r)
            v %= MOD
        if r>1:
            # 가장 오른쪽에 가장 작은 빌딩을 추가하는 경우
            # N과 R이 1씩 증가 (1가지)
            v += f(n-1, l, r-1)
            v %= MOD
        if n>2:
            # 가장 왼쪽과 오른쪽을 제외한 곳에 가장 작은 빌딩을 추가하는 경우
            # N만 1씩 증가 (N-1가지 경우의 수 존재)
            v += f(n-1, l, r) * (n - 2)
            v %= MOD
    return v

print(f(*map(int, input().split())))