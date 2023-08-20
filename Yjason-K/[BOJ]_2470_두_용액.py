# 2470 알약, 정렬/ 이분탐색 / 두 포인터
# 양수 산성, 음수 알칼리성

import sys
input = sys.stdin.readline

def find_answer():
    left, right = 0, N-1 # 포인터 설정
    min_sum = float('inf') # 줄여나가야할 값
    answer = [] # 특성값이 0에 가장 가까운 배열

    # left, right를 조절해가며 특성값이 0에 가깝게 만들기
    while left < right:
      # 현재 특성값
      cur_sum = features[left] + features[right]

      # 특성값 갱신
      if abs(cur_sum) < abs(min_sum):
        min_sum = cur_sum
        answer = [features[left], features[right]]

      # 합이 0보다 작으면 left를 +1 이동
      if cur_sum < 0:
        left += 1
      # 합이 0보다 크면 right를 -1 이동
      else:
        right -= 1
      
    return answer

N = int(input()) # 전체 용액의 수
# 용액의 특성들 배열, 오름차순 정렬
features = sorted(list(map(int, input().split())))

answer = find_answer()
print(answer[0], answer[1])
