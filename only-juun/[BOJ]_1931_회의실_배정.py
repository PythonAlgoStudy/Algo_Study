n = int(input())
meetings = [list(map(int,input().split())) for _ in range(n)]
meetings.sort(key = lambda x: (x[1], x[0]))

ans = 0
end = 0
for a in meetings:
    if a[0] >= end:
        ans += 1
        end = a[1]
        
print(ans)