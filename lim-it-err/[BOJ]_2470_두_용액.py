N = int(input())
arr = list(map(int, input().split()))
arr.sort()
start, end = 0, N-1
min_sum = 999999999999999
result = (start, end)
while start < end:
    sum = arr[start]+arr[end]
    if abs(min_sum) > abs(sum):
        result = (arr[start], arr[end])
    min_sum = min(abs(min_sum),abs(sum))
    if sum<0:
        start+=1
    else:
        end-=1
print(result[0], result[1])