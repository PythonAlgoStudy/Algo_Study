import sys

# n= int(input)  = 총 회의 수
n= int(sys.stdin.readline())
# n 개 갯수만큼 [0.0]을 넣는다 이차원 배열
time = [[0]*2 for _ in range(n)]
#print(time)
# 튜플로 key에 여러인자를 주면 순서대로 정렬한다
for i in range(n):
    s,e = map(int,sys.stdin.readline().split())
    time[i][0] = s
    time[i][1] = e
time.sort(key=lambda x :(x[1],x[0]))

cnt = 1
# 마지막 시간에 각각 time [0] [1] 값을 찾는다
end_time = time[0][1]
for i in range(1,n):
    if time[i][0] >= end_time:
        cnt +=1
        end_time =time[i][1]
        # 시작하는 시간이  움직임
print(cnt)