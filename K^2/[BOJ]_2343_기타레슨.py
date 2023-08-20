import sys
input = sys.stdin.readline

# 이진탐색-> str,end 결정 ,분할 조건, 분할불가시 종료
# 기존 n,m 
n,m = map(int,input().rstrip().split())
arr =list(map(int,input().rstrip().split()))

start,end= max(arr), sum(arr)

# 이진 탐색 일반종료조건
while start <= end:
    mid = (start+end)//2
    limit =0
    div =1
    # 이진탐색위한 분할조건 구현
    #mid 크기를 가진 블루레이 주어진자료와 비교
    # 원하는 블루레이 갯수와 일치하는지 비교
    for i in range (n):
        limit += arr[i]
        if limit > mid:
            div += 1
            limit =arr[i]
    # div = 블루레이 갯수 많을시 블루레이 최대 크기 증가 / 그외 반대
    if div <= m:
        answer = mid
        end = mid -1
    else: 
        start = mid +1
print(answer)

