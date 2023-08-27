# 회의의 최대 개수 구하기
import sys

input = sys.stdin.readline
N = int(input()) # 주어진 회의의 갯수
meetings = [ list(map(int, input().split())) for _ in range(N) ] # 전체회의 목록
# 끝나는 시간이 빠른것부터 오름차순 -> 시작이 빠른 순서로 오름차순
meetings.sort(key= lambda x: (x[1], x[0]))

ans = 1 # 가능한 회의 갯수 count
end_time = meetings[0][1] # 회의 처음 끝나는 시간
for meeting in meetings[1:]:
    # 다음 회의 시작 시간과 이전 회의 끝나느 시간 비교
    if meeting[0] >= end_time:
      ans += 1
      end_time = meeting[1]
      
print(ans)