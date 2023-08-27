import sys
input_ = sys.stdin.readline
N = int(input_())
meetings = [tuple(map(int, input_().split())) for _ in range(N)]
# 먼저 끝나되 끝나는 시간이 같다면 먼저 시작하는 회의 순으로 정렬
meetings.sort(key=lambda x: (x[1], x[0]))
curr, cnt = 0, 0
while curr < N:
    prev = curr
    curr += 1
    cnt += 1
    # prev의 회의가 끝나자마자 시작될 수 있는 회의를 찾아 curr에 갱신하기
    while curr < N and meetings[prev][1] > meetings[curr][0]:
        curr += 1
print(cnt)