n = int(input()) # 회의의 수
time = [list(map(int,input().split())) for _ in range(n)]
# time.sort(key = lambda x: x[1]) 
# 시작하는 시간도 정렬 해줘야 한다. 시작하자마자 끝나는 경우 ex ([4,4],[4,4],[1,4]) 
time.sort(key = lambda x : (x[1],x[0]))


ans = 1
index = 0

for i in range(1,n):
    if time[index][1]<=time[i][0]:
        ans+=1
        index = i
print(ans)