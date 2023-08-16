import sys

n, m = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

left, right = max(arr), sum(arr)
ans = right

# 해당 블루레이 크기로 모두 녹화가 가능한지 확인
def is_possible(target):
    cnt = 1
    s = 0
    for i in range(n):
        if (s + arr[i]) <= target:
            s += arr[i]
        else:
            s = arr[i]
            cnt += 1

        if cnt > m:
            return False
    return True

while left <= right:
    mid = (left + right) // 2

    # 해당 블루레이 크기가
    # 가능하다면
    if is_possible(mid):
        # 답을 갱신하고, 더 작은 크기로 탐색
        ans = min(ans, mid)
        right = mid - 1
    # 불가능하다면
    else:
        # 더 큰 크기에서 탐색
        left = mid + 1
print(ans)