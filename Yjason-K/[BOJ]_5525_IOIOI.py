# 5525 IOIOI
import sys
input = sys.stdin.readline

N = int(input()) # Pn
M = int(input()) # S의 길이
S = input() # I와 O로만 이루어진 문자열
P = 'I' + "OI" * N

count = 0  # 찾은 패턴의 수
answer = 0  # 정답

i = 1
# 문자열을 한번만 순회하면서 패턴 찾기
while i < M - 1:
    if S[i-1:i+2] == 'IOI':
        count += 1
        if count == N:  # n개의 패턴을 찾았다면
            count -= 1  # 패턴이 겹치게 되므로 하나를 빼준다
            answer += 1  # 정답을 증가시킨다
        i += 1  # 현재 패턴의 다음 문자로 이동
    else:
        count = 0  # 패턴이 아니라면 초기화
    i += 1

print(answer)

## 50점, 태스크 1만 통과된 경우
# S[i:i+2*N +1] == P  O(N)의 시간 복잡도
# 전체 시간 복잡도는 O(N^2)
# import sys
# input = sys.stdin.readline

# N = int(input()) # Pn
# M = int(input()) # S의 길이
# S = input() # I와 O로만 이루어진 문자열
# P = 'I' + "OI" * N

# answer = 0
# i = 0
# while i < (M - 2*N):
#     if S[i:i+2*N +1] == P:
#       answer +=1
#       i +=2
#     else:
#       i +=1

# print(answer)