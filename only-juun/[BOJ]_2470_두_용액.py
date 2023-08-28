import sys

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

start, end = 0, n - 1
cnt = sys.maxsize
answer = [0, 0]

while start != end:
    left, right = arr[start], arr[end]

    x = left + right
    # 절댓값이 현재의 최솟값보다 작거나 같으면 답 갱신
    if abs(x) <= cnt:
        cnt = min(abs(x), cnt)
        answer = [left, right]
    
    # 0에 가까워지기 위해
    # 음수인 경우, 왼쪽 포인터를 이동
    if x < 0:
        start += 1
    # 양수인 경우, 오른쪽 포인터를 이동
    else:
        end -= 1
    
print(*answer)
