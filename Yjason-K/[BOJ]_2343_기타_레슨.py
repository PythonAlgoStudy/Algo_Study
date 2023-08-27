# 2343 기타레슨, 이분탐색
# N개의 강의  -> 순서가 바뀌면 안됨
# i번의 강의와 j번의 강의를 같은 블루레이에 녹화하려면 
# i와 j사이의 모든 강의도 같은 블루레이에 녹화해야 한다.

import sys
input = sys.stdin.readline

# mid값을 기준으로 블루레이 강의 들을 나눌 수 있는지 확인하는 함수
def is_divide(lessons, M, mid):
  n_blu = 1 # 블루레이 갯수
  cur_sum = 0 # 현재 블루레이에 담긴 강의의 합
  
  for lesson in lessons:
    # 현재 블루레이에 강의를 추가하는 경우 mid값을 초과하는지 확인
    if cur_sum + lesson > mid:
      n_blu += 1
      cur_sum = lesson
    else:
      cur_sum += lesson
      
  return n_blu <= M

N, M = map(int, input().split()) # N개의 강의, M개의 블루레이
lessons = list(map(int, input().split())) # 강의 모음

answer = 0 # 블루레이 길이
# 가능한 블루레이 크기의 범위는 가장 긴 레슨부터 모든 레슨의 합까지
start, end = max(lessons), sum(lessons)

while start <= end:
  mid = (start + end) // 2
  
  if is_divide(lessons, M, mid):
    answer = mid
    end = mid - 1
  else:
    start = mid + 1

print(answer)
